from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel,QPushButton, QVBoxLayout,QRadioButton,QMessageBox,QHBoxLayout
from PyQt5.QtGui import QPixmap,QIcon

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Crazy people опитування')
pixmap = QPixmap('m2\\u2\\CrazyPeopleдод\\icon.png')
main_window.setWindowIcon(QIcon(pixmap))


question = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')
ans1 = QRadioButton('TheBrianMaps')
ans2 = QRadioButton('Рет і Лінк')
ans3 = QRadioButton('SlivkiShow')
ans4 = QRadioButton('PewDiePie')
ans5 = QRadioButton('Mister Max')
ans6 = QRadioButton('EeOneGuy')
line = QVBoxLayout()
line_gorisontal1 = QHBoxLayout()
line_gorisontal2 = QHBoxLayout()
line_gorisontal3 = QHBoxLayout()
line_gorisontal4 = QHBoxLayout()
line_gorisontal5 = QHBoxLayout()
line_gorisontal1.addWidget(question,alignment=Qt.AlignCenter)


line_gorisontal2.addWidget(ans1,alignment=Qt.AlignCenter)
line_gorisontal2.addWidget(ans2,alignment=Qt.AlignCenter)

line_gorisontal2.addWidget(ans5,alignment=Qt.AlignCenter)


line_gorisontal3.addWidget(ans3,alignment=Qt.AlignCenter)
line_gorisontal3.addWidget(ans4,alignment=Qt.AlignCenter)

line_gorisontal3.addWidget(ans6,alignment=Qt.AlignCenter)



line.addLayout(line_gorisontal1)
line.addLayout(line_gorisontal2)
line.addLayout(line_gorisontal3)
def win():
    victory_window = QMessageBox()
    pixmap = QPixmap('m2\\u2\\CrazyPeopleдод\\icon.png')
    victory_window.setWindowIcon(QIcon(pixmap))
    victory_window.setStyleSheet('background-color: green;font-size:30px;color: white;')
    victory_window.setWindowTitle('Виграш')
    victory_window.setText('Ви виграли зустріч з творцями каналу!')
    victory_window.exec_()
def lose():

    lose_window = QMessageBox()
    pixmap = QPixmap('m2\\u2\\CrazyPeopleдод\\icon.png')
    lose_window.setWindowIcon(QIcon(pixmap))
    lose_window.setStyleSheet('background-color: red;font-size:30px;color: white;')
    lose_window.setWindowTitle('Програш')
    lose_window.setText('Пощастить іншим разом!')
    lose_window.exec_()

main_window.setStyleSheet('background-color: red;font-size:20px;color: white;')
ans1.clicked.connect(lose)
ans1.setStyleSheet('background-color: green;font-size:20px;')
ans2.clicked.connect(lose)
ans2.setStyleSheet('background-color: blue;font-size:20px;')
ans3.clicked.connect(lose)
ans3.setStyleSheet('background-color: orange;font-size:20px;')
ans4.clicked.connect(win)
ans4.setStyleSheet('background-color: gray;font-size:20px;')
ans5.clicked.connect(lose)
ans5.setStyleSheet('background-color: purple;font-size:20px;')
ans6.clicked.connect(lose)
ans6.setStyleSheet('background-color: brown;font-size:20px;')
main_window.setLayout(line)

main_window.show()
app.exec_()