# Playwright + ffmpeg Tutorial Video Pattern

Use this as the implementation checklist for polished browser tutorial videos.

## Recorder Structure

Prefer one Node script with a config object for variants:

```js
const LANGUAGE_CONFIGS = {
  en: {
    homeUrl: "https://www.example.com/",
    newsPath: "/news/",
    newsText: /NEWS/i,
    articleText: /Target article title/,
    countryHeading: "Ukraine",
    locale: "en-US",
  },
};
const LANG_CODE = (process.argv[2] || "en").toLowerCase();
const LANGUAGE = LANGUAGE_CONFIGS[LANG_CODE];
```

Keep raw frames, generated frame sequence, PDFs, timelines, and Chrome profile
in a per-variant output directory. Put final MP4s at stable paths such as
`out/tutorial-en.mp4`.

## Browser Setup

Use persistent Chrome when a site is sensitive to automation:

```js
const context = await chromium.launchPersistentContext(PROFILE_DIR, {
  channel: "chrome",
  headless: true,
  args: [
    `--window-size=${VIEWPORT.width},${VIEWPORT.height}`,
    "--no-first-run",
    "--disable-session-crashed-bubble",
    "--disable-background-timer-throttling",
    "--disable-renderer-backgrounding",
    "--force-color-profile=srgb",
  ],
  viewport: VIEWPORT,
  deviceScaleFactor: 1,
  locale: LANGUAGE.locale,
  userAgent: USER_AGENT,
  acceptDownloads: true,
});
```

Inject cookie-hiding CSS with `context.addInitScript`, seed consent cookies when
practical, and still keep a `dismissCookieBanner(page)` fallback.

Apply page zoom by injecting CSS that excludes the overlay:

```css
body > :not(#demo-overlay-root) {
  zoom: 1.5 !important;
}
```

## Overlay Behavior

The overlay should be a fixed top-level element:

- `html, body, * { cursor: none !important; }`
- `#demo-overlay-root { position: fixed; inset: 0; pointer-events: none; z-index: 2147483647; }`
- `.demo-highlight` with yellow border, glow, and light background.
- `.demo-cursor` with a large SVG cursor and drop shadow.
- `.demo-ripple` centered at click coordinates.

Keep cursor state outside the page:

```js
let cursorPosition = { x: 120, y: 120 };
```

After every navigation or modal/page reload, reinstall the overlay and set the
cursor to `cursorPosition`. This prevents top-left cursor teleports.

Click order matters:

```js
async function clickLocator(page, locator, fallback) {
  const point = await centerOf(locator, fallback);
  await highlightLocator(page, locator);
  await page.waitForTimeout(420);
  await animateCursor(page, point, 650);
  cursorPosition = point;
  await page.waitForTimeout(260);
  clicks.push({
    at: (Date.now() - startedAt) / 1000,
    x: Math.round(point.x),
    y: Math.round(point.y),
  });
  await page.evaluate((position) => window.__demoOverlay.click(position.x, position.y), point);
  await page.mouse.click(point.x, point.y, { delay: 70 });
  await page.waitForTimeout(220);
}
```

The highlight must appear before cursor motion starts.

## Capture Strategy

Use CDP screencast for normal browsing:

```js
await client.send("Page.startScreencast", {
  format: "jpeg",
  quality: 100,
  maxWidth: VIDEO_SIZE.width,
  maxHeight: VIDEO_SIZE.height,
  everyNthFrame: 1,
});
```

Store each frame with a timestamp from `startedAt`, acknowledge each screencast
frame, then build a constant-FPS image sequence by linking or copying the
nearest captured source frame for each target time.

For PDF scrolls, if browser capture is choppy:

1. Download the PDF.
2. Create a local viewer HTML with an iframe:
   ```html
   <iframe src="file:///path/to/file.pdf#toolbar=1&navpanes=0&zoom=150"></iframe>
   ```
3. Stop the screencast after the PDF page is ready.
4. Scroll with small wheel deltas and capture manual screenshots at `VIDEO_FPS`.

## Click Audio

Decode the user-provided MP3 with ffmpeg:

```js
const { stdout } = await execFileAsync("ffmpeg", [
  "-v", "error",
  "-i", CLICK_SOUND_PATH,
  "-ac", "1",
  "-ar", "48000",
  "-f", "f32le",
  "-",
], { encoding: "buffer", maxBuffer: 20 * 1024 * 1024 });
```

Convert the float32 stream into samples, mix it at each logged click timestamp,
normalize if peak exceeds about `0.92`, write a mono 48 kHz WAV, then pass that
WAV to the final ffmpeg render.

## Final Render

Use a high-quality H.264/AAC render:

```bash
ffmpeg -y -framerate 60 -i frame-%06d.jpg -i click-track.wav \
  -vf "scale=in_range=pc:out_range=tv,setsar=1,format=yuv420p" \
  -c:v libx264 -crf 10 -preset slow -profile:v high -pix_fmt yuv420p \
  -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 192k -r 60 -movflags +faststart -shortest out.mp4
```

## Verification Commands

Run syntax check:

```bash
node --check scripts/record-*.js
```

Inspect final MP4:

```bash
ffprobe -v error \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,pix_fmt,sample_rate,channels \
  -show_entries format=duration,size \
  -of json out/final.mp4
```

Read click timeline:

```bash
cat out/<variant>/clicks.json
```

Extract QA frames:

```bash
ffmpeg -y -loglevel error -ss <click_time_minus_1s> -i out/final.mp4 -frames:v 1 out/checks/preclick.png
ffmpeg -y -loglevel error -ss <pdf_end_time> -i out/final.mp4 -frames:v 1 out/checks/pdf-end.png
```

Then use image viewing or browser screenshots to confirm:

- no unwanted text labels;
- target highlight appears before the cursor arrives;
- cursor does not teleport after navigation;
- click ripple appears on targets;
- PDF is zoomed as requested and reaches the intended final position;
- final dimensions, FPS, and audio match the request.
