import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence
from PIL import Image, ImageFilter

from PIL import Image, ImageFilter
app = QApplication([])
window = QWidget()
folder_btn = QPushButton('Папка')
lst_photos = QListWidget()

left_btn = QPushButton('Вілво')
right_btn = QPushButton('Вправо')
mirrow_btn = QPushButton('Дзеркало')
sharpness_btn = QPushButton('Різкість')
color_btn = QPushButton('Ч/Б')
photo = QLabel('Картинка')



left_btn.setStyleSheet('''
    QPushButton {
        background-color: orange;
    }
    QPushButton:hover {
        background-color: darkorange;
    }
''')
right_btn.setStyleSheet('''
    QPushButton {
        background-color: green;
    }
    QPushButton:hover {
        background-color: darkgreen;
    }
''')

mirrow_btn.setStyleSheet('''
    QPushButton {
        background-color: red;
    }
    QPushButton:hover {
        background-color: darkred;
    }
''')

sharpness_btn.setStyleSheet('''
    QPushButton {
        background-color: white;
    }
    QPushButton:hover {
        background-color: grey;
    }
''')
color_btn.setStyleSheet('''
    QPushButton {
        background-color: blue;
    }
    QPushButton:hover {
        background-color: darkblue;
    }
''')

folder_btn.setStyleSheet('''
    QPushButton {
        background-color: grey;
    }
    QPushButton:hover {
        background-color: white;
    
    }
    
''')
lst_photos.setStyleSheet('''
    background-color:purple

''')

window.setStyleSheet('''


    font-size:20px;
    border: 1px solid blue;
    background-color:cyan;
    




''')


vertical_1 = QVBoxLayout()
horisontal_1 = QHBoxLayout()
vertical_2 = QVBoxLayout()
horisontal_2 = QHBoxLayout()


vertical_1.addWidget(folder_btn)
vertical_1.addWidget(lst_photos)


horisontal_1.addWidget(left_btn)
horisontal_1.addWidget(right_btn)
horisontal_1.addWidget(mirrow_btn) 
horisontal_1.addWidget(sharpness_btn)
horisontal_1.addWidget(color_btn)


vertical_2.addWidget(photo)
vertical_2.addLayout(horisontal_1)


horisontal_2.addLayout(vertical_1,1)
horisontal_2.addLayout(vertical_2,4)

workdir = QFileDialog.getExistingDirectory()

files_and_folders = os.listdir(workdir)
def filter(files):
    result = []
    ext = ['png', 'jpg', 'jpeg', 'gif', 'jfif', 'svg']
    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)

    return result



print(filter(files_and_folders))


        







window.resize(600,550)
window.setLayout(horisontal_2)
window.show()
app.exec_()







