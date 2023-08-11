from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget, QLabel,QPushButton, QVBoxLayout,QRadioButton,QMessageBox,QHBoxLayout

app = QApplication([])
main_window = QWidget()


question = QLabel('У якому році створили YouTube')
ans1 = QRadioButton('2005')
ans2 = QRadioButton('2010')
ans3 = QRadioButton('2015')
ans4 = QRadioButton('2020')
line = QVBoxLayout()
line_gorisontal1 = QHBoxLayout()
line_gorisontal2 = QHBoxLayout()
line_gorisontal3 = QHBoxLayout()
line_gorisontal1.addWidget(question)


line_gorisontal2.addWidget(ans1)
line_gorisontal2.addWidget(ans2)


line_gorisontal3.addWidget(ans3)
line_gorisontal3.addWidget(ans4)



line.addLayout(line_gorisontal1)
line.addLayout(line_gorisontal2)
line.addLayout(line_gorisontal3)

main_window.setLayout(line)

main_window.show()
app.exec_()