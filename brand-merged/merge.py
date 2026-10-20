#!/usr/bin/env python3
"""Merge the Studio Artifice brand page (base, wins on conflict) with the R&D research page.

Base: renaise/studio-artifice-brand @ safx-brand-page index.html (= Figma frame 2043:2).
Added: research from safx-research.pages.dev (Figma frame 2166:713), marked "R&D".
Writes public/index.html. Study pages live in public/pages/ on the safx-rnd stage.
"""
import pathlib, sys

HERE = pathlib.Path(__file__).parent
s = (HERE / "base.html").read_text()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"expected {count} of: {old[:70]!r}, found {n}")
    s = s.replace(old, new)


# ---------- head ----------
rep("""  Studio Artifice Brand
  Repo:""", """  Studio Artifice Brand, merged with the R&D (2026-10-20)
  Base: this page as built from the Figma "Brand Page" (frame 2043:2). Base copy wins on any conflict.
  Added: the R&D research (safx-research.pages.dev, Figma frame 2166:713), each block tagged "R&D".
  Served first from the safx-rnd Worker, where /pages/ holds the live studies and rnd.html the old index.
  Repo:""")
rep("""<title>Studio Artifice Brand</title>""", """<title>Studio Artifice Brand</title>
<meta name="color-scheme" content="dark" />""")

