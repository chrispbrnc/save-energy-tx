'''
Generate site icons from a single 192x192 png file
'''
from PIL import Image

types = {
    'android-chrome': [192],
    'apple-touch-icon': [114, 120, 144, 152, 180, 57, 60, 72, 76],
    'favicon': [16, 32, 48, 64, 96]
}

def resize_file(infile, outfile, size):
    try:
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, 'PNG')
    except IOError:
        print("cannot create thumbnail for '{}'".format(infile))


def make_icons(infile):
    for name in types:
        for l in types[name]:
            size = (l, l)
            outfile = 'app/static/icons/{}-{}x{}.png'.format(name, l, l)
            print(outfile)
            resize_file(infile, outfile, size)



if __name__ == '__main__':
    make_icons('app/static/images/icon_base.png')
