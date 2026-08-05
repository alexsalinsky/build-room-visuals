// Renders the Jul 10 + Jul 14 accent cards. Pattern copied from build-room-visuals/events/render.js.
// Usage: node build-room-visuals/exports/render-2026-07-04-cards.js
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();

  // Step 1: screenshot the Wins Wall (grid view, filter All) for the framed card.
  // Served locally (same source as the live GitHub Pages site, with the Majo spelling fix)
  // because wins-wall.html fetches proof-library.json, which file:// blocks.
  const { spawn } = require('child_process');
  const server = spawn('python', ['-m', 'http.server', '8765'], { cwd: path.join(__dirname, '..') });
  await new Promise(r => setTimeout(r, 1200));
  const wall = await browser.newPage({ viewport: { width: 1240, height: 1260 }, deviceScaleFactor: 2 });
  await wall.goto('http://localhost:8765/wins-wall.html', { waitUntil: 'networkidle' });
  await wall.waitForTimeout(1500);
  // Clip below the page's own pill so the frame pill isn't duplicated. 1240x1140 matches the frame inset aspect.
  await wall.screenshot({ path: path.join(__dirname, 'wins-wall-shot-raw.png'), clip: { x: 0, y: 60, width: 1240, height: 1140 } });
  console.log('captured wins-wall-shot-raw.png 1240x1140 @2x');
  await wall.close();
  server.kill();

  // Step 2: render the cards.
  const jobs = [
    { file: '2026-07-10-brand-card-src.html', out: '2026-07-10-brand-card.png', w: 1200, h: 1200 },
    { file: '2026-07-14-countdown-card-src.html', out: '2026-07-14-countdown-card.png', w: 1200, h: 1200 },
    { file: '2026-07-14-wins-wall-framed-src.html', out: '2026-07-14-wins-wall-framed.png', w: 1200, h: 1200 },
  ];
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 2 });
    await page.goto('file://' + path.join(__dirname, j.file));
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(__dirname, j.out) });
    console.log('rendered', j.out, `${j.w}x${j.h} @2x`);
    await page.close();
  }
  await browser.close();
})();
