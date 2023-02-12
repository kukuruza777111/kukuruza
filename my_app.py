from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import randint

app = QApplication([])
window =QWidget()


main_layout = QHBoxLayout()
line = QVBoxLayout()
line_buttons = QHBoxLayout()



button_add = QPushButton("Добавить")
button_del = QPushButton("Удалить")
button_save =QPushButton("Сохранить")



line_buttons.addWidget(button_add)
line_buttons.addWidget(button_del)
line_buttons.addWidget(button_save)



contries_info = QTextEdit
line_addWidget(contries_info)
line.addLayout(line_buttons)



contries_list = QListWindget()
main_layout.addWindget(contries_list)
main_layout.addLayout(line)



contries_edit =QListwidget()
contries_edit.setPlaseholgerTexst('Введите страну')
line.addWindget(contries_edit)



with open('contries.json','r') as fille:
    contries = json.load(fille)
    for countyry in contries
    contries_list.addItem(contriry)


def info_country():
    with open('coutries,json', 'r') as file:
        countries = json.load(file)
    country = countries_list.selectedItems()[0].text()
    countries_info.setText(countries[country])

def add_country():
    country = countries_edit.text()
    with open('countries.json', 'r') as file:
        countries = json.load(file)
    countries[country] = ''
    with open('countries.json', 'w') as file:
        countries = json.dump(count,file)
    countries_info.clear()
    countries_list.addItem(country)

def edit_country():
    country = ''
    if countries_list.selectedItems()[0].text()
         country = countries_list.selectedItems()[0].text()
    with open('countries.json', 'r') as file:
        countries = json.load(file)
    countries[country] = countries_info.to_PlainText()
    with open('countries.json', 'w') as file:
        countries = json.dump(countries, file)
    countries_info.clear()
    countries_list.itemClicked.connect(info_country)
 button_del.clicked.connect(del_country)
      button_save.clicked.connect(edit_country)

window.setLayout(main_layout)
window.show()
app.exec()


   
