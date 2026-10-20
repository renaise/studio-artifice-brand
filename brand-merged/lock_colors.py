# Renaise's decision (Oct 20): Figma order is final, each color locked to one phase. Film order retired.
import re, sys
p = 'public/index.html'; s = open(p).read()
def rep(a, b):
    global s
    if s.count(a) != 1: sys.exit('mismatch: ' + a[:70])
    s = s.replace(a, b)
rep('<tr><td>Row order</td><td>Which phase owns which color is fixed. The order of the row is open (see Color).</td></tr>\n', '')
rep('<p class="sub">Four colors, one per phase, in the Figma order. They never fill a surface',
    '<p class="sub">Four colors, each locked to one phase, in the Figma order: lime is Strategy, magenta is Identity, cyan is Applications, blue is Production. Renaise decided on Oct 20 that the pairs and the order are final. The colors never fill a surface')
s, n = re.subn(r' · film \d+ nm</div>', '</div>', s); assert n == 4
a = s.index('        <h3 class="sh">Orders</h3>'); b = s.index('        <h3 class="sh">Proposed usage</h3>')
s = s[:a] + '''        <h3 class="sh">Pairs</h3>
        <div class="orders">
          <span class="legend4"><i style="background:var(--strategy)"></i><i style="background:var(--identity)"></i><i style="background:var(--application)"></i><i style="background:var(--production)"></i></span>
          <span class="t"><b>Figma order · final</b>Strategy, Identity, Applications, Production. A color always names its phase, and the row always runs in this order. The film order proposed in the R&amp;D is retired.</span>
        </div>
''' + s[b:]
rep('<tr><td>A phase color never appears without its scale.</td>', '<tr><td>A phase color always names its phase.</td><td>The pairs are fixed, so a color is read as its phase wherever it appears.</td></tr>\n            <tr><td>A phase color never appears without its scale.</td>')
rep('The thermal image ranks the four colors by heat: blue, cyan, lime, magenta. That is the film order, so the figure already uses the proposed order. On the brand vectorscope',
    'The thermal image ranks its colors by heat: blue, cyan, lime, magenta. That is not the phase order, so its colors stay part of the picture and are never read as phases. On the brand vectorscope')
rep('banded in heat order.</p>', 'banded in the Figma order: Production at the isotherm, Strategy at the hottest.</p>')
rep('Scale · heat order', 'Scale · Figma order')
rep('<div class="scalebar" aria-hidden="true"><i style="background:var(--identity)"></i><i style="background:var(--strategy)"></i>',
    '<div class="scalebar" aria-hidden="true"><i style="background:var(--strategy)"></i><i style="background:var(--identity)"></i>')
rep('<span><span>Identity</span><span>hottest</span></span><span><span>Strategy</span><span></span></span>',
    '<span><span>Strategy</span><span>hottest</span></span><span><span>Identity</span><span></span></span>')
rep("HEAT = ['#0009FF', '#00EBEF', '#D2FF1E', '#FF1BD1']", "HEAT = ['#0009FF', '#00EBEF', '#FF1BD1', '#D2FF1E']")
a = s.index('      <h3 class="sh">Film spectrum</h3>'); b = s.index('<div class="filmaxis">'); b = s.index('</div>', b) + 7
s = s[:a] + s[b:]
rep('runs in Figma order or film order.', 'runs in the Figma order. Some still offer the retired film order as a toggle.')
a = s.index("        ['Film order', 'Proposed."); b = s.index('\n', a) + 1; s = s[:a] + s[b:]
rep('Figma order, canonical. One color per phase.', 'Figma order, final. Each color locked to its phase.')
rep('The four phase colors are second-order colors of one film, 222 to 398 nm.', 'Its bands report a gap or a thickness.')
open(p, 'w').write(s); print('ok')
