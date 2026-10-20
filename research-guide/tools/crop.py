import sys
from PIL import Image
S=sys.argv[1]
C={ # x,y,w  (h = w*0.75)
'shape-field':(0,0,860),
'mannequin':(300,330,660),
'iridescence-1-2':(560,90,700),
'iridescence-3-6':(260,100,740),
'color-check-suite':(16,270,900),
'color-check-prototypes':(40,500,720),
'vectorscope':(60,270,800),
'phase-sliders':(330,300,620),
'registration-scope':(250,640,600),
}
for n,(x,y,w) in C.items():
    im=Image.open(f'{S}/raw/{n}.png').convert('RGB')
    h=int(w*.75); c=im.crop((x,y,x+w,y+h)).resize((800,600),Image.LANCZOS)
    c.save(f'{S}/site/public/img/{n}.jpg',quality=82)
ims=[Image.open(f'{S}/site/public/img/{n}.jpg').resize((400,300)) for n in C]
W=Image.new('RGB',(1200,900))
for i,im in enumerate(ims): W.paste(im,((i%3)*400,(i//3)*300))
W.save(f'{S}/crops.png')
