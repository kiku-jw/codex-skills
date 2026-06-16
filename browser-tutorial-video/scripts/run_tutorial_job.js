#!/usr/bin/env node
"use strict";

const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const { createRequire } = require("node:module");
const path = require("node:path");
const { pathToFileURL } = require("node:url");

function usage() {
  return [
    "Usage:",
    "  run_tutorial_job.js --job tutorial-job.json [options]",
    "",
    "Options:",
    "  --out DIR       Override job outputDir.",
    "  --headed        Run browser visibly.",
    "  --skip-qa       Do not run tutorial_video_qa.js after render.",
  ].join("\n");
}

function parseArgs(argv) {
  const args = { headed: false, skipQa: false };
  for (let index = 0; index < argv.length; index += 1) {
    const key = argv[index];
    if (key === "--help" || key === "-h") {
      console.log(usage());
      process.exit(0);
    }
    if (key === "--headed") {
      args.headed = true;
      continue;
    }
    if (key === "--skip-qa") {
      args.skipQa = true;
      continue;
    }
    const value = argv[index + 1];
    if (!key.startsWith("--")) throw new Error(`unexpected argument: ${key}`);
    if (value === undefined || value.startsWith("--")) throw new Error(`missing value for ${key}`);
    index += 1;
    if (key === "--job") args.job = value;
    else if (key === "--out") args.out = value;
    else throw new Error(`unknown option: ${key}`);
  }
  if (!args.job) throw new Error("--job is required");
  return args;
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    encoding: "utf8",
    stdio: options.stdio || "pipe",
  });
  if (result.error) throw result.error;
  if (result.status !== 0) {
    const stderr = result.stderr ? `\n${result.stderr}` : "";
    throw new Error(`${command} failed with exit ${result.status}${stderr}`);
  }
  return result.stdout || "";
}

function loadPlaywright() {
  const candidates = [
    path.join(process.cwd(), "noop.js"),
    path.join(__dirname, "noop.js"),
  ];
  for (const candidate of candidates) {
    try {
      return createRequire(candidate)("playwright");
    } catch (_error) {
      // Try the next resolution root.
    }
  }
  throw new Error("playwright is required. Run this from a project with playwright installed.");
}

function readJob(jobPath) {
  const absolute = path.resolve(jobPath);
  const job = JSON.parse(fs.readFileSync(absolute, "utf8"));
  return { job, jobPath: absolute, jobDir: path.dirname(absolute) };
}

function resolveOutputDir(job, jobDir, override) {
  const value = override || job.outputDir || "./out/tutorial-video";
  return path.isAbsolute(value) ? value : path.resolve(jobDir, value);
}

