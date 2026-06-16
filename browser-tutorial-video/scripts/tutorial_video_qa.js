#!/usr/bin/env node
"use strict";

const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");

function usage() {
  return [
    "Usage:",
    "  tutorial_video_qa.js --video final.mp4 --out qa-dir [options]",
    "",
    "Options:",
    "  --clicks clicks.json       JSON array or object with a clicks array.",
    "  --pdf-end seconds[,..]      Long-scroll/PDF checkpoint timestamps.",
    "  --checkpoint seconds[,..]   Extra checkpoint timestamps.",
    "  --every seconds            Extract interval frames every N seconds.",
    "  --pre-offset seconds       Pre-click frame offset. Default: 0.8.",
    "  --post-offset seconds      Post-click frame offset. Default: 0.2.",
    "  --tile-cols count          Contact sheet columns. Default: 4.",
  ].join("\n");
}

function parseArgs(argv) {
  const args = {
    checkpoints: [],
    pdfEnds: [],
    every: null,
    preOffset: 0.8,
    postOffset: 0.2,
    tileCols: 4,
  };
  for (let index = 0; index < argv.length; index += 1) {
    const key = argv[index];
    const value = argv[index + 1];
    if (key === "--help" || key === "-h") {
      console.log(usage());
      process.exit(0);
    }
    if (!key.startsWith("--")) {
      throw new Error(`unexpected argument: ${key}`);
    }
    if (value === undefined || value.startsWith("--")) {
      throw new Error(`missing value for ${key}`);
    }
    index += 1;
    if (key === "--video") args.video = value;
    else if (key === "--out") args.out = value;
    else if (key === "--clicks") args.clicks = value;
    else if (key === "--pdf-end") args.pdfEnds.push(...parseNumberList(value, key));
    else if (key === "--checkpoint") args.checkpoints.push(...parseNumberList(value, key));
    else if (key === "--every") args.every = positiveNumber(value, key);
    else if (key === "--pre-offset") args.preOffset = nonNegativeNumber(value, key);
    else if (key === "--post-offset") args.postOffset = nonNegativeNumber(value, key);
    else if (key === "--tile-cols") args.tileCols = positiveInteger(value, key);
    else throw new Error(`unknown option: ${key}`);
  }
  if (!args.video) throw new Error("--video is required");
  if (!args.out) throw new Error("--out is required");
  return args;
}

function parseNumberList(raw, key) {
  return raw.split(",").map((part) => nonNegativeNumber(part.trim(), key));
}

function positiveNumber(raw, key) {
  const value = Number(raw);
  if (!Number.isFinite(value) || value <= 0) {
    throw new Error(`${key} must be a positive number`);
  }
  return value;
}

function nonNegativeNumber(raw, key) {
  const value = Number(raw);
  if (!Number.isFinite(value) || value < 0) {
    throw new Error(`${key} must be a non-negative number`);
  }
  return value;
}

