const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const dir = process.argv[2], out = process.argv[3];
const pages = ['shape-field','mannequin','iridescence-1-2','iridescence-3-6','color-check-prototypes','color-check-suite','vectorscope','phase-sliders','registration-scope'];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 1300 }, deviceScaleFactor: 1 });
  for (const n of pages) {
    await p.goto('file://' + dir + '/' + n + '.html');
    await p.waitForTimeout(2500);
    await p.screenshot({ path: out + '/' + n + '.png' });
    console.log(n);
  }
  await b.close();
})();
