import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox)
import pyautogui
import time

pyautogui.PAUSE = 0.5

app = QApplication(sys.argv)
app.setStyle("Fusion")
window = QWidget()
window.setWindowTitle("Tao Picking")

layout = QHBoxLayout()


vitripicking = QLabel("Vi Tri Picking")
vitripicking.move(100, 100)

adresabudouci = (616, 139)
zbozi = (93, 140)



def vlozPrvniRadek():
 pyautogui.click(zbozi)
 pyautogui.hotkey('alt', 'w')
 pyautogui.typewrite('cuong')
 pyautogui.hotkey('enter')
 pyautogui.click(zbozi)



def vlozDalsiRadek():
 pyautogui.click(712, 431)
 pyautogui.hotkey('alt', 'w')
 pyautogui.click(zbozi)





def vlozDatum():
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('F5')
 pyautogui.hotkey('enter')



def vlozPripravy() :
 pyautogui.hotkey('tab')
 pyautogui.typewrite('00')
 pyautogui.hotkey('tab')
 pyautogui.typewrite('000')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')
 pyautogui.hotkey('tab')



def adjust_text_height():
    lines = len(vitripicking.get("1.0", "end").split("\n"))
    vitripicking.config(height=lines)
    vitripicking.bind("<Key>", adjust_text_height)


def get_vitripicking():
    text_input = str(vitripicking.toPlainText()).strip()
    data_vitripicking = text_input.split("\n")
    return data_vitripicking


def get_mnb():
    text_input = str(mnb.toPlainText()).strip()
    data_mnb = text_input.split("\n")
    return data_mnb


def change_picking(data_vitripicking, data_mnb):
    for i in data_vitripicking:
        for j in data_mnb:
            pyautogui.write(str(j))
            vlozPripravy()
            pyautogui.write(str(i))
            vlozDatum()
            vlozDalsiRadek()


def multiple_commands():
    vlozPrvniRadek()
    int_data_pickingposition = get_vitripicking()
    int_data_mnb = get_mnb()
    change_picking(int_data_pickingposition, int_data_mnb)



vitripicking = QTextEdit(parent=window)
vitripicking.insertPlainText("Insert picking position here")
vitripicking.show()
layout.addWidget(vitripicking)


mnb = QTextEdit(parent=window)
mnb.insertPlainText("Insert product code here")
mnb.show()
layout.addWidget(mnb)

button = QPushButton("Change Picking", parent=window)
button.clicked.connect(multiple_commands)
button.show()
layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
