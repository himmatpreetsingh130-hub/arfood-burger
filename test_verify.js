const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 390, height: 844 }); // iPhone size

  const fileUrl = 'file://' + path.resolve('pump.html');
  await page.goto(fileUrl);
  await page.waitForTimeout(500);

  // Take home screenshot
  await page.screenshot({ path: '/home/jules/verification/01_home.png' });

  // Click ONLINE MATCH button
  await page.click('#onlineMatchBtn');
  await page.waitForTimeout(300);
  await page.screenshot({ path: '/home/jules/verification/02_match_mode_modal.png' });

  // Click JOIN ROOM -> opens PIN pad modal
  await page.click('button:has-text("JOIN ROOM")');
  await page.waitForTimeout(300);
  await page.screenshot({ path: '/home/jules/verification/03_pin_pad_modal.png' });

  // Close pin modal
  await page.click('.pin-modal-close');
  await page.waitForTimeout(300);

  // Click ONLINE MATCH again, then CREATE ROOM
  await page.click('#onlineMatchBtn');
  await page.waitForTimeout(300);
  await page.click('button:has-text("CREATE ROOM")');
  await page.waitForTimeout(300);

  // Now on Choose Exercise
  await page.screenshot({ path: '/home/jules/verification/04_exercise_select.png' });

  // Select Pushup
  await page.click('.exercise-card[data-ex="pushup"]');
  await page.waitForTimeout(300);

  // Now on Duration Select
  await page.screenshot({ path: '/home/jules/verification/05_duration_select.png' });

  await browser.close();
  console.log('Verification screenshots captured!');
})();
