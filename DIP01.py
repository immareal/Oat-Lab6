from PIL import Image

im = Image.open('image1.jpg')

w,h = im.size

for i in range(10,76):

    dec = 100-i
    im = im.resize((int(w*dec/100),int(h*dec/100)))
    name = f'Image1-{i}.jpg'
    im.save(name)

