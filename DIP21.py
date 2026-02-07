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
        img_sepia.putpixel(
            (i, j),
            (min(255, tr), min(255, tg), min(255, tb))
        )

        tr = 0
        tg = int(0.5 * g)
        tb = int(0.8 * b + 0.2 * g)
        img_cyano.putpixel(
            (i, j),
            (tr, min(255, tg), min(255, tb))
        )



canvas = Image.new("RGB", (w * 3, h * 3))

canvas.paste(img_red, (0, 0))
canvas.paste(img_green, (w, 0))
canvas.paste(img_blue, (w * 2, 0))

canvas.paste(img_max, (0, h))
canvas.paste(img_min, (w, h))
canvas.paste(img_mean, (w * 2, h))

canvas.paste(img_bw, (0, h * 2))
canvas.paste(img_sepia, (w, h * 2))
canvas.paste(img_cyano, (w * 2, h * 2))

canvas.show()
