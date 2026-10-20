# Light and dark mode, like safx-research.pages.dev: follows the system, sidebar toggle overrides and is remembered.
import sys
p = 'public/index.html'; s = open(p).read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: sys.exit(f'mismatch ({s.count(a)}): ' + a[:70])
    s = s.replace(a, b)
rep('<meta name="color-scheme" content="dark" />', '<meta name="color-scheme" content="dark light" />\n<script>try{var t=localStorage.getItem("safx-rnd-theme");if(t)document.documentElement.dataset.theme=t}catch(e){}</script>')
rep("    --ctl-wash:rgba(244,241,234,.05);\n  }\n", """    --ctl-wash:rgba(244,241,234,.05);
    --plate:#0b0b0b;
    --scale-grey:linear-gradient(180deg,#555,#111);
    color-scheme:dark;
  }
  /* Light mode: the same system on linen. Ink becomes the text; brand surface values
     in the swatches and tokens stay literal. */
  @media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) {
    --bg:#fcfaf5; --panel:#f4f1ea; --line:#dedad0; --border-2:#c4bfb3; --text:#0e0e0e;
    --text-2:#3e3e3e; --text-3:#5c5c5c; --text-4:#6a6a6a; --err:#b3412f; --err-edge:#ebcfc9;
    --ctl-wash:rgba(14,14,14,.05); --plate:#f4f1ea; --scale-grey:linear-gradient(180deg,#b8b8b8,#f4f1ea);
    color-scheme:light; } }
  :root[data-theme="light"] {
    --bg:#fcfaf5; --panel:#f4f1ea; --line:#dedad0; --border-2:#c4bfb3; --text:#0e0e0e;
    --text-2:#3e3e3e; --text-3:#5c5c5c; --text-4:#6a6a6a; --err:#b3412f; --err-edge:#ebcfc9;
    --ctl-wash:rgba(14,14,14,.05); --plate:#f4f1ea; --scale-grey:linear-gradient(180deg,#b8b8b8,#f4f1ea);
    color-scheme:light; }
""")
rep('body { background:var(--ink);', 'body { background:var(--bg);')
rep('flex-direction:column; gap:18px; background:var(--ink);', 'flex-direction:column; gap:18px; background:var(--bg);')
rep('background:var(--ink); color:var(--text); }', 'background:var(--bg); color:var(--text); }')
rep('accent-color:var(--paper);', 'accent-color:var(--text);')
rep('.fieldplate { position:relative; background:#0b0b0b;', '.fieldplate { position:relative; background:var(--plate);')
rep('.vcard .img { aspect-ratio:4/3; background:#0b0b0b;', '.vcard .img { aspect-ratio:4/3; background:var(--plate);')
rep('.scalebar i.grey { background:linear-gradient(180deg,#555,#111); }', '.scalebar i.grey { background:var(--scale-grey); }')
for v, h in [('ink', '#0E0E0E'), ('paper', '#F4F1EA'), ('linen', '#FCFAF5'), ('panel', '#171717'), ('line', '#242424')]:
    rep(f'<div class="chip" style="background:var(--{v})"></div>', f'<div class="chip" style="background:{h}"></div>')
rep('  .acts { margin-top:auto; display:flex; gap:var(--sp-1); }',
    '  .theme { margin-top:auto; display:inline-flex; align-items:center; gap:8px; background:none; border:0; padding:0; cursor:pointer; font-family:var(--sans); font-size:11px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-3); transition:color var(--dur) var(--ease); }\n  .theme:hover { color:var(--text); }\n  .theme i { width:8px; height:8px; border-radius:50%; border:1px solid currentColor; background:var(--text); }\n  .acts { display:flex; gap:var(--sp-1); }')
rep('    <div class="acts">\n      <button class="btn" id="printBtn"', '    <button class="theme" id="theme" type="button"><i></i><span>Dark mode</span></button>\n    <div class="acts">\n      <button class="btn" id="printBtn"')
rep("    document.getElementById('printBtn').addEventListener('click', () => window.print());",
"""    document.getElementById('printBtn').addEventListener('click', () => window.print());
    // Theme: system by default; the toggle overrides and is remembered. Marks swap to their black files on light.
    (() => {
      const root = document.documentElement, tb = document.getElementById('theme');
      const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : !matchMedia('(prefers-color-scheme: light)').matches;
      const sync = () => {
        const d = isDark(); tb.lastElementChild.textContent = d ? 'Dark mode' : 'Light mode';
        document.querySelectorAll('img[src*="assets/marks/"]').forEach((im) => { const src = im.getAttribute('src'), n = d ? src.replace('-black.', '-white.') : src.replace('-white.', '-black.'); if (n !== src) im.setAttribute('src', n); });
        dispatchEvent(new Event('resize'));
      };
      tb.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; try { localStorage.setItem('safx-rnd-theme', root.dataset.theme); } catch (e) {} sync(); });
      matchMedia('(prefers-color-scheme: light)').addEventListener('change', sync);
      sync();
    })();""")
# field: tones and ground follow the theme
rep("TONES = ['', '#5e5e5e', '#8f8f8f', '#b4b4b4', '#F4F1EA'];", "TONES_D = ['', '#5e5e5e', '#8f8f8f', '#b4b4b4', '#F4F1EA'], TONES_L = ['', '#b4b0a6', '#85827a', '#4e4c47', '#0E0E0E'];\n      let TONES = TONES_D;")
rep("ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.fillStyle = '#0b0b0b';", "ctx.setTransform(dpr, 0, 0, dpr, 0, 0); TONES = getComputedStyle(document.documentElement).colorScheme === 'light' ? TONES_L : TONES_D; ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--plate').trim() || '#0b0b0b';")
open(p, 'w').write(s); print('ok')
