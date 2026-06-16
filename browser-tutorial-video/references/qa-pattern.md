# Browser Tutorial Video QA Pattern

Use this after rendering the final MP4 and before claiming the recording is
ready.

## QA Script

Run the bundled helper when there is a click timeline, long-scroll checkpoint,
or PDF ending to verify:

- target highlight appears before the cursor arrives;
- click ripple appears around the click moment;
- cursor does not teleport after navigation;
- PDF or long scroll reaches the intended final position;
- final metadata matches the requested resolution, FPS, and audio expectations.

```bash
node /path/to/browser-tutorial-video/scripts/tutorial_video_qa.js \
  --video out/tutorial-en.mp4 \
  --clicks out/en/clicks.json \
  --out out/en/qa \
  --every 10 \
  --pdf-end 82.5
```

The script writes:

- `frames/*.jpg` for pre-click, post-click, interval, and checkpoint frames;
- `contact-sheet.jpg` for fast visual review;
- `qa-summary.json` with ffprobe metadata, extracted frame paths, and checklist
  items.

## Expected Click Timeline Shape

The helper accepts either a raw array:

```json
[
  { "at": 4.25, "x": 1400, "y": 720 }
]
```

or an object with a `clicks` array:

```json
{
  "clickSoundPath": "click.mp3",
  "clicks": [
    { "at": 4.25, "x": 1400, "y": 720 }
  ]
}
```

Fields named `time`, `timestamp`, `seconds`, `x`, and `y` are tolerated when
present.

## Manual Review Checklist

Open the contact sheet and inspect:

- first frame has no cookie banner or unwanted modal;
- each pre-click frame already shows the target highlight;
- each post-click frame shows the ripple or resulting UI transition;
- cursor position is continuous after navigation;
- zoom level is correct;
- PDF or long-scroll ending is visible and readable;
- no text overlays appear when the user asked for a clean recording;
- final video is not blurry, flickery, or frame-starved.

If any item fails, rerender or report the exact limitation. Do not claim the
video is ready based only on `ffprobe`.

## Optional Pixel Comparison

For stricter checks, add `pixelmatch` in the project using the recorder and
compare expected reference frames against extracted QA frames. Keep this
project-local unless the recorder has stable reference images; generic skills
should not ship brittle pixel baselines.