function resolveUrl(rawUrl, jobDir) {
  if (!rawUrl) throw new Error("job.startUrl is required");
  if (/^(https?:|file:|data:)/.test(rawUrl)) return rawUrl;
  return pathToFileURL(path.resolve(jobDir, rawUrl)).href;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function assertPositiveInteger(value, fallback, name) {
  const number = Number(value === undefined ? fallback : value);
  if (!Number.isInteger(number) || number <= 0) throw new Error(`${name} must be a positive integer`);
  return number;
}

async function installOverlay(page, zoom) {
  await page.addStyleTag({
    content: `
      html, body, * { cursor: none !important; }
      body > :not(#demo-overlay-root) { zoom: ${zoom}; }
      #demo-overlay-root {
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 2147483647;
      }
      .demo-cursor {
        position: absolute;
        width: 46px;
        height: 46px;
        transform: translate(-4px, -2px);
        filter: drop-shadow(0 4px 8px rgba(0,0,0,.45));
      }
      .demo-highlight {
        position: absolute;
        border: 5px solid rgba(255, 214, 10, .95);
        border-radius: 10px;
        box-shadow: 0 0 0 5px rgba(255, 214, 10, .24), 0 0 28px rgba(255, 214, 10, .7);
        background: rgba(255, 214, 10, .12);
        opacity: 0;
        transition: opacity .18s ease;
      }
      .demo-ripple {
        position: absolute;
        width: 34px;
        height: 34px;
        margin: -17px 0 0 -17px;
        border-radius: 999px;
        border: 5px solid rgba(255, 214, 10, .95);
        animation: demo-ripple .42s ease-out forwards;
      }
      @keyframes demo-ripple {
        from { transform: scale(.35); opacity: 1; }
        to { transform: scale(2.5); opacity: 0; }
      }
    `,
  });
  await page.evaluate(() => {
    const existing = document.getElementById("demo-overlay-root");
    if (existing) existing.remove();
    const root = document.createElement("div");
    root.id = "demo-overlay-root";
    const highlight = document.createElement("div");
    highlight.className = "demo-highlight";
    const cursor = document.createElement("div");
    cursor.className = "demo-cursor";
    cursor.innerHTML = `
      <svg width="46" height="46" viewBox="0 0 46 46" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M8 5L34 26L22 28L17 40L8 5Z" fill="white" stroke="black" stroke-width="3" stroke-linejoin="round"/>
      </svg>`;
    root.appendChild(highlight);
    root.appendChild(cursor);
    document.body.appendChild(root);
    window.__tutorialOverlay = {
      setCursor(x, y) {
        cursor.style.left = `${x}px`;
        cursor.style.top = `${y}px`;
      },
      moveCursor(x, y, duration) {
        return new Promise((resolve) => {
          cursor.style.transition = `left ${duration}ms ease, top ${duration}ms ease`;
          cursor.style.left = `${x}px`;
          cursor.style.top = `${y}px`;
          window.setTimeout(() => {
            cursor.style.transition = "";
            resolve();
          }, duration);
        });
      },
      highlight(box) {
        highlight.style.left = `${box.x - 8}px`;
        highlight.style.top = `${box.y - 8}px`;
        highlight.style.width = `${box.width + 16}px`;
        highlight.style.height = `${box.height + 16}px`;
        highlight.style.opacity = "1";
      },
      clearHighlight() {
        highlight.style.opacity = "0";
      },
      ripple(x, y) {
        const ripple = document.createElement("div");
        ripple.className = "demo-ripple";
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        root.appendChild(ripple);
        window.setTimeout(() => ripple.remove(), 500);
      },
    };
    window.__tutorialOverlay.setCursor(120, 120);
  });
}

async function startCapture(page, framesDir, fps) {
  let frame = 0;
  let stopped = false;
  const interval = 1000 / fps;
  const capture = async () => {
    while (!stopped) {
      const started = Date.now();
      frame += 1;
      const file = path.join(framesDir, `frame-${String(frame).padStart(6, "0")}.jpg`);
      await page.screenshot({ path: file, type: "jpeg", quality: 95 });
      const elapsed = Date.now() - started;
      await sleep(Math.max(0, interval - elapsed));
    }
  };
  const promise = capture();
  return {
    stop: async () => {
      stopped = true;
      await promise;
      return frame;
    },
  };
}

async function locatorForAction(page, action) {
  if (action.selector) return page.locator(action.selector).first();
  if (action.text) return page.getByText(action.text, { exact: Boolean(action.exact) }).first();
  throw new Error("click action needs selector or text");
}

async function clickAction(page, action, clicks, startedAt) {
  const locator = await locatorForAction(page, action);
  await locator.waitFor({ state: "visible", timeout: action.timeoutMs || 10000 });
  const box = await locator.boundingBox();
  if (!box) throw new Error(`click target has no bounding box: ${action.label || action.selector || action.text}`);
  const point = { x: box.x + box.width / 2, y: box.y + box.height / 2 };
  await page.evaluate((targetBox) => window.__tutorialOverlay.highlight(targetBox), box);
  await sleep(action.highlightMs || 420);
  await page.evaluate((targetPoint) => window.__tutorialOverlay.moveCursor(targetPoint.x, targetPoint.y, 650), point);
  await sleep(action.preClickMs || 180);
  const at = (Date.now() - startedAt) / 1000;
  clicks.push({ at, x: Math.round(point.x), y: Math.round(point.y), label: action.label || action.selector || action.text });
  await page.evaluate((targetPoint) => window.__tutorialOverlay.ripple(targetPoint.x, targetPoint.y), point);
  await page.mouse.click(point.x, point.y, { delay: 70 });
  await sleep(action.afterMs || 300);
  await page.evaluate(() => window.__tutorialOverlay.clearHighlight());
}

async function scrollAction(page, action) {
  const y = Number(action.y || action.deltaY || 0);
  const duration = Number(action.durationMs || 900);
  await page.evaluate(({ y: targetY, durationMs }) => new Promise((resolve) => {
    const start = window.scrollY;
    const end = start + targetY;
    const startedAt = performance.now();
    const tick = (now) => {
      const progress = Math.min(1, (now - startedAt) / durationMs);
      const eased = progress < 0.5 ? 2 * progress * progress : -1 + (4 - 2 * progress) * progress;
      window.scrollTo(0, start + (end - start) * eased);
      if (progress < 1) window.requestAnimationFrame(tick);
      else resolve();
    };
    window.requestAnimationFrame(tick);
  }), { y, durationMs: duration });
}

async function performAction(page, action, context) {
  if (action.type === "wait") {
    await sleep(Number(action.ms || 500));
  } else if (action.type === "goto") {
    await page.goto(resolveUrl(action.url, context.jobDir), { waitUntil: action.waitUntil || "domcontentloaded" });
    await installOverlay(page, context.zoom);
    await sleep(Number(action.afterMs || 500));
  } else if (action.type === "click") {
    await clickAction(page, action, context.clicks, context.startedAt);
  } else if (action.type === "scroll") {
    await scrollAction(page, action);
    await sleep(Number(action.afterMs || 250));
  } else {
    throw new Error(`unsupported action type: ${action.type}`);
  }
}

function renderVideo(framesDir, finalVideo, fps) {
  run("ffmpeg", [
    "-hide_banner",
    "-loglevel",
    "error",
    "-y",
    "-framerate",
    String(fps),
    "-i",
    path.join(framesDir, "frame-%06d.jpg"),
    "-vf",
    "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p",
    "-c:v",
    "libx264",
    "-crf",
    "14",
    "-preset",
    "slow",
    "-pix_fmt",
    "yuv420p",
    "-color_range",
    "tv",
    "-colorspace",
    "bt709",
    "-color_primaries",
    "bt709",
    "-color_trc",
    "bt709",
    "-movflags",
    "+faststart",
    finalVideo,
  ]);
}

function runQa(finalVideo, clicksPath, qaDir, job) {
  const qaScript = path.resolve(__dirname, "tutorial_video_qa.js");
  const args = [qaScript, "--video", finalVideo, "--clicks", clicksPath, "--out", qaDir];
  if (job.qa && job.qa.every !== undefined) args.push("--every", String(job.qa.every));
  if (job.qa && Array.isArray(job.qa.checkpoints) && job.qa.checkpoints.length > 0) {
    args.push("--checkpoint", job.qa.checkpoints.join(","));
  }
  if (job.qa && Array.isArray(job.qa.pdfEnds) && job.qa.pdfEnds.length > 0) {
    args.push("--pdf-end", job.qa.pdfEnds.join(","));
  }
  run(process.execPath, args, { stdio: "inherit" });
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const { chromium } = loadPlaywright();
  const { job, jobPath, jobDir } = readJob(args.job);
  const outputDir = resolveOutputDir(job, jobDir, args.out);
  const framesDir = path.join(outputDir, "frames");
  const qaDir = path.join(outputDir, "qa");
  fs.mkdirSync(framesDir, { recursive: true });
  fs.mkdirSync(qaDir, { recursive: true });

  const fps = assertPositiveInteger(job.fps, 15, "job.fps");
  const viewport = {
    width: assertPositiveInteger(job.viewport && job.viewport.width, 1280, "viewport.width"),
    height: assertPositiveInteger(job.viewport && job.viewport.height, 720, "viewport.height"),
  };
  const zoom = Number(job.zoom === undefined ? 1 : job.zoom);
  if (!Number.isFinite(zoom) || zoom <= 0) throw new Error("job.zoom must be positive");

  const launchOptions = { headless: args.headed ? false : job.headless !== false };
  if (job.browserChannel) launchOptions.channel = job.browserChannel;
  const browser = await chromium.launch(launchOptions);
  const page = await browser.newPage({ viewport });
  const clicks = [];
  const startedAt = Date.now();
  let frameCount = 0;
  try {
    await page.goto(resolveUrl(job.startUrl, jobDir), { waitUntil: job.waitUntil || "domcontentloaded" });
    await installOverlay(page, zoom);
    await sleep(Number(job.initialWaitMs || 500));
    const capture = await startCapture(page, framesDir, fps);
    for (const action of job.actions || []) {
      await performAction(page, action, { jobDir, clicks, startedAt, zoom });
    }
    await sleep(Number(job.finalWaitMs || 600));
    frameCount = await capture.stop();
  } finally {
    await browser.close();
  }

  if (frameCount === 0) throw new Error("no frames captured");
  const finalVideo = path.join(outputDir, "final.mp4");
  renderVideo(framesDir, finalVideo, fps);
  const clicksPath = path.join(outputDir, "clicks.json");
  fs.writeFileSync(clicksPath, `${JSON.stringify({ clicks }, null, 2)}\n`, "utf8");
  if (!args.skipQa) runQa(finalVideo, clicksPath, qaDir, job);

  const summary = {
    title: job.title || "Browser tutorial video",
    jobPath,
    outputDir,
    finalVideo,
    clicksPath,
    qaDir,
    framesDir,
    frameCount,
    fps,
    viewport,
    clicks: clicks.length,
  };
  const summaryPath = path.join(outputDir, "run-summary.json");
  fs.writeFileSync(summaryPath, `${JSON.stringify(summary, null, 2)}\n`, "utf8");
  console.log(summaryPath);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
