#!/usr/bin/env node
"use strict";

const fs = require("node:fs");
const path = require("node:path");

function usage() {
  return [
    "Usage:",
    "  scaffold_tutorial_job.js --out tutorial-job.json [options]",
    "",
    "Options:",
    "  --url URL             Set startUrl.",
    "  --title TITLE         Set title.",
    "  --output-dir DIR      Set outputDir.",
    "  --fps N               Set FPS.",
    "  --width N             Set viewport width.",
    "  --height N            Set viewport height.",
  ].join("\n");
}

function parseArgs(argv) {
  const args = {};
  for (let index = 0; index < argv.length; index += 1) {
    const key = argv[index];
    const value = argv[index + 1];
    if (key === "--help" || key === "-h") {
      console.log(usage());
      process.exit(0);
    }
    if (!key.startsWith("--")) throw new Error(`unexpected argument: ${key}`);
    if (value === undefined || value.startsWith("--")) throw new Error(`missing value for ${key}`);
    index += 1;
    if (key === "--out") args.out = value;
    else if (key === "--url") args.url = value;
    else if (key === "--title") args.title = value;
    else if (key === "--output-dir") args.outputDir = value;
    else if (key === "--fps") args.fps = number(value, key);
    else if (key === "--width") args.width = number(value, key);
    else if (key === "--height") args.height = number(value, key);
    else throw new Error(`unknown option: ${key}`);
  }
  if (!args.out) throw new Error("--out is required");
  return args;
}

function number(raw, key) {
  const value = Number(raw);
  if (!Number.isInteger(value) || value <= 0) {
    throw new Error(`${key} must be a positive integer`);
  }
  return value;
}

function main() {
  const args = parseArgs(process.argv.slice(2));
  const templatePath = path.resolve(__dirname, "../templates/tutorial-job.json");
  const job = JSON.parse(fs.readFileSync(templatePath, "utf8"));
  if (args.url) job.startUrl = args.url;
  if (args.title) job.title = args.title;
  if (args.outputDir) job.outputDir = args.outputDir;
  if (args.fps) job.fps = args.fps;
  if (args.width) job.viewport.width = args.width;
  if (args.height) job.viewport.height = args.height;

  const outPath = path.resolve(args.out);
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, `${JSON.stringify(job, null, 2)}\n`, "utf8");
  console.log(outPath);
}

try {
  main();
} catch (error) {
  console.error(error.message);
  process.exit(1);
}
