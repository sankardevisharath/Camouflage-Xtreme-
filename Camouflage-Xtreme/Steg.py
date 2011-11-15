import os
import random
import Image

def pixel_embed(d, c):
    c = ord(c)
    return (((d[0] >> 3) << 3) | (c >> 5), ((d[1] >> 3) << 3) | ((c >> 2) % 8), ((d[2] >> 2)<<2) | (c%4))
         

def embed_inplace(image, data, key):
    w = image.size[0]
    r = range(0, w)
    y = 1
    x = err = 0
    random.seed(key[0])
    random.shuffle(r)
    t = ln = len(data)
    if ln > w * (image.size[1] - 1) :
	ln = w * (image.size[1] - 1)
        err = 1
    for i in xrange(0, 4):
        pixel = pixel_embed(image.getpixel((i, 0)), chr(t % 256))
        image.putpixel((i, 0), pixel)
        t >>= 8
    for i in xrange(0, ln):
        pixel = pixel_embed(image.getpixel((r[x], y)), data[i])
        image.putpixel((r[x], y), pixel)
        if x == (w - 1):
            random.shuffle(r)
            x = 0
            y += 1
        else:
            x += 1
    return err


def embed_lossless(image_in, data_in, image_out, key):
    data_in = open(data_in, 'rb')
    data = data_in.read()
    image = Image.open(image_in)
    err = embed_inplace(image, data, key)
    image.save(image_out)
    return err


def pixel_extract(x, y, image):
    p = image.getpixel((x, y))
    return (((p[0] % 8) << 5) + ((p[1] % 8) << 2) + (p[2] % 4))


def extract_lossless(image_in, data_out, key):
    image = Image.open(image_in)
    data_out = open(data_out, 'wb')
    w = image.size[0]
    r = range(0, w)
    y = 1
    x = ln = 0
    random.seed(key[0])
    random.shuffle(r)
    for i in xrange(0, 4):
        ln += (256 ** i) * (pixel_extract(i, 0, image))
    if ln > w * (image.size[1] - 1) :
	ln = w * (image.size[1] - 1)
    ln = (ln/16)*16
    for i in xrange(0, ln):
        data_out.write(chr(pixel_extract(r[x], y, image)))
        if x == (w - 1):
            random.shuffle(r)
            x = 0
            y += 1
        else:
            x += 1


def embed(in_img, in_data, out_img, key = ' '):
    l = len(out_img)
    if out_img[l-4] + out_img[l - 3] + out_img[l - 2] + out_img[l - 1] == '.jpg' :
        out_format = 'JPEG'
    else:
        out_format = 'BMP'
    image = Image.open(in_img)
    in_format = image.format
    if  out_format != 'JPEG' :
        return embed_lossless(in_img, in_data, out_img, key)
    elif out_format == 'JPEG' and in_format != 'JPEG' :
        image.save('tmp.jpg')
        err = os.system('./jpgsteg ' + ' -e tmp.jpg ' + in_data + ' ' + out_img)
        os.remove('tmp.jpg')
        return err
    else:
        return os.system('./jpgsteg ' + ' -e ' + in_img + ' ' + in_data + ' ' + out_img)


def extract(in_img, out_data, key = ' '):
    image = Image.open(in_img)
    in_format = image.format
    if in_format == 'JPEG':
        os.system('./jpgsteg ' + ' -d ' + in_img + ' ' + out_data)
    else:
        extract_lossless(in_img, out_data, key)
