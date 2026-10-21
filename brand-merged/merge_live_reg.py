"""Take the registration readings from the live page (Winterthur + Yale 'Photography in Ink'),
keep this repo's color bars and vectorscope readings."""
import re
live = open('/tmp/claude-0/-home-user-studio-artifice-brand/ff89e9da-dc1f-519d-ba60-28c9dbc5d84e/scratchpad/refs/live.html').read()
reg_live = [a for a in re.findall(r'<article class="rf">.*?</article>', live, re.S) if 'Registration marks' in a][0]
new_lis = re.findall(r'<li>.*?</li>', reg_live, re.S)
assert len(new_lis) == 2 and 'winterthur' in new_lis[0]
for path, p in [('public/index.html', 'rf-'), ('/mnt/project-files/references/reference-sources.html', '')]:
    s = open(path).read()
    tag = '<article class="rf">' if p else '<article class="ref">'
    parts = s.split(tag); i = next(k for k, x in enumerate(parts) if '>Registration marks<' in x)
    old = re.findall(r'<li>.*?</li>', parts[i].split('</article>')[0], re.S)
    for o, n in zip(old, new_lis):
        parts[i] = parts[i].replace(o, n if p else n.replace('rf-', ''), 1)
    s = tag.join(parts); open(path, 'w').write(s)
    assert 'winterthur' in s and 'Mulvin' in s and 'download.tek.com' in s and 'duke.edu' not in s and 'asianart' not in s
    print('ok', path)