CSS = r"""
  /* ================= R&D additions (2026-10-20) =================
     Same vocabulary as the base: 1px lines, 2px radius, 11px labels, one ease. */
  :root {
    --strategy:#D2FF1E; --identity:#FF1BD1; --application:#00EBEF; --production:#0009FF;
    --register:#9A9A9A;
    --film:linear-gradient(90deg,#000000 0.0%,#020203 0.2%,#4D505F 2.2%,#9395A9 4.6%,#C7C3CF 7.1%,#E6D7CE 9.6%,#F0D3AD 11.8%,#EABC70 13.9%,#D8960E 15.8%,#BC6504 17.5%,#A43C4D 18.6%,#880075 19.6%,#4E00A5 21.2%,#3324B1 21.7%,#003CBB 22.2%,#0091D6 24.8%,#72C5C4 27.5%,#9FD4AA 28.9%,#CCD973 30.8%,#EFCB07 33.0%,#FDAA30 35.0%,#F67088 37.3%,#CF18BF 39.8%,#8C3BD1 42.0%,#6757D1 42.8%,#0075CB 43.8%,#00B89A 46.8%,#53D352 49.7%,#B5CE50 52.0%,#EFB08C 54.6%,#FF7DB9 57.3%,#F154C4 59.8%,#BE63B3 62.3%,#88829B 64.0%,#57958A 65.1%,#03A37D 66.0%,#00BE70 68.6%,#6EC391 71.6%,#C1B1AE 74.4%,#E598B5 76.8%,#EF82AB 79.0%,#E77999 81.1%,#CE8089 83.2%,#8B9E8C 86.8%,#5BB1A2 89.9%,#88B3AA 93.9%,#D6938F 100.0%);
  }
  .toc .rule-r { height:0; border-top:var(--hairline) solid var(--border-2); margin:10px 0 0; }
  .toc .grp { font-size:11px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-4); padding:12px 0 6px; border-bottom:var(--hairline) solid var(--line); }
  .rnd { display:inline-flex; align-items:center; min-height:20px; padding:0 7px; margin-left:8px; vertical-align:2px;
         font-size:10.5px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-2);
         border:var(--hairline) solid var(--border-2); border-radius:var(--r-xs); font-weight:400; }
  .rndbox { border-left:var(--hairline) solid var(--border-2); padding-left:var(--sp-4); margin-top:var(--sp-6); }
  .rndbox > .sh:first-child { margin-top:0; }
  .rndbox .sh { margin-top:var(--sp-6); }
  .rndbox .sh + * { margin-top:var(--sp-4); }
  .rulequote { font-size:clamp(17px,1.9vw,21px); line-height:1.35; color:var(--text); letter-spacing:var(--tr-display);
               max-width:40ch; border-left:2px solid var(--text); padding-left:var(--sp-4); margin-top:var(--sp-5); }
  .legend4 { display:inline-grid; grid-template-columns:repeat(4,22px); height:14px; border:1px solid var(--register); vertical-align:middle; }
  .legend4 i { border-left:1px solid var(--register); }
  .legend4 i:first-child { border-left:0; }

  .tbl { overflow-x:auto; margin-top:var(--sp-4); }
  .tbl table { border-collapse:collapse; width:100%; min-width:560px; font-size:13px; }
  .tbl th { font-weight:400; text-align:left; font-size:11px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-3);
            padding:var(--sp-2) var(--sp-4) var(--sp-2) 0; border-bottom:var(--hairline) solid var(--border-2); }
  .tbl td { padding:var(--sp-2) var(--sp-4) var(--sp-2) 0; border-bottom:var(--hairline) solid var(--line); vertical-align:top; color:var(--text-2); line-height:1.45; }
  .tbl td:first-child { color:var(--text); }
  .num { font-variant-numeric:tabular-nums; }
  .sw11 { display:inline-block; width:11px; height:11px; vertical-align:-1px; margin-right:8px; border:1px solid var(--register); }

  .phases { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:var(--sp-4); margin-top:var(--sp-4); }
  .phase .chip { height:120px; border:var(--hairline) solid var(--line); }
  .phase .nm { font-size:15px; color:var(--text); margin-top:var(--sp-3); }
  .phase .rl { font-size:12.5px; color:var(--text-3); margin-top:var(--sp-1); line-height:1.45; font-variant-numeric:tabular-nums; }
  .orders { display:grid; grid-template-columns:max-content minmax(0,1fr); gap:var(--sp-4) var(--sp-5); align-items:center; margin-top:var(--sp-4); }
  .orders .legend4 { grid-template-columns:repeat(4,30px); height:18px; }
  .orders .t { font-size:13.5px; color:var(--text-2); line-height:1.45; }
  .orders .t b { font-weight:400; color:var(--text); display:block; }

  .greys { display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); gap:var(--sp-3); margin-top:var(--sp-4); }
  .grey .chip { height:48px; border:var(--hairline) solid var(--line); }
  .grey .k { font-size:11px; color:var(--text-3); margin-top:var(--sp-1); }
  .grey .v { font-size:11.5px; color:var(--text); font-variant-numeric:tabular-nums; }
  .pluge { display:grid; grid-template-columns:repeat(3,1fr); height:90px; border:var(--hairline) solid var(--line); margin-top:var(--sp-4); max-width:520px; }
  .pluge div { display:flex; align-items:flex-end; padding:8px 10px; font-size:11px; color:#8a8a8a; }

  .matrix { display:grid; grid-template-columns:84px repeat(5,minmax(0,1fr)); border:var(--hairline) solid var(--line); background:var(--panel); margin-top:var(--sp-4); }
  .matrix > div { border-right:var(--hairline) solid var(--line); border-bottom:var(--hairline) solid var(--line); padding:12px 8px;
                  display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px; text-align:center; min-width:0; }
  .matrix > div:nth-child(6n) { border-right:0; }
  .matrix > div:nth-last-child(-n+6) { border-bottom:0; }
  .matrix .h { font-size:11px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-3); }
  .matrix .rh { align-items:flex-start; }
  .matrix svg { width:48px; height:48px; color:var(--text); }
  .matrix .n { font-size:12.5px; color:var(--text); }
  .matrix .c { font-size:11px; color:var(--text-3); font-variant-numeric:tabular-nums; }
  .cov { display:block; width:100%; max-width:100px; height:5px; background:repeating-linear-gradient(to right,var(--border-2) 0 1px,transparent 1px 4px); position:relative; }
  .cov i { position:absolute; inset:0 auto 0 0; background:var(--text-2); }

  .fieldwrap { display:grid; grid-template-columns:minmax(0,1fr) 200px; gap:var(--sp-4); margin-top:var(--sp-5); }
  .fieldplate { position:relative; background:#0b0b0b; border:var(--hairline) solid var(--line); aspect-ratio:16/10; touch-action:none; cursor:crosshair; overflow:hidden; }
  .fieldplate canvas { position:absolute; inset:0; width:100%; height:100%; display:block; }
  .fieldplate .hint { position:absolute; left:12px; top:10px; font-size:11px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-4); pointer-events:none; }
  .scale { border:var(--hairline) solid var(--line); background:var(--panel); padding:var(--sp-4); display:flex; flex-direction:column; gap:var(--sp-2); font-size:12px; }
  .scalebar { display:grid; grid-template-rows:repeat(4,1fr) 2.2fr; height:200px; border:1px solid var(--register); }
  .scalebar i { border-top:1px solid var(--register); }
  .scalebar i:first-child { border-top:0; }
  .scalebar i.grey { background:linear-gradient(180deg,#555,#111); }
  .scalekey { display:grid; gap:3px; color:var(--text-2); font-variant-numeric:tabular-nums; }
  .scalekey span { display:flex; justify-content:space-between; }
  .scale input { width:100%; accent-color:var(--paper); }
  .film { position:relative; height:48px; border:var(--hairline) solid var(--line); background:var(--film); margin-top:var(--sp-4); }
  .film .mk { position:absolute; top:-5px; bottom:-5px; width:1px; background:var(--text); }
  .film .mk span { position:absolute; top:calc(100% + 6px); left:50%; transform:translateX(-50%); font-size:11px; white-space:nowrap; color:var(--text-2); display:flex; align-items:center; gap:4px; font-variant-numeric:tabular-nums; }
  .film .mk span i { width:8px; height:8px; border:1px solid var(--register); }
  .filmaxis { display:flex; justify-content:space-between; font-size:11px; color:var(--text-3); margin-top:30px; font-variant-numeric:tabular-nums; }

  .vgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); gap:var(--sp-4); margin-top:var(--sp-4); }
  .vcard { border:var(--hairline) solid var(--line); background:var(--panel); text-decoration:none; display:flex; flex-direction:column;
           transition:border-color var(--dur) var(--ease); }
  a.vcard:hover { border-color:var(--text-3); }
  .vcard .img { aspect-ratio:4/3; background:#0b0b0b; overflow:hidden; display:grid; place-items:center; border-bottom:var(--hairline) solid var(--line); }
  .vcard .img img { width:100%; height:100%; object-fit:cover; display:block; }
  .vcard .img.paper { background:#f6f6f6; }
  .vcard .img.paper img { object-fit:contain; width:84%; height:auto; }
  .vcard .img svg { width:72%; height:72%; }
  .vcard .t { font-size:14px; color:var(--text); margin:var(--sp-3) var(--sp-3) 4px; line-height:1.3; }
  .vcard .m { font-size:11px; letter-spacing:var(--tr-label); text-transform:uppercase; color:var(--text-3); margin:0 var(--sp-3) var(--sp-1); }
  .vcard .d { font-size:12.5px; color:var(--text-3); margin:0 var(--sp-3) var(--sp-4); line-height:1.45; }
  .grouph { margin-top:var(--sp-6); }

  .tgroup { font-size:13px; color:var(--text); margin-top:var(--sp-5); }
  .tgroupn { font-size:12.5px; color:var(--text-3); margin-top:4px; }
  .tgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(140px,1fr)); gap:var(--sp-2); margin-top:var(--sp-2); align-items:start; }
  .tcard { display:flex; flex-direction:column; text-align:left; background:var(--panel); border:var(--hairline) solid var(--line); border-radius:var(--r-xs);
           cursor:pointer; padding:0 0 var(--sp-3); min-height:124px; font-family:var(--sans); transition:border-color var(--dur) var(--ease); }
  .tcard:hover { border-color:var(--text-3); }
  .tsw { display:block; height:52px; border-bottom:var(--hairline) solid var(--line); }
  .tsw.glyph, .tsw.type { display:flex; align-items:center; justify-content:center; background:var(--ink); color:var(--text); }
  .tsw.glyph svg { width:30px; height:30px; }
  .tsw.type { font-size:24px; }
  .tbody { display:flex; flex-direction:column; gap:3px; padding:var(--sp-2) var(--sp-3) 0; }
  .tnm { font-size:12px; color:var(--text); line-height:1.3; }
  .tkv { font-size:11px; color:var(--text-3); overflow-wrap:anywhere; }
  .thx { font-size:11px; color:var(--text-2); font-variant-numeric:tabular-nums; overflow-wrap:anywhere; }
  .tcard.copied .thx::after { content:" · copied"; color:var(--text); }

  @media (max-width:900px) {
    .fieldwrap { grid-template-columns:1fr; }
    .scalebar { height:110px; }
    .greys { grid-template-columns:repeat(3,minmax(0,1fr)); }
  }
  @media (max-width:680px) {
    .phases { grid-template-columns:repeat(2,minmax(0,1fr)); }
    .orders { grid-template-columns:1fr; gap:6px 0; }
    .orders .t { margin-bottom:var(--sp-3); }
    .matrix { grid-template-columns:56px repeat(5,minmax(0,1fr)); }
    .matrix svg { width:30px; height:30px; }
    .matrix .n { font-size:10.5px; }
    .rndbox { padding-left:var(--sp-3); }
  }
"""
rep("""  @media (max-width:900px) {
    .app { flex-direction:column; }""", CSS + """
  @media (max-width:900px) {
    .app { flex-direction:column; }""")

