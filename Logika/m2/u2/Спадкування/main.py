class Widget():
    def __init__(self,text,num_x,num_y) :

        self.text = text
        self.num_x = num_x
        self.num_y = num_y
    def print_about(self):
        print('Напис:',self.text)
        print('Розташування:',self.num_x,self.num_y)
class Button(Widget):
    def __init__(self, text, num_x, num_y):
        super().__init__(text, num_x, num_y)
        self.is_clicked = False
    def clicked(self):
        self.is_clicked = True
        print('Ви зареєстровані')
objekt = Button('Брати участь',100,100)
objekt.print_about()

action = input('Хочете зареєструватись?(так/ні):').lower()
if action =='так':
    objekt.clicked()
else:
    print('А шкода!')
    