function positiveInteger(raw, key) {
  const value = Number(raw);
  if (!Number.isInteger(value) || value <= 0) {
    throw new Error(`${key} must be a positive integer`);
  }
  return value;
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

function ensureTool(command) {
  const result = spawnSync(command, ["-version"], { encoding: "utf8", stdio: "pipe" });
  if (result.error || result.status !== 0) {
    throw new Error(`${command} is required on PATH`);
  }
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function readClicks(filePath) {
  if (!filePath) return [];
  const payload = readJson(filePath);
  const rawClicks = Array.isArray(payload) ? payload : payload.clicks;
  if (!Array.isArray(rawClicks)) {
    throw new Error("--clicks must be a JSON array or object with a clicks array");
  }
  return rawClicks.map((click, index) => {
    const at = numberFrom(click, ["at", "time", "timestamp", "seconds"]);
    if (at === null || at < 0) {
      throw new Error(`click ${index + 1} has no valid timestamp`);
    }
    return {
      index: index + 1,
      at,
      x: numberFrom(click, ["x"]),
      y: numberFrom(click, ["y"]),
    };
  });
}

function numberFrom(object, keys) {
  if (!object || typeof object !== "object") return null;
  for (const key of keys) {
    const value = Number(object[key]);
    if (Number.isFinite(value)) return value;
  }
  return null;
}

function timestamp(seconds) {
  return Math.max(0, seconds).toFixed(3);
}

function safeLabel(label) {
  return label.replace(/[^a-zA-Z0-9._-]+/g, "-").replace(/^-+|-+$/g, "");
}

function extractFrame(video, outFile, seconds) {
  run("ffmpeg", [
    "-hide_banner",
    "-loglevel",
    "error",
    "-ss",
    timestamp(seconds),
    "-i",
    video,
    "-frames:v",
    "1",
    "-q:v",
    "2",
    outFile,
  ]);
}

function extractIntervalFrames(video, framesDir, everySeconds) {
  const pattern = path.join(framesDir, "interval-%04d.jpg");
  run("ffmpeg", [
    "-hide_banner",
    "-loglevel",
    "error",
    "-i",
    video,
    "-vf",
    `fps=1/${everySeconds}`,
    "-q:v",
    "2",
    pattern,
  ]);
}

function probeVideo(video) {
  const output = run("ffprobe", [
    "-v",
    "error",
    "-print_format",
    "json",
    "-show_format",
    "-show_streams",
    video,
  ]);
  return JSON.parse(output);
}

function makeContactSheet(framesDir, outFile, tileCols) {
  const frames = fs.readdirSync(framesDir).filter((file) => file.endsWith(".jpg")).sort();
  if (frames.length === 0) return null;
  const rows = Math.ceil(frames.length / tileCols);
  run("ffmpeg", [
    "-hide_banner",
    "-loglevel",
    "error",
    "-pattern_type",
    "glob",
    "-i",
    path.join(framesDir, "*.jpg"),
    "-vf",
    `scale=360:-1,tile=${tileCols}x${rows}:padding=8:margin=8`,
    "-frames:v",
    "1",
    outFile,
  ]);
  return outFile;
}

function writeSummary(outDir, summary) {
  const outFile = path.join(outDir, "qa-summary.json");
  fs.writeFileSync(outFile, `${JSON.stringify(summary, null, 2)}\n`, "utf8");
  return outFile;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  ensureTool("ffmpeg");
  ensureTool("ffprobe");

  const video = path.resolve(args.video);
  if (!fs.existsSync(video)) throw new Error(`video does not exist: ${video}`);

  const outDir = path.resolve(args.out);
  const framesDir = path.join(outDir, "frames");
  fs.mkdirSync(framesDir, { recursive: true });

  const extracted = [];
  const clicks = readClicks(args.clicks);
  for (const click of clicks) {
    const preFile = path.join(framesDir, `click-${String(click.index).padStart(3, "0")}-pre-${safeLabel(timestamp(click.at - args.preOffset))}.jpg`);
    const postFile = path.join(framesDir, `click-${String(click.index).padStart(3, "0")}-post-${safeLabel(timestamp(click.at + args.postOffset))}.jpg`);
    extractFrame(video, preFile, click.at - args.preOffset);
    extractFrame(video, postFile, click.at + args.postOffset);
    extracted.push({ kind: "click-pre", click: click.index, at: click.at - args.preOffset, file: preFile, x: click.x, y: click.y });
    extracted.push({ kind: "click-post", click: click.index, at: click.at + args.postOffset, file: postFile, x: click.x, y: click.y });
  }

  const checkpoints = [
    ...args.checkpoints.map((value) => ({ kind: "checkpoint", at: value })),
    ...args.pdfEnds.map((value) => ({ kind: "pdf-end", at: value })),
  ];
  checkpoints.forEach((checkpoint, index) => {
    const label = `${checkpoint.kind}-${String(index + 1).padStart(3, "0")}-${safeLabel(timestamp(checkpoint.at))}`;
    const file = path.join(framesDir, `${label}.jpg`);
    extractFrame(video, file, checkpoint.at);
    extracted.push({ ...checkpoint, file });
  });

  if (args.every !== null) {
    extractIntervalFrames(video, framesDir, args.every);
  }

  const contactSheet = makeContactSheet(framesDir, path.join(outDir, "contact-sheet.jpg"), args.tileCols);
  const summaryFile = writeSummary(outDir, {
    video,
    clicks: clicks.length,
    checkpoints: checkpoints.length,
    intervalEverySeconds: args.every,
    ffprobe: probeVideo(video),
    framesDir,
    extracted,
    contactSheet,
    manualChecklist: [
      "Pre-click frames show the highlight before the cursor arrives.",
      "Post-click frames show ripple or expected UI transition.",
      "Cursor position remains continuous after navigation.",
      "PDF or long-scroll end checkpoint is readable.",
      "No unwanted cookie banner, modal, or instructional text appears.",
      "Final resolution, FPS, codecs, and audio match the request.",
    ],
  });

  console.log(summaryFile);
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
