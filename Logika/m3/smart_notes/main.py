from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence

import json
import os

def writeToFile():
    with open('m3\\smart_notes\\notes.json','w',encoding='utf8') as file:
        json.dump(notes, file,ensure_ascii=False, sort_keys=True,indent=4)


app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна

text_editor = QTextEdit()
text_editor.setStyleSheet('''
        background-color:#80FF00;

''')
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()
list_widget_1.setStyleSheet('''
        background-color:#CCFFFF;


''')
list_widget_2 = QListWidget()
list_widget_2.setStyleSheet('''
        background-color:#9445B6;


''')
text_searcher = QLineEdit()
text_searcher.setPlaceholderText('Введіть текст...')
input_dialog = QLineEdit()
input_dialog.setStyleSheet('''
        background-color:#FF3333;


''')
input_dialog.setPlaceholderText('Введіть тег...')

# Створення кнопок
make_note = QPushButton()
make_note.setStyleSheet('''
    QPushButton {
        background-color: purple;
    }
    QPushButton:hover {
        background-color: darkpurple;
    }
''')
make_note.setText('Створити замітку')
delete_note = QPushButton()
delete_note.setStyleSheet('''
    QPushButton {
        background-color: blue;
    }
    QPushButton:hover {
        background-color: darkblue;
    }
''')
delete_note.setText('Видалити замітку')
save_note = QPushButton()
save_note.setStyleSheet('''
    QPushButton {
        background-color: grey;
    }
    QPushButton:hover {
        background-color: white;
    }
''')
save_note.setText('Зберегти замітку')


#створення нижніх кнопок
search_for_text = QPushButton()
search_for_text.setText('Шукати замітку за текстом')
add_to_note = QPushButton()
add_to_note.setStyleSheet('''
    QPushButton {
        background-color: white;
    }
    QPushButton:hover {
        background-color: gray;
    }
''')
add_to_note.setText('Додати до замітки')
unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('''
    QPushButton {
        background-color: red;
    }
    QPushButton:hover {
        background-color: darkred;
    }
''')
unpin_to_note.setText('Відкріпити від замітки')
search_for_note = QPushButton()
search_for_note.setStyleSheet('''
    QPushButton {
        background-color: green;
    }
    QPushButton:hover {
        background-color: darkgreen;
    }
''')
search_for_note.setText('Шукати замітки за тегом')

export_as_txt = QPushButton()
export_as_txt.setText('Конвертувати до txt-формату')
export_as_txt.setStyleSheet('''
    QPushButton {
        background-color: orange;
    }
    QPushButton:hover {
        background-color: darkorange;
    }
''')
action_exit = QAction("Exit", window)
action_exit.setShortcut(QKeySequence("Ctrl+W"))

change_theme_btn = QPushButton()
change_theme_btn.setText(f'Змінити тему на чорну')
change_theme_btn1 = QPushButton()
change_theme_btn1.setText(f'Змінити тему на білу')

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
col2.addWidget(text_searcher)
col2.addLayout(row2)
col2.addWidget(search_for_note)
col2.addWidget(search_for_text)
col2.addWidget(export_as_txt)
col2.addWidget(change_theme_btn)
col2.addWidget(change_theme_btn1)



layout_notes = QHBoxLayout()
layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2)



def change_theme_to_dark():

    window.setStyleSheet(' background-color:black;color:white;font-size:20px; border: 1px solid white;')
    text_editor.setStyleSheet('background-color:black;color:white;')
    list_widget_1.setStyleSheet(' background-color:black;color:white;')
    list_widget_2.setStyleSheet(' background-color:black;color:white;')
    unpin_to_note.setStyleSheet(' background-color:black;color:white;')
    add_to_note.setStyleSheet(' background-color:black;color:white;')
    make_note.setStyleSheet(' background-color:black;color:white;')
    delete_note.setStyleSheet(' background-color:black;color:white;')
    search_for_note.setStyleSheet(' background-color:black;color:white;')
    search_for_text.setStyleSheet(' background-color:black;color:white;')
    input_dialog.setStyleSheet(' background-color:black;color:white;')
    export_as_txt.setStyleSheet(' background-color:black;color:white;')
    save_note.setStyleSheet(' background-color:black;color:white;')


