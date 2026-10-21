"""Fill section 15 References with the external reference research
(images + credits + readings) from references/reference-sources.html."""
import base64, re, sys
SRC = '/mnt/project-files/references/reference-sources.html'
SITE = '/mnt/project-files/brand-merged/public/index.html'
src, site = open(SRC).read(), open(SITE).read()
names = ['thermal', 'film', 'bars', 'registration', 'vectorscope']
arts = re.findall(r'<article class="ref">(.*?)</article>', src, re.S)
assert len(arts) == 5, len(arts)
out = []
for name, a in zip(names, arts):
    m = re.search(r'src="data:image/(\w+);base64,([^"]+)"', a)
    ext = 'jpg' if m.group(1) == 'jpeg' else m.group(1)
    fn = f'img/ext-{name}.{ext}'
    open('/mnt/project-files/brand-merged/public/' + fn, 'wb').write(base64.b64decode(m.group(2)))
    a = a.replace(m.group(0), f'src="{fn}" loading="lazy"')
    a = re.sub(r'\s*<p class="gap">.*?</p>', '', a, flags=re.S)  # sourcing notes stay in the draft
    a = a.replace('<h2>', '<h3>').replace('</h2>', '</h3>')
    for c in ['plate', 'img contain', 'img', 'credit', 'lic', 'body', 'lab meta', 'why', 'reads', 'kind', 'cite', 't', 'n']:
        a = a.replace(f'class="{c}"', 'class="' + ' '.join(w if w == 'lab' else 'rf-' + w for w in c.split()) + '"')
    out.append('        <article class="rf">' + a.rstrip() + '\n        </article>')
html = '\n'.join(out)
old_grid = '<div class="vgrid" id="refgrid"></div>'
assert old_grid in site
site = site.replace(old_grid, '<div class="rfs">\n' + html + '\n      </div>')
site = site.replace('<p class="sub">What the system is measured against: instruments that use color as a reading. Each one informed a study above.</p>',
  '<p class="sub">What the system is measured against: instruments that use color as a reading. Each one informed a study above. Images are by outside authors under the licences shown; each comes with readings written for a general reader.</p>')
# drop the old generated grid
s = site.index('      // references (15)'); e = site.index('      // the field (12)')
site = site[:s] + site[e:]
css = '''
  /* references (15): external images, credits, readings */
  .rfs { display:flex; flex-direction:column; border-top:var(--hairline) solid var(--line); margin-top:var(--sp-5); }
  .rf { display:grid; grid-template-columns:minmax(0,5fr) minmax(0,7fr); gap:28px; padding:28px 0; border-bottom:var(--hairline) solid var(--line); }
  .rf-plate { display:flex; flex-direction:column; gap:var(--sp-2); min-width:0; }
  .rf-img { aspect-ratio:4/3; background:var(--plate); border:var(--hairline) solid var(--line); border-radius:var(--r-xs); overflow:hidden; display:grid; place-items:center; }
  .rf-img img { width:100%; height:100%; object-fit:cover; display:block; }
  .rf-img.rf-contain img { object-fit:contain; }
  .rf-credit { font-size:12px; color:var(--text-3); line-height:1.45; }
  .rf-credit a { color:var(--text-3); }
  .rf-lic { display:inline-block; padding:1px 6px; border:var(--hairline) solid var(--line); border-radius:var(--r-xs); font-size:11px; letter-spacing:.04em; color:var(--text-2); margin-right:6px; }
  .rf-body { display:flex; flex-direction:column; gap:var(--sp-4); min-width:0; }
  .rf-body h3 { margin:0; font-weight:400; font-size:22px; letter-spacing:-0.015em; color:var(--text); }
  .rf-meta { margin-top:-8px; }
  .rf-why { margin:0; max-width:60ch; color:var(--text-2); font-size:15px; line-height:1.5; }
  .rf-reads { list-style:none; margin:0; padding:0; display:flex; flex-direction:column; border-top:var(--hairline) solid var(--line); }
  .rf-reads li { display:grid; grid-template-columns:118px minmax(0,1fr); gap:var(--sp-3); padding:var(--sp-3) 0; border-bottom:var(--hairline) solid var(--line); }
  .rf-kind { font-size:11px; letter-spacing:.06em; text-transform:uppercase; color:var(--text-3); padding-top:3px; }
  .rf-cite { color:var(--text-2); font-size:14px; line-height:1.45; }
  .rf-cite .rf-t { color:var(--text); }
  .rf-cite .rf-n { display:block; margin-top:4px; font-size:13px; color:var(--text-3); }
  @media (max-width:760px) { .rf { grid-template-columns:1fr; gap:18px; } .rf-reads li { grid-template-columns:1fr; gap:2px; } }
'''
anchor = '  .vgrid { display:grid;'
site = site.replace(anchor, css.lstrip('\n') + anchor, 1)
open(SITE, 'w').write(site)
print('ok', site.count('class="rf"'))