# ---------- glyph defs, right after <body> ----------
DEFS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <path id="g-square" d="M-0.5 -0.5L0.5 -0.5L0.5 0.5L-0.5 0.5L-0.5 -0.5Z"/>
  <path id="g-screw" fill-rule="evenodd" d="M0 -0.5C0.27614 -0.5 0.5 -0.27614 0.5 0C0.5 0.27614 0.27614 0.5 0 0.5C-0.27614 0.5 -0.5 0.27614 -0.5 0C-0.5 -0.27614 -0.27614 -0.5 0 -0.5ZM-0.03857 -0.26667L-0.03857 -0.03857L-0.26667 -0.03857L-0.26667 0.03857L-0.03857 0.03857L-0.03857 0.26667L0.03857 0.26667L0.03857 0.03857L0.26667 0.03857L0.26667 -0.03857L0.03857 -0.03857L0.03857 -0.26667L-0.03857 -0.26667Z"/>
  <path id="g-cross" d="M-0.07231 -0.5L0.07231 -0.5L0.07231 -0.07231L0.5 -0.07231L0.5 0.07231L0.07231 0.07231L0.07231 0.5L-0.07231 0.5L-0.07231 0.07231L-0.5 0.07231L-0.5 -0.07231L-0.07231 -0.07231L-0.07231 -0.5Z"/>
  <path id="g-mono" fill-rule="evenodd" d="M-0.00001 -0.5C0.27614 -0.5 0.5 -0.27615 0.5 -0.00001L0.49984 0.0129C0.493 0.28308 0.27182 0.5 -0.00001 0.5L-0.0129 0.49984C-0.28308 0.493 -0.5 0.27182 -0.5 -0.00001C-0.5 -0.27614 -0.27614 -0.5 -0.00001 -0.5ZM-0.00001 -0.43228C-0.23874 -0.43227 -0.43227 -0.23874 -0.43228 -0.00001C-0.43228 0.23873 -0.23874 0.43227 -0.00001 0.43228C0.23873 0.43228 0.43228 0.23873 0.43228 -0.00001C0.43227 -0.23874 0.23873 -0.43228 -0.00001 -0.43228ZM0.24338 0.22766L0.17857 0.22766L0.11813 0.07691L-0.11781 0.07691L-0.17753 0.22766L-0.24161 0.22766L-0.03479 -0.29083L0.03365 -0.29083L0.24338 0.22766ZM-0.0013 -0.22457C-0.03188 -0.14301 -0.06271 -0.06291 -0.09378 0.01574L-0.09597 0.02157L0.09628 0.02157L0.09337 0.01502C0.07007 -0.04275 0.03851 -0.12262 -0.0013 -0.22457Z"/>
