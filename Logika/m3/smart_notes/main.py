from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json
import os

def writeToFile():
    with open('m3\\smart_notes\\notes.json','w',encoding='utf8') as file:
        json.dump(notes, file,ensure_ascii=False, sort_keys=True,indent=4)


app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна

text_editor = QTextEdit()
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()
list_widget_2 = QListWidget()
input_dialog = QLineEdit()
input_dialog.setPlaceholderText('Введіть тег...')

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
    global key
    key = list_widget_1.selectedItems()[0].text()
    
    list_widget_2.clear()
    
    list_widget_2.addItems(notes[key]['теги'])
def delete_notes():
    if list_widget_1.currentItem():
        if key in notes:
            notes.pop(key)
            
            text_editor.clear()
            list_widget_2.clear()
            list_widget_1.clear()
            list_widget_1.addItems(notes)
            writeToFile()

def add_notes():
    note_name,ok = QInputDialog.getText(window,'Додати замітку',"Назва замітки")
    if note_name and ok:
        list_widget_1.addItem(note_name)
        notes[note_name] = {"текст":"","теги":[]}
    writeToFile()

def save_notes():
    
    if list_widget_1.currentItem():
        key = list_widget_1.currentItem().text()
        notes[key]['текст'] = text_editor.toPlainText()
        writeToFile()




save_note.clicked.connect(save_notes)
make_note.clicked.connect(add_notes)
delete_note.clicked.connect(delete_notes)
list_widget_1.itemClicked.connect(show_notes)




with open('m3\\smart_notes\\notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

list_widget_1.addItems(notes)





window.setLayout(layout_notes)
window.resize(main_width,main_height)
window.show()
app.exec_()