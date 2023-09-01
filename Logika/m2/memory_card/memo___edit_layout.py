''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong_Answer1 = QLineEdit('')
txt_Wrong_Answer2 = QLineEdit('')
txt_Wrong_Answer3 = QLineEdit('')
layout_form = QFormLayout()
layout_form.addRow('Питання',txt_Question)
layout_form.addRow('Правильна відповідь',txt_Answer)
layout_form.addRow('НЕ Правильна відповідь 1',txt_Wrong_Answer1)
layout_form.addRow('НЕ Правильна відповідь 2',txt_Wrong_Answer2)
layout_form.addRow('НЕ Правильна відповідь 3',txt_Wrong_Answer3)