''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox,QMessageBox,)
from PyQt5.QtGui import QPixmap,QIcon

app = QApplication([])

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.


btn_OK = QPushButton('Відповісти')
btn_OK.setStyleSheet('''
    QPushButton {
        background-color: red;
    }
    QPushButton:hover {
        background-color: darkred;
    }
''')



btn_sleep = QPushButton('Відпочити')
btn_sleep.setStyleSheet('''
    QPushButton {
        background-color: green;
    }
    QPushButton:hover {
        background-color: darkgreen;
    }
''')


btn_menu = QPushButton('Меню')
btn_menu.setStyleSheet( '''
    QPushButton {
        background-color: orange;
    }
    QPushButton:hover {
        background-color: darkorange;
    }
''')

question = QLabel('')

box_minutes = QSpinBox()

box_minutes.setStyleSheet('background-color:green')

box_minutes.setValue(5)



radio_group_box = QGroupBox('Варіанти відповідей')

radiogrup = QButtonGroup()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

ans1 = QRadioButton('')
ans2 = QRadioButton('')
ans3 = QRadioButton('')
ans4 = QRadioButton('')

radiogrup.addButton(ans1)
radiogrup.addButton(ans2)
radiogrup.addButton(ans3)
radiogrup.addButton(ans4)

layout_ans2.addWidget(ans1)
layout_ans2.addWidget(ans2)
layout_ans3.addWidget(ans3)
layout_ans3.addWidget(ans4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_group_box.setLayout(layout_ans1)

AnsGroupBox = QGroupBox()

lb_result = QLabel('')
lb_correct = QLabel('')
layout_res = QVBoxLayout()


layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_correct,alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_card  = QVBoxLayout()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()

layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(question,alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

layout_line3.addWidget(radio_group_box)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK)
layout_line4.addStretch(1)

layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)
sleep_button = QPushButton('Закінчити відпочинок')
sleep_layout = QVBoxLayout()
sleep_layout.addWidget(sleep_button)

timer_window = QWidget()
timer_window.setWindowTitle('Відпочинок')
pixmap = QPixmap('m2\\memory_card\\logo.png')
timer_window.setWindowIcon(QIcon(pixmap))
timer_window.setStyleSheet('background-color:yellow;font-size:20px;')
timer_label = QLabel('Відпочинок')
endsllep = QPushButton('Завершити відпочинок')
endsllep.setStyleSheet('''
    QPushButton {
        background-color: green;
    }
    QPushButton:hover {
        background-color: darkgreen;
    }
''')

timer_layout = QVBoxLayout()
timer_layout.addWidget(timer_label)
timer_layout.addWidget(endsllep)
timer_window.setLayout(timer_layout)




def show_result():
    radio_group_box.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання')
    
def show_question():
    radio_group_box.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    radiogrup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    radiogrup.setExclusive(True)




