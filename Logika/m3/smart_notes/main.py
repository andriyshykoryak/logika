from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json
app = QApplication([])
window = QWidget()

text_editor = QTextEdit()
text_editor.setText('Текст')
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(text_editor)


list_widget_1 = QListWidget()
list_widget_2 = QListWidget()

make_note = QPushButton()
make_note.setText('Створити замітку')
delete_note = QPushButton()
delete_note.setText('Видалити замітку')
make_note.setText('Створити замітку')
save_note = QPushButton()
save_note.setText('зберегти замітку')

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)



col2.addWidget(QLabel('Список питань'))
col2.addWidget(list_widget_1)
col2.addWidget(save_note)
col2.addWidget(QLabel('Список тегів'))
col2.addWidget(list_widget_2)
col2.addLayout(row1)



layout_notes = QHBoxLayout()
layout_notes.addLayout(col1,stretch=2)
layout_notes.addLayout(col2)
def show_notes():
    key = list_widget_1.selectedItems()[0].text()
    text_editor.setText(notes[key]['текст'])

list_widget_1.itemClicked.connect(show_notes)

with open('notes.json','r',encoding='utf8') as file:
    notes = json.load(file)

list_widget_1.addItems(notes)


window.setLayout(layout_notes)
window.show()
app.exec_()