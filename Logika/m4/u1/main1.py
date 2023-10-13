from PIL import Image, ImageFilter
class ImageEditor():
    def __init__(self,filename):
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
       left=self.original.transpose(Image.ROTATE_90)
       self.edited.append(left)
       left.save('left_'+self.filename)
img = ImageEditor('cat.jpeg')
img.open_file()
img.do_left()