from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будемо змішувати відповіді в картці питання

from PyQt5.QtGui import QPixmap,QIcon

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

def show_data():
    ''' показує на екрані потрібну інформацію '''
    pass

def check_result():
    ''' перевірка, чи вибрана правильна відповідь 
    якщо відповідь була вибрана, то напис "правильно/не правильно" отримує потрібне значення
    і показує панель відповідів'''
    pass

win_card = QWidget()
#тут повинні бути параметри вікна

win_card.setWindowTitle('Memory card')
pixmap = QPixmap('m2\\memory_card\\logo.png')
win_card.setWindowIcon(QIcon(pixmap))
win_card.setLayout(layout_card)
win_card.setStyleSheet('background-color:purple;color:white;font-size:20px')
win_card.resize(card_width,card_height)
win_card.show()
app.exec_()