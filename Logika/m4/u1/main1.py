from PIL import Image, ImageFilter


class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.edited = []

    def open_file(self):
        try:
            self.original = Image.open(self.filename)
            self.original.show()
        except:
            print('Такого файлу не знайдено')

    def do_left(self):
        left = self.original.transpose(Image.ROTATE_90)
        self.edited.append(left)
        left.save('left_'+self.filename)

    def bw_photo(self):
        bw = self.original.convert('L')
        self.edited.append(bw)
        bw.save('bw_' + self.filename)

    def cropp(self):
        box = (25, 25, 25,25)
        cropped = self.original.crop(box)
        self.edited.append(cropped)
        


img = ImageEditor('cat.jpeg')
img.open_file()
img.do_left()
img.bw_photo()
