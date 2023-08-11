from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel,QPushButton, QVBoxLayout,QRadioButton,QMessageBox,QHBoxLayout

app = QApplication([])
main_window = QWidget()


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
    victory_window.setText('Ви виграли зустріч з творцями каналу!')
    victory_window.exec_()
def lose():
    lose_window = QMessageBox()
    lose_window.setText('Пощастить іншим разом!')
    lose_window.exec_()

ans1.clicked.connect(lose)
ans2.clicked.connect(lose)
ans3.clicked.connect(lose)
ans4.clicked.connect(win)
ans5.clicked.connect(lose)
ans6.clicked.connect(lose)
main_window.setLayout(line)

main_window.show()
app.exec_()