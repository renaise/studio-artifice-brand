"""Swap broken or off-topic readings in References (15) for checked sources.
Works on the site page (rf- classes) and the review draft (plain classes)."""
import re
def li(p, kind, href, title, rest, note):
    return (f'<li><span class="{p}kind">{kind}</span><span class="{p}cite"><a class="{p}t" href="{href}" target="_blank" rel="noopener">{title}</a>. {rest}'
            f'<span class="{p}n">{note}</span></span></li>')
def new(p):
    bars = [li(p, 'Free paper', 'https://sterneworks.org/Mulvin-Sterne-Scenes.pdf', 'Scenes from an Imaginary Country: Test Images and the American Color Television Standard',
               'Dylan Mulvin and Jonathan Sterne. <i>Television &amp; New Media</i>, 2016. Author’s copy.',
               'How the test images used to set American color television decided what “correct” color looks like. A readable humanities paper on why a reference is never neutral.'),
            li(p, 'Article', 'https://tedium.co/2025/01/19/television-test-patterns-history/', 'Test Pattern History: How Color Bars Became a TV Staple',
               'Ernie Smith. <i>Tedium</i>, 2025.',
               'Where the bars came from, who designed them at RCA, and what each part of the pattern lets an engineer check.')]
    reg = [li(p, 'Museum book, free online', 'https://printedpicture.artgallery.yale.edu/the-book/color-printing', 'Color Printing',
              'Richard Benson. <i>The Printed Picture</i>, Yale University Art Gallery.',
              'A master printer walks through color printing, from stencils to chromolithography, and shows why every added color brings the problem of registration.'),
           li(p, 'Museum guide', 'https://education.asianart.org/resources/the-ukiyo-e-woodblock-printing-process/', 'The Ukiyo-e (Woodblock) Printing Process',
              'Asian Art Museum of San Francisco, Education.',
              'Registration marks in their oldest working form: <i>kento</i> notches cut into every color block so each pass lands in the same place.')]
    scope2 = li(p, 'Free primer', 'https://download.tek.com/document/25W_29166_0_Interactive.pdf', 'The Basics of Waveform Monitors and Vectorscopes',
                'Tektronix, application note.',
                'The instrument maker’s own introduction: what the targets on the scope mean and where color bars should land in them.')
    return bars, reg, scope2
def lis_of(art):
    return re.findall(r'<li>.*?</li>', art, re.S)
for path, p in [('/mnt/project-files/brand-merged/public/index.html', 'rf-'), ('/mnt/project-files/references/reference-sources.html', '')]:
    s = open(path).read()
    tag = '<article class="rf">' if p else '<article class="ref">'
    parts = s.split(tag)
    assert len(parts) == 6, (path, len(parts))
    bars, reg, scope2 = new(p)
    for i, h in [(3, 'SMPTE color bars'), (4, 'Registration marks'), (5, 'Vectorscope')]:
        assert h in parts[i], (path, i)
        old = lis_of(parts[i].split('</article>')[0])
        assert len(old) == 2
        repl = {3: bars, 4: reg, 5: [old[0], scope2]}[i]
        for o, n in zip(old, repl): parts[i] = parts[i].replace(o, n, 1)
        # drop gap notes that described the old sources
        if i in (3, 5): parts[i] = re.sub(r'\s*<p class="gap">.*?</p>', '', parts[i], count=1, flags=re.S)
    s = tag.join(parts)
    for gone in ['blogs.library.duke.edu', 'atlas_halftone.pdf', 'oshermaps.org']:
        assert gone not in s, (path, gone)
    open(path, 'w').write(s)
    print('ok', path)
