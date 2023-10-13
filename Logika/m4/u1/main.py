from PIL import Image, ImageFilter

with Image.open('cat.jpeg') as cat_photo:
    print(cat_photo.size)
    print(cat_photo.format)
    print(cat_photo.mode)

    bw_photo = cat_photo.convert('L')
    # bw_photo.show()



    blur_photo = cat_photo.filter(ImageFilter.BLUR)
    # blur_photo.show()



    left_photo = cat_photo.transpose(Image.ROTATE_90)
    left_photo.show()
    bw_photo.save('bw_cat.jpeg')