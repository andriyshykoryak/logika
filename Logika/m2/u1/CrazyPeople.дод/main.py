from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel,QPushButton, QVBoxLayout
from random import randint
app = QApplication([]) 

main_window = QWidget()


text = QLabel('Натисни, щоб дізнатись переможця')
winner = QLabel('?')
winner1 = QLabel('?')
button = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(winner,alignment=Qt.AlignCenter)
line.addWidget(winner1,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)

def win():
    ran = randint(1,100)
    ran1 = randint(1,100)
    if ran == ran1:
        asi = QLabel('Ти виграв')
        line.addWidget(asi,alignment=Qt.AlignCenter)
    else:
        asi = QLabel('Ти Програв')
        line.addWidget(asi,alignment=Qt.AlignCenter)
        
        

    winner.setText(str(ran))
    winner1.setText(str(ran1))

button.clicked.connect(win)


main_window.setLayout(line)

main_window.show()

app.exec_()