</defs></svg>
"""
rep("<body>\n", "<body>\n" + DEFS)

# ---------- TOC ----------
rep("""      <a href="#voice"><span class="n">11</span>Voice</a>
    </nav>""", """      <a href="#voice"><span class="n">11</span>Voice</a>
      <span class="grp">R&amp;D</span>
      <a href="#reading"><span class="n">12</span>The reading</a>
      <a href="#studies"><span class="n">13</span>Studies</a>
      <a href="#tokens"><span class="n">14</span>Tokens</a>
      <a href="#refs"><span class="n">15</span>References</a>
    </nav>""")
rep("""        <a href="#color">Color</a>
      </div>
    </section>""", """        <a href="#color">Color</a>
        <a href="#reading">R&amp;D</a>
      </div>
    </section>""")

# ---------- 02 Thesis: phase colors tie-in ----------
rep("""      <div class="chips"><span>Strategy</span><span>Identity</span><span>Applications</span><span>Production</span></div>
    </section>""", """      <div class="chips"><span>Strategy</span><span>Identity</span><span>Applications</span><span>Production</span></div>
      <p class="note"><span class="legend4" aria-label="Phase colors in Figma order"><i style="background:var(--strategy)"></i><i style="background:var(--identity)"></i><i style="background:var(--application)"></i><i style="background:var(--production)"></i></span>&nbsp;&nbsp;Each phase carries one color. See <a href="#phase-colors">Color</a>.<span class="rnd">R&amp;D</span></p>
    </section>""")

# ---------- 03 POV: the research question ----------
rep("""because those are the tools of work being verified, not advertised.</p>
    </section>""", """because those are the tools of work being verified, not advertised.</p>
      <div class="rndbox">
        <h3 class="sh">In research <span class="rnd">R&amp;D</span></h3>
        <p class="sub">The R&amp;D takes that register literally. The identity is monochrome and carries four phase colors, so it asks what those colors are for. Three instrument traditions give the same answer: in thermal imaging, thin-film interference and color bars, color is a reading on a declared scale, never decoration.</p>
        <p class="rulequote">Color appears only with its reference, and the row of four squares is that reference.</p>
        <p class="note">Hue never builds hierarchy. It only reports a condition. The studies are under <a href="#reading">12 The reading</a> and <a href="#studies">13 Studies</a>.</p>
      </div>
    </section>""")

# ---------- 04 Primitive logic: the ramp ----------
rep("""anything that cannot be decorated and gets cut.</p>
    </section>""", """anything that cannot be decorated and gets cut.</p>
      <div class="rndbox">
        <h3 class="sh">The ramp <span class="rnd">R&amp;D</span></h3>
        <p class="sub">Sorted by how much of a cell each one inks, the primitives become a tone ramp, so an image or a field can be drawn in the brand's own shapes. The chosen ramp, Brand 5, uses the circle with the plus knocked out (as in the device, never a plain filled circle) and scales the plus to 72% so it sits halfway to the monogram.</p>
        <div class="matrix" id="matrix"></div>
      </div>
    </section>""")

# ---------- 05 The mark: masters and open decisions ----------
rep("""      <p class="note">High contrast only, approved files only, no recoloring or effects.</p>
    </section>""", """      <p class="note">High contrast only, approved files only, no recoloring or effects.</p>
      <div class="rndbox">
        <h3 class="sh">On the Figma masters <span class="rnd">R&amp;D</span></h3>
        <div class="tbl"><table>
          <thead><tr><th>Element</th><th>Master</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Device</td><td class="num">252.79 × 124.27</td><td>Used from 14 px to 949 px.</td></tr>
            <tr><td>Wordmark</td><td class="num">1662.39 × 217.19</td><td>Outlined art. No live font matches it, so it is never re-set in type.</td></tr>
            <tr><td>Ⓐ monogram</td><td class="num">135.65 square</td><td>A component instance on the cover.</td></tr>
            <tr><td>Lockup</td><td class="num">1856 × 269.6</td><td>The masters combine wordmark and Ⓐ only; the three-part lockup above has no master yet.</td></tr>
          </tbody>
        </table></div>
        <h3 class="sh">Open decisions <span class="rnd">R&amp;D</span></h3>
        <div class="tbl"><table>
          <thead><tr><th>Decision</th><th>Options</th></tr></thead>
          <tbody>
            <tr><td>Lockup master</td><td>Draw the three-part master (device, wordmark, Ⓐ), or keep the two-part one as drawn.</td></tr>
            <tr><td>Minimum sizes</td><td>Not yet set for the device or the lockup (see above).</td></tr>
            <tr><td>Row order</td><td>Which phase owns which color is fixed. The order of the row is open (see Color).</td></tr>
          </tbody>
        </table></div>
      </div>
    </section>""")

# ---------- 07 Color ----------
rep("""      <h3 class="sh">Grayscale</h3>
      <div><span class="tbd">Grayscale tints TBD · Artifice to supply</span></div>
    </section>""", """      <h3 class="sh">Grayscale</h3>
      <div><span class="tbd">Grayscale tints TBD · Artifice to supply</span></div>
      <div class="rndbox" id="phase-colors">
        <h3 class="sh">Phase colors <span class="rnd">R&amp;D</span></h3>
        <p class="sub">Four colors, one per phase, in the Figma order. They never fill a surface: the surfaces above stay monochrome, and a phase color appears only as a reading on its scale.</p>
        <div class="phases">
          <div class="phase"><div class="chip" style="background:var(--strategy)"></div><div class="nm">Strategy</div><div class="rl">L* 94 · hue 72° · film 308 nm</div><div class="cprow"><button type="button" class="cpbtn" data-copy="#D2FF1E">#D2FF1E</button></div></div>
          <div class="phase"><div class="chip" style="background:var(--identity)"></div><div class="nm">Identity</div><div class="rl">L* 59 · hue 312° · film 398 nm</div><div class="cprow"><button type="button" class="cpbtn" data-copy="#FF1BD1">#FF1BD1</button></div></div>
          <div class="phase"><div class="chip" style="background:var(--application)"></div><div class="nm">Applications</div><div class="rl">L* 85 · hue 181° · film 275 nm</div><div class="cprow"><button type="button" class="cpbtn" data-copy="#00EBEF">#00EBEF</button></div></div>
          <div class="phase"><div class="chip" style="background:var(--production)"></div><div class="nm">Production</div><div class="rl">L* 33 · hue 238° · film 222 nm</div><div class="cprow"><button type="button" class="cpbtn" data-copy="#0009FF">#0009FF</button></div></div>
        </div>
        <p class="note">Measured, they span both media: three sit near print's process inks, one near the screen's blue primary. Mixed as light at 41 : 23 : 10 : 26 they balance to a neutral grey near L* 76, so the monochrome system is their balanced sum.</p>
        <h3 class="sh">Orders</h3>
        <div class="orders">
          <span class="legend4"><i style="background:var(--strategy)"></i><i style="background:var(--identity)"></i><i style="background:var(--application)"></i><i style="background:var(--production)"></i></span>
          <span class="t"><b>Figma order · canonical</b>Strategy, Identity, Applications, Production. In grey, four keys that dip and recover.</span>
          <span class="legend4"><i style="background:var(--production)"></i><i style="background:var(--application)"></i><i style="background:var(--strategy)"></i><i style="background:var(--identity)"></i></span>
          <span class="t"><b>Film order · proposed</b>Production, Applications, Strategy, Identity: the order a thin film passes through as it thickens, and the heat order of the thermal mannequin.</span>
        </div>
        <h3 class="sh">Proposed usage</h3>
        <div class="tbl"><table>
          <thead><tr><th>Rule</th><th>Why</th></tr></thead>
          <tbody>
            <tr><td>A phase color never appears without its scale.</td><td>Thermal color only means something next to its scale bar.</td></tr>
            <tr><td>Exact hexes only in bands, isotherms and readings.</td><td>Photography is the picture; the hexes are the measurement.</td></tr>
            <tr><td>Iridescence never fills a surface.</td><td>Film color appears only where two layers meet, and its hue reports the gap.</td></tr>
            <tr><td>The row of four is the check strip.</td><td>Every other appearance of color is checked against it.</td></tr>
          </tbody>
        </table></div>
        <h3 class="sh">Greys on the Figma masters</h3>
        <p class="sub">Found on the masters, not adopted. The grayscale above stays TBD until Artifice supplies it.</p>
        <div class="greys" id="greys"></div>
        <div class="pluge"><div style="background:#0E0E0E">Ink · L* 4</div><div style="background:#171717">Panel</div><div style="background:#242424">Line</div></div>
        <p class="note">The near-blacks need a check: a badly set screen merges ink, panel and line. The black level check study is built from exactly these.</p>
      </div>
    </section>""")

# ---------- 08 Typography ----------
rep("""          <div class="ds">No monospace anywhere; code shown as content is the only exception.</div>""",
    """          <div class="ds">No monospace anywhere, with no exceptions (Renaise, Oct 20).</div>""")
rep("""          <li><span class="x">✕</span>No monospace anywhere; code shown as content is the only exception.</li>""",
    """          <li><span class="x">✕</span>No monospace anywhere, not even for code or figures.</li>""")
rep("""          <li><span class="x">✕</span>Nothing exceeds 500.</li>""", """          <li><span class="x">✕</span>Nothing exceeds 500.</li>""")
rep("""          <li>Rules and borders are 1px. Radius is 2px.</li>
        </ul></div>""", """          <li>Rules and borders are 1px. Radius is 2px.</li>
        </ul></div>""")
rep("""          <li><span class="x">✕</span>No monospace anywhere, not even for code or figures.</li>
        </ul></div>
      </div>
    </section>""", """          <li><span class="x">✕</span>No monospace anywhere, not even for code or figures.</li>
        </ul></div>
      </div>
      <div class="rndbox">
        <h3 class="sh">Steps on the Figma masters <span class="rnd">R&amp;D</span></h3>
        <div class="tbl"><table>
          <thead><tr><th>Step</th><th>Size</th><th>Case</th><th>Tracking</th><th>Where</th></tr></thead>
          <tbody>
            <tr><td>Body</td><td class="num">24 px</td><td>Sentence</td><td class="num">+12%</td><td>Index and slide body text</td></tr>
            <tr><td>Label</td><td class="num">18 px</td><td>Uppercase</td><td>—</td><td>Phase bar, taglines, chapter numbers, slide headers</td></tr>
            <tr><td>Caption</td><td class="num">18 px</td><td>Sentence</td><td>—</td><td>Index chapter labels</td></tr>
          </tbody>
        </table></div>
        <p class="note">Settings lines that read like instruments (ε 0.95 · SPAN 18–36 °C) are set as labels with tabular figures, never in a monospace face. Rive files and every study use Helvetica Now Display Regular, with Light for display sizes.</p>
      </div>
    </section>""")

# ---------- 09 Motion ----------
rep("""        <div><dt>Duration</dt><dd>around 0.2s</dd></div>
      </dl>
    </section>""", """        <div><dt>Duration</dt><dd>around 0.2s</dd></div>
      </dl>
      <div class="rndbox">
        <h3 class="sh">Stings in development <span class="rnd">R&amp;D</span></h3>
        <div class="tbl"><table>
          <thead><tr><th>Sting</th><th>What happens</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td>Registration Sting</td><td>Crop marks become the scope; four plates close into register; the mark resolves to the screw. 6.4 s, built in Rive as editable keyframes.</td><td>Chosen, in polish</td></tr>
            <tr><td>Warm-up</td><td>The thermal mannequin's head and heart ignite, heat spreads, an isotherm sweeps, and the cells gather into the Ⓐ monogram. About 7 s.</td><td>Study</td></tr>
            <tr><td>Bars and tone</td><td>A leader of the four bars with a slate before every film or reel cut; the same file is the site's loading and offline state.</td><td>Study</td></tr>
          </tbody>
        </table></div>
        <p class="note">Every Rive file is built from a copy of the brand library: its tokens, primitives, marks and one Motion ease.</p>
      </div>
    </section>""")

# ---------- 10 Imagery: the thermal figure is supplied ----------
rep("""        <figure><div class="tile"><span class="tbd">TBD · Artifice to supply</span></div><figcaption>Thermal · the figure as hero</figcaption></figure>""",
    """        <figure><div class="tile" style="padding:0;overflow:hidden"><img src="img/ref-thermal.jpg" alt="The thermal mannequin, Artifice's official image" style="max-width:none;max-height:none;width:100%;height:100%;object-fit:cover" loading="lazy" /></div><figcaption>Thermal · the figure as hero</figcaption></figure>""")
rep("""shot in available light; no stock, no heavy grades.</p>
    </section>""", """shot in available light; no stock, no heavy grades.</p>
      <div class="rndbox">
        <h3 class="sh">Reading the thermal figure <span class="rnd">R&amp;D</span></h3>
        <p class="sub">The thermal image ranks the four colors by heat: blue, cyan, lime, magenta. That is the film order, so the figure already uses the proposed order. On the brand vectorscope its colors sit 0% on target, because the image is softened. Proposed: the photograph stays the picture, and exact phase hexes appear only in bands and isotherms drawn from it.</p>
      </div>
    </section>""")

# ---------- new sections 12-15, before the footer ----------
NEW = r"""
    <!-- 12 · THE READING (R&D) -->
    <section class="card" id="reading">
      <div class="lab"><span class="n">12</span><span>R&amp;D</span></div>
      <h2>The reading</h2>
      <p class="sub">The idea every study tests. The field stays monochrome. Color appears only where a value crosses a declared threshold, and the scale it is read against is always on screen.</p>
      <h3 class="sh">Heat on the field</h3>
      <p class="sub">The primitives as a field, with the pointer as a heat source. Brightness drifts on noise and picks a shape from the ramp; heat lifts cells up the ramp and cools on a known curve. Only cells past the isotherm take a phase color, banded in heat order.</p>
      <div class="fieldwrap">
        <div class="fieldplate" id="fieldplate"><canvas id="field" aria-label="Field of brand primitives with pointer heat and phase isotherms"></canvas><span class="hint">Move to add heat · press to pulse</span></div>
        <div class="scale">
          <span class="sh" style="margin:0">Scale · heat order</span>
          <div class="scalebar" aria-hidden="true"><i style="background:var(--identity)"></i><i style="background:var(--strategy)"></i><i style="background:var(--application)"></i><i style="background:var(--production)"></i><i class="grey"></i></div>
          <div class="scalekey"><span><span>Identity</span><span>hottest</span></span><span><span>Strategy</span><span></span></span><span><span>Applications</span><span></span></span><span><span>Production</span><span id="isoval">iso 0.55</span></span></div>
          <label class="sh" for="iso" style="margin:6px 0 0">Isotherm</label>
          <input id="iso" type="range" min="0.25" max="0.9" step="0.01" value="0.55">
        </div>
      </div>
      <h3 class="sh">Directions</h3>
      <div class="tbl"><table>
        <thead><tr><th>Direction</th><th>What a color means</th><th>Over time</th><th>Where the four colors appear</th></tr></thead>
        <tbody>
          <tr><td>Thermal</td><td>A condition now</td><td>Live, decays</td><td>Isotherm bands on a scale bar</td></tr>
          <tr><td>Iridescence</td><td>The gap between layers, or what has built up</td><td>Persistent</td><td>Film bands in seams, temper, the live mark</td></tr>
          <tr><td>Color bars</td><td>A known value to check against</td><td>Fixed</td><td>The row of four as the reference strip</td></tr>
          <tr><td>Registration</td><td>Where a plate landed against its target</td><td>Per proof</td><td>Four plates on one mark; in register they close to black</td></tr>
        </tbody>
      </table></div>
      <h3 class="sh">Film spectrum</h3>
      <p class="sub">Thin-film color from 0 to 1000 nm, fitted as 47 stops. All four phase colors are second-order colors of one film, which gives them a physical order. A candidate gradient, used only where it reports a gap or a thickness.</p>
      <div class="film" role="img" aria-label="Film spectrum from 0 to 1000 nanometres with the four phase colors marked">
        <span class="mk" style="left:22.2%"><span><i style="background:var(--production)"></i>222</span></span>
        <span class="mk" style="left:27.5%"><span><i style="background:var(--application)"></i>275</span></span>
        <span class="mk" style="left:30.8%"><span><i style="background:var(--strategy)"></i>308</span></span>
        <span class="mk" style="left:39.8%"><span><i style="background:var(--identity)"></i>398</span></span>
      </div>
      <div class="filmaxis"><span>0 nm · black</span><span>500 nm</span><span>1000 nm · pale wash</span></div>
    </section>

    <!-- 13 · STUDIES (R&D) -->
    <section class="card" id="studies">
      <div class="lab"><span class="n">13</span><span>R&amp;D</span></div>
      <h2>Studies</h2>
      <p class="sub">Every live study, by label. Each opens full screen and runs in Figma order or film order. The <a href="rnd.html">R&amp;D index</a> holds the research notes in full.</p>
      <div id="studygroups"></div>
    </section>

    <!-- 14 · TOKENS (R&D) -->
    <section class="card" id="tokens">
      <div class="lab"><span class="n">14</span><span>R&amp;D</span></div>
      <h2>Tokens</h2>
      <p class="sub">Every value on this page, by name. Select a card to copy its value. Surfaces follow the base above; the rest are proposals from the R&amp;D.</p>
      <div id="tokrows"></div>
    </section>

    <!-- 15 · REFERENCES (R&D) -->
    <section class="card" id="refs">
      <div class="lab"><span class="n">15</span><span>R&amp;D</span></div>
      <h2>References</h2>
      <p class="sub">What the system is measured against: instruments that use color as a reading. Each one informed a study above.</p>
      <div class="vgrid" id="refgrid"></div>
    </section>

    <footer>"""
rep("""
    <footer>""", NEW)

# ---------- script ----------
JS = r"""
    // ================= R&D additions =================
    (function () {
      const $ = (q) => document.querySelector(q);
      const el = (tag, cls, html) => { const e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
      const glyph = (id, fill = 'currentColor', s = 1) => `<svg viewBox="-0.5 -0.5 1 1" aria-hidden="true"><use href="#g-${id}" fill="${fill}"${s !== 1 ? ` transform="scale(${s})"` : ''}/></svg>`;
      const dPath = (k) => document.getElementById('g-' + k).getAttribute('d');

      // ramp matrix (04)
      const RAMP = [['Blank', 0, null], ['Plus at 72%', 9, ['cross', .72]], ['Ⓐ monogram', 19, ['mono', 1]], ['Circle with plus', 48, ['screw', 1]], ['Square', 67, ['square', 1]]];
      const mx = $('#matrix');
      mx.append(el('div', 'h rh', 'Ramp')); RAMP.forEach((r, i) => mx.append(el('div', 'h', 'Step ' + i)));
      mx.append(el('div', 'h rh', 'Shape'));
      RAMP.forEach((r) => mx.append(el('div', '', (r[2] ? glyph(r[2][0], 'currentColor', r[2][1]) : '<svg viewBox="-0.5 -0.5 1 1"><rect x="-.5" y="-.5" width="1" height="1" fill="none" stroke="currentColor" stroke-width=".01" stroke-dasharray=".03 .03" opacity=".4"/></svg>') + `<span class="n">${r[0]}</span>`)));
      mx.append(el('div', 'h rh', 'Ink'));
      RAMP.forEach((r) => mx.append(el('div', '', `<span class="cov"><i style="width:${r[1] / 67 * 100}%"></i></span><span class="c">${r[1]}%</span>`)));

      // greys (07)
      const gw = $('#greys');
      for (const [k, v] of [['Ground', '#F6F6F6'], ['Ground', '#EBEBEB'], ['Ground', '#CACACA'], ['Register', '#9A9A9A'], ['Warm 06', '#7A7871'], ['Warm 05', '#5C5A54']])
        gw.append(el('div', 'grey', `<div class="chip" style="background:${v}"></div><div class="k">${k}</div><div class="v">${v}</div>`));

      // studies (13)
      const GROUPS = [
        ['Field and heat', [
          ['shape-field', 'B2', 'Shape Field', 'The live field on the ramp. Move to light it up, click to send a ripple, tune grid, noise and pointer.'],
          ['mannequin', 'D1', 'Mannequin directions', 'The thermal mannequin as a field, isotherm and contour figures, a warm-up sting and the image on the scope.'],
          ['mannequin-3d', 'D2', 'Mannequin in 3D', 'The mannequin as a three-dimensional figure.', true],
          ['phase-sliders', 'G1', 'Phase Sliders', 'The four-box legend opens into a dashed rail and becomes four sliders, from isotherm thresholds to a motion cue sheet.']]],
        ['Film', [
          ['iridescence-1-2', 'E2', 'Temper record · Register test', 'Heat leaves a permanent film in the field; the circle acts as an optical flat whose fringes close to black at register.'],
          ['iridescence-3-6', 'E3', 'Original only · Interference chart · Seam · Coated lens', 'Four iridescence studies in one tabbed page.']]],
        ['Checks', [
          ['color-check-prototypes', 'F2', 'Proof strip · Grey balance', 'Patches measured against targets; only failures take their color. Grey balance was dropped.'],
          ['color-check-suite', 'F3', 'SAFX Color Check', 'Bars and tone leader with slate, a black level check from the near-blacks, and a plate switchboard.'],
          ['vectorscope', 'F4', 'Brand Vectorscope', 'The circle as graticule, the plus as axes, the four colors as target boxes.'],
          ['registration-scope', 'G2', 'Registration Scope', 'Registration marks joined with the vectorscope. Four plates on one mark; in register they close to black.']]],
      ];
      const sg = $('#studygroups');
      for (const [g, list] of GROUPS) {
        sg.append(el('h3', 'sh grouph', g));
        const grid = el('div', 'vgrid');
        for (const [src, id, t, d, noimg] of list) {
          const media = noimg ? glyph('screw', '#9a9a9a') : `<img loading="lazy" src="img/${src}.jpg" alt="">`;
          const a = el('a', 'vcard', `<span class="img">${media}</span><span class="t">${t}</span><span class="m">${id} · Study ↗</span><span class="d">${d}</span>`);
          a.href = 'pages/' + src + '.html'; a.target = '_blank'; a.rel = 'noopener';
          grid.append(a);
        }
        sg.append(grid);
      }

      // tokens (14)
      const T = (nm, tk, val, kind, sw) => ({ nm, tk, val, kind, sw: sw || val });
      const TOK = [
        ['Surfaces', 'From the base. Hierarchy from value and scale, never hue.', [T('The ground.', '--ink', '#0E0E0E'), T('The text on it.', '--paper', '#F4F1EA'), T('The light sections.', '--linen', '#FCFAF5'), T('The raised surface.', '--panel', '#171717'), T('The hairline.', '--line', '#242424')]],
        ['Phase', 'Figma order, canonical. One color per phase.', [T('Strategy', '--strategy', '#D2FF1E'), T('Identity', '--identity', '#FF1BD1'), T('Applications', '--application', '#00EBEF'), T('Production', '--production', '#0009FF')]],
        ['Film order', 'Proposed. The same four by thickness and by heat.', [T('222 nm. Coolest.', '--production', '#0009FF'), T('275 nm', '--application', '#00EBEF'), T('308 nm', '--strategy', '#D2FF1E'), T('398 nm. Hottest.', '--identity', '#FF1BD1'), T('0 to 1000 nm, 47 stops.', '--film', 'Gradient', null, 'var(--film)')]],
        ['Lines', 'Structure.', [T('Legend and register border.', '--register', '#9A9A9A')]],
        ['Ramp', 'Brand 5. Ink coverage of each step in its cell.', [T('Blank', '--ramp-0', '0%', 'g:'), T('Plus at 72%', '--ramp-1', '9%', 'g:cross'), T('Ⓐ monogram', '--ramp-2', '19%', 'g:mono'), T('Circle with plus', '--ramp-3', '48%', 'g:screw'), T('Square', '--ramp-4', '67%', 'g:square')]],
        ['Type and motion', 'One family; one curve.', [T('Everything. Regular.', '--sans', 'Helvetica Now Display', 't:400'), T('Display. Light.', '--fw-display', '300', 't:300'), T('The one curve.', '--ease', 'cubic-bezier(.22,1,.36,1)', 'x'), T('Around 0.2s.', '--dur', '.2s', 'x')]],
      ];
      const tr = $('#tokrows');
      for (const [g, note, list] of TOK) {
        tr.append(el('div', 'tgroup', g)); tr.append(el('p', 'tgroupn', note));
        const grid = el('div', 'tgrid');
        for (const t of list) {
          let sw;
          if (t.kind && t.kind.startsWith('g:')) { const k = t.kind.slice(2); sw = `<span class="tsw glyph">${k ? glyph(k, 'currentColor', k === 'cross' ? .72 : 1) : ''}</span>`; }
          else if (t.kind && t.kind.startsWith('t:')) sw = `<span class="tsw type" style="font-weight:${t.kind.slice(2)}">Aa</span>`;
          else if (t.kind === 'x') sw = `<span class="tsw type" style="font-size:13px;color:var(--text-3)">${t.tk === '--ease' ? 'ease' : '0.2s'}</span>`;
          else sw = `<span class="tsw" style="background:${t.sw}"></span>`;
          const b = el('button', 'tcard', `${sw}<span class="tbody"><span class="tnm">${t.nm}</span><span class="tkv">${t.tk}</span><span class="thx">${t.val}</span></span>`);
          b.type = 'button'; b.title = 'Copy ' + t.val;
          b.onclick = async () => { try { await navigator.clipboard.writeText(t.val === 'Gradient' ? `var(${t.tk})` : t.val); b.classList.add('copied'); setTimeout(() => b.classList.remove('copied'), 1200); } catch (e) {} };
          grid.append(b);
        }
        tr.append(grid);
      }

      // references (15)
      const scope = `<svg viewBox="-60 -60 120 120" aria-hidden="true"><circle r="50" fill="none" stroke="#9A9A9A" stroke-width=".6"/><path d="M-50 0H50M0 -50V50" stroke="#9A9A9A" stroke-width=".5"/>${[[72,'#D2FF1E'],[312,'#FF1BD1'],[181,'#00EBEF'],[238,'#0009FF']].map(([h,c])=>{const a=(h-90)*Math.PI/180,x=Math.cos(a)*38,y=Math.sin(a)*38;return `<rect x="${(x-4).toFixed(1)}" y="${(y-4).toFixed(1)}" width="8" height="8" fill="none" stroke="${c}" stroke-width=".9"/>`}).join('')}<circle r="1.4" fill="#F4F1EA"/></svg>`;
      const ramp = (() => { const seq = ['', 'cross', 'mono', 'screw', 'square']; let s = '<svg viewBox="0 0 240 180" aria-hidden="true">'; for (let y = 0; y < 9; y++) for (let x = 0; x < 12; x++) { const v = (Math.sin(x * .45 + y * .3) + Math.cos(y * .6 - x * .2) + 2) / 4; const k = seq[Math.min(4, Math.floor(v * 5))]; if (k) s += `<use href="#g-${k}" fill="#F4F1EA" transform="translate(${10 + x * 20} ${10 + y * 20}) scale(${k === 'cross' ? 10 : 14})"/>`; } return s + '</svg>'; })();
      const REFS = [
        ['img/ref-thermal.jpg', 'Thermal imaging', 'False color · isotherms', 'A palette stretched across a declared temperature window, meaningless without its scale bar. Isotherms color only what crosses a threshold.'],
        ['img/ref-film.jpg', 'Thin-film interference', 'Soap film · temper colors', 'Color that is a distance, not a pigment. The four phase colors are second-order colors of one film, 222 to 398 nm.'],
        ['img/ref-bars.jpg', 'SMPTE color bars', 'Broadcast reference', 'Known values sent ahead of the signal so everything after can be checked. In grey they step down a staircase.'],
        ['img/ref-marks.png', 'Registration marks', 'Print · control strip', 'A circle and a crosshair printed on every plate. In register the plates stack to one black mark; drift splits it into colored ghosts.', true],
        [scope, 'Vectorscope', 'Broadcast · color targets', 'Every pixel plotted by hue and saturation against target boxes. The circle is the graticule, the plus the axes.'],
        [ramp, 'ASCII art', 'Tone by ink coverage', 'Characters sorted by how much of a cell they ink, so type can render any image. The ramp does the same with the primitives.'],
      ];
      const rg = $('#refgrid');
      for (const [m, t, meta, d, paper] of REFS) {
        const media = m.startsWith('<svg') ? m : `<img loading="lazy" src="${m}" alt="">`;
        rg.append(el('div', 'vcard', `<span class="img${paper ? ' paper' : ''}">${media}</span><span class="t">${t}</span><span class="m">${meta}</span><span class="d">${d}</span>`));
      }

      // the field (12)
      const cv = $('#field'), plate = $('#fieldplate'), ctx = cv.getContext('2d');
      const G = {}; for (const k of ['square', 'screw', 'cross', 'mono']) G[k] = new Path2D(dPath(k));
      const STEPS = [0, .09, .19, .48, .67], HEAT = ['#0009FF', '#00EBEF', '#D2FF1E', '#FF1BD1'], TONES = ['', '#5e5e5e', '#8f8f8f', '#b4b4b4', '#F4F1EA'];
      let W = 0, H = 0, cols = 0, rows = 0, cell = 22, heat = new Float32Array(0), dpr = 1, iso = .55;
      const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
      $('#iso').oninput = (e) => { iso = +e.target.value; $('#isoval').textContent = 'iso ' + iso.toFixed(2); if (still) draw(0); };
      function resize() { dpr = Math.min(2, devicePixelRatio || 1); const r = plate.getBoundingClientRect(); W = r.width; H = r.height; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); cell = W < 520 ? 16 : 22; cols = Math.ceil(W / cell); rows = Math.ceil(H / cell); heat = new Float32Array(cols * rows); }
      const P = new Uint8Array(512); { const p = [...Array(256).keys()]; for (let i = 255; i > 0; i--) { const j = (Math.random() * (i + 1)) | 0; [p[i], p[j]] = [p[j], p[i]]; } for (let i = 0; i < 512; i++) P[i] = p[i & 255]; }
      const fade = (t) => t * t * (3 - 2 * t), h3 = (x, y, z) => P[(P[(P[x & 255] + y) & 255] + z) & 255] / 255;
      function noise(x, y, z) { const xi = Math.floor(x), yi = Math.floor(y), zi = Math.floor(z), xf = fade(x - xi), yf = fade(y - yi), zf = fade(z - zi), l = (a, b, t) => a + (b - a) * t; const v = (dz) => l(l(h3(xi, yi, zi + dz), h3(xi + 1, yi, zi + dz), xf), l(h3(xi, yi + 1, zi + dz), h3(xi + 1, yi + 1, zi + dz), xf), yf); return l(v(0), v(1), zf); }
      const ptr = { x: 0, y: 0, on: false };
      function addHeat(px, py, amt, rad) { const cx = px / cell, cy = py / cell, R = rad / cell; for (let y = Math.max(0, (cy - R) | 0); y < Math.min(rows, cy + R + 1); y++) for (let x = Math.max(0, (cx - R) | 0); x < Math.min(cols, cx + R + 1); x++) { const d = Math.hypot(x + .5 - cx, y + .5 - cy) / R; if (d < 1) { const i = y * cols + x; heat[i] = Math.min(1, heat[i] + amt * (1 - d * d)); } } }
      const at = (e) => { const r = plate.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; };
      plate.addEventListener('pointermove', (e) => { [ptr.x, ptr.y] = at(e); ptr.on = true; if (still) { addHeat(ptr.x, ptr.y, .12, 70); draw(0); } });
      plate.addEventListener('pointerleave', () => { ptr.on = false; });
      plate.addEventListener('pointerdown', (e) => { const [x, y] = at(e); addHeat(x, y, .9, 120); if (still) draw(0); });
      function draw(t) {
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.fillStyle = '#0b0b0b'; ctx.fillRect(0, 0, W, H);
        const s = cell * .8, z = t * .00012, by = [[], [], [], [], []], hot = [];
        for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) {
          const i = y * cols + x, n = noise(x * .09 + noise(x * .03, y * .03, z) * 2, y * .09, z * 2);
          const v = Math.min(1, Math.max(0, Math.min(1, (n - .25) * 1.5)) * .62 + heat[i]);
          let k = 0, best = 9; for (let j = 0; j < 5; j++) { const d = Math.abs(STEPS[j] - v * .67); if (d < best) { best = d; k = j; } }
          if (heat[i] > iso) hot.push([x, y, k || 4, Math.min(3, Math.floor((heat[i] - iso) / ((1 - iso) / 4)))]); else if (k) by[k].push(x, y);
        }
        const paint = (k, x, y) => { const sc = s * (k === 1 ? .72 : 1); ctx.setTransform(dpr * sc, 0, 0, dpr * sc, dpr * (x * cell + cell / 2), dpr * (y * cell + cell / 2)); ctx.fill(k === 1 ? G.cross : k === 2 ? G.mono : k === 3 ? G.screw : G.square, 'evenodd'); };
        for (let k = 1; k < 5; k++) { ctx.fillStyle = TONES[k]; const a = by[k]; for (let j = 0; j < a.length; j += 2) paint(k, a[j], a[j + 1]); }
        for (const [x, y, k, b] of hot) { ctx.fillStyle = HEAT[b]; paint(k, x, y); }
        ctx.setTransform(1, 0, 0, 1, 0, 0);
      }
      let last = 0, visible = true;
      new IntersectionObserver((es) => { visible = es[0].isIntersecting; }).observe(plate);
      function loop(t) {
        requestAnimationFrame(loop);
        if (!visible || t - last < 30) return;
        const dt = Math.min(64, t - last) / 1000; last = t;
        if (ptr.on) addHeat(ptr.x, ptr.y, .16, 80); else addHeat(W * (.5 + .36 * Math.sin(t * .00041)), H * (.5 + .32 * Math.sin(t * .00067 + 1)), .09, 70);
        const k = Math.exp(-dt / 1.2); for (let i = 0; i < heat.length; i++) heat[i] *= k;
        draw(t);
      }
      resize();
      if (still) { addHeat(W * .5, H * .5, .95, 110); addHeat(W * .3, H * .4, .7, 70); }
      draw(0);
      addEventListener('resize', () => { resize(); draw(performance.now()); });
      if (!still) requestAnimationFrame(loop);
    })();
  </script>"""
rep("""      syncEnd();
    })();
  </script>""", """      syncEnd();
    })();
""" + JS)

(HERE / "public" / "index.html").write_text(s)
print("ok", len(s))
