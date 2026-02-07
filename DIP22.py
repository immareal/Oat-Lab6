from PIL import Image

im = Image.open('WatWaAram.jpg')
w, h = im.size

img_red   = im.copy()
img_green = im.copy()
img_blue  = im.copy()
img_mean  = im.copy()
img_max   = im.copy()
img_min   = im.copy()
img_bw    = im.copy()
img_sepia = im.copy()
img_cyano = im.copy()

for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i, j))

        img_red.putpixel((i, j), (r, r, r))
        img_green.putpixel((i, j), (g, g, g))
        img_blue.putpixel((i, j), (b, b, b))

        mean = (r + g + b) // 3
        img_mean.putpixel((i, j), (mean, mean, mean))

        mx = max(r, g, b)
        img_max.putpixel((i, j), (mx, mx, mx))

        mn = min(r, g, b)
        img_min.putpixel((i, j), (mn, mn, mn))

        bw = 255 if mean > 128 else 0
        img_bw.putpixel((i, j), (bw, bw, bw))

        tr = int(0.393*r + 0.769*g + 0.189*b)
        tg = int(0.349*r + 0.686*g + 0.168*b)
        tb = int(0.272*r + 0.534*g + 0.131*b)
        img_sepia.putpixel((i, j),
            (min(255, tr), min(255, tg), min(255, tb))
        )

        tr = 0
        tg = int(0.5 * g)
        tb = int(0.8 * b + 0.2 * g)
        img_cyano.putpixel((i, j),
            (tr, min(255, tg), min(255, tb))
        )

out = im.copy()

cw = w // 3
ch = h // 3

out.paste(img_red.crop((0,0,cw,ch)), (0,0))
out.paste(img_green.crop((cw,0,2*cw,ch)), (cw,0))
out.paste(img_blue.crop((2*cw,0,w,ch)), (2*cw,0))

out.paste(img_max.crop((0,ch,cw,2*ch)), (0,ch))
out.paste(img_min.crop((cw,ch,2*cw,2*ch)), (cw,ch))
out.paste(img_mean.crop((2*cw,ch,w,2*ch)), (2*cw,ch))

out.paste(img_bw.crop((0,2*ch,cw,h)), (0,2*ch))
out.paste(img_sepia.crop((cw,2*ch,2*cw,h)), (cw,2*ch))
out.paste(img_cyano.crop((2*cw,2*ch,w,h)), (2*cw,2*ch))

out.save('Wat22.jpg')
out.show()
