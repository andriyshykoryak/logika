from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна

text_editor = QTextEdit()
text_editor.setText('Текст')

list_widget_1 = QListWidget()
list_widget_2 = QListWidget()
input_dialog = QLineEdit()

# Створення кнопок
make_note = QPushButton()
make_note.setText('Створити замітку')
delete_note = QPushButton()
delete_note.setText('Видалити замітку')
save_note = QPushButton()
save_note.setText('Зберегти замітку')


#створення нижніх кнопок
add_to_note = QPushButton()
add_to_note.setText('Додати до замітки')
unpin_to_note = QPushButton()
unpin_to_note.setText('Відкріпити від замітки')
search_for_note = QPushButton()
search_for_note.setText('Шукати замітки за тегом')




row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)
row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel('Список питань'))
col2.addWidget(list_widget_1)
col2.addLayout(row1) 
col2.addWidget(save_note)  
col2.addWidget(QLabel('Список тегів'))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addLayout(row2)
col2.addWidget(search_for_note)

layout_notes = QHBoxLayout()
layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2)

def show_notes():
    key = list_widget_1.selectedItems()[0].text()
    text_editor.setText(notes[key]['текст'])

list_widget_1.itemClicked.connect(show_notes)

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

list_widget_1.addItems(notes)

window.setLayout(layout_notes)
window.resize(main_width,main_height)
window.show()
app.exec_()