def change_theme_to_light():

    window.setStyleSheet(' background-color:white;color:black;font-size:20px; border: 1px solid black;')
    text_editor.setStyleSheet('background-color:white;color:black;')
    list_widget_1.setStyleSheet(' background-color:white;color:black;')
    list_widget_2.setStyleSheet('background-color:white;color:black;')
    unpin_to_note.setStyleSheet('background-color:white;color:black;')
    add_to_note.setStyleSheet('background-color:white;color:black;')
    make_note.setStyleSheet('background-color:white;color:black;')
    delete_note.setStyleSheet('background-color:white;color:black;')
    search_for_note.setStyleSheet('background-color:white;color:black;')
    search_for_text.setStyleSheet('background-color:white;color:black;')
    input_dialog.setStyleSheet('background-color:white;color:black;')
    export_as_txt.setStyleSheet('background-color:white;color:black;')
    save_note.setStyleSheet('background-color:white;color:black;')


def exitt():
    app.exit()

def show_notes():
    global key
    key = list_widget_1.selectedItems()[0].text()
    
    list_widget_2.clear()
    text_editor.setText(notes[key]['текст'])
    
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
def add_tag():
    if key in notes:
        tag_name, ok = QInputDialog.getText(window, 'Додати тег', 'Назва тегу')
        if tag_name and ok:
            list_widget_2.addItem(tag_name)  
            notes[key]["теги"].append(tag_name)  
            writeToFile() 
     
def delete_tag():
  
    
    if key in notes:
        current_item = list_widget_2.currentItem()
        if current_item:
            tag_name = current_item.text()
            notes[key]["теги"].remove(tag_name)
            list_widget_2.takeItem(list_widget_2.row(current_item)) 
            writeToFile()  

def search_note():
    tag = input_dialog.text()
    if search_for_note.text() == 'Шукати замітки за тегом':
            filtered_notes = {}
            for key in notes:
                if tag in notes[key]['теги']:
                    filtered_notes[key] = notes[key]
            search_for_note.setText('Скинути пошук')

            list_widget_1.clear()
            list_widget_1.addItems(filtered_notes)
            list_widget_2.clear()
            text_editor.clear()


    elif search_for_note.text() == 'Скинути пошук':
            search_for_note.setText('Шукати замітки за тегом')
            list_widget_1.clear()
            list_widget_1.addItems(notes)
            list_widget_2.clear()
            text_editor.clear()
            input_dialog.clear()
def search_note_for_text():
    text_to_search = text_searcher.text().strip()
    if search_for_text.text() == 'Шукати замітку за текстом':
        filtered_notes = {}
        for key, note_data in notes.items():
            if text_to_search in note_data['текст']:
                filtered_notes[key] = note_data
        search_for_text.setText('Скинути пошук')

        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes.keys())
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_text.text() == 'Скинути пошук':
        search_for_text.setText('Шукати замітку за текстом')
        list_widget_1.clear()
        list_widget_1.addItems(notes.keys())
        list_widget_2.clear()
        text_editor.clear()
def export_to_txt():
    if list_widget_1.currentItem():
        key = list_widget_1.currentItem().text()
        note_data = notes[key]
        note_text = note_data['текст']
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(window, "Зберегти як .txt", "", "Text Files (*.txt)")

        if file_path:
            with open(file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(note_text)






change_theme_btn.clicked.connect(change_theme_to_dark)
change_theme_btn1.clicked.connect(change_theme_to_light)

action_exit.triggered.connect(exitt)
window.addAction(action_exit)

export_as_txt.clicked.connect(export_to_txt)
        

search_for_text.clicked.connect(search_note_for_text)

search_for_text.clicked.connect(search_note_for_text)

search_for_text.clicked.connect(search_note_for_text)
unpin_to_note.clicked.connect(delete_tag)
search_for_note.clicked.connect(search_note)
add_to_note.clicked.connect(add_tag)
save_note.clicked.connect(save_notes)
make_note.clicked.connect(add_notes)
delete_note.clicked.connect(delete_notes)
list_widget_1.itemClicked.connect(show_notes)




with open('m3\\smart_notes\\notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

list_widget_1.addItems(notes)






window.setStyleSheet('background-color:yellow;font-size:20px')
window.setLayout(layout_notes)
window.resize(main_width,main_height)
window.show()
app.exec_()