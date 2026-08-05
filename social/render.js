// Renders social graphics to PNG at exact pixel dimensions.
// Usage: node build-room-visuals/social/render.js
const { chromium } = require('playwright');
const path = require('path');

const jobs = [
  { file: 'ig-thesis-post.html', out: 'ig-thesis-post.png', w: 1080, h: 1350 },
];

(async () => {
  const browser = await chromium.launch();
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 2 });
    await page.goto('file://' + path.join(__dirname, j.file));
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(__dirname, j.out) });
    console.log('rendered', j.out);
    await page.close();
  }
  await browser.close();
})();
