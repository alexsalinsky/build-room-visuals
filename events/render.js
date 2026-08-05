// Renders the event graphics to PNG at exact pixel dimensions.
// Usage: node build-room-visuals/events/render.js
const { chromium } = require('playwright');
const path = require('path');

const jobs = [
  { file: 'upcoming-events-ig.html', out: 'upcoming-events-ig-1080x1350.png', w: 1080, h: 1350 },
  { file: 'upcoming-events-linkedin.html', out: 'upcoming-events-linkedin-1200x627.png', w: 1200, h: 627 },
];

(async () => {
  const browser = await chromium.launch();
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
