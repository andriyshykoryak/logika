''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox,QListView)
from memo___edit_layout import layout_form



list_questions = QListView()

wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Нове питання')
btn_add.setStyleSheet('''
    QPushButton {
        background-color: white;
    }
    QPushButton:hover {
        background-color: grey;
    }
''')
btn_delete = QPushButton('Видалити питання')
btn_delete.setStyleSheet('''
    QPushButton {
        background-color: yellow;
    }
    QPushButton:hover {
        background-color: darkorange;
    }
''')
btn_start = QPushButton('Почати тренування')
btn_start.setStyleSheet('''
    QPushButton {
        background-color: grey;
    }
    QPushButton:hover {
        background-color: dark;
    }
''')
main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_delete)

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_add)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)


main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start,stretch=2)
main_line2.addStretch(1)


layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)






















