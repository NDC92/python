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

password_entry = QLineEdit(parent=window)
password_entry.setEchoMode(QLineEdit.Password)
password_entry.move(20, 80)
"""
def verify_password():
    if password_entry.text() == "mojeprogramy":
        vitripicking = QTextEdit(parent=window)
        vitripicking.insertPlainText("Insert internal product code here")
        vitripicking.show()
        layout.addWidget(vitripicking)
        button = QPushButton("Delete Picking", parent=window)
        button.clicked.connect(multiple_commands)
        button.show()
        layout.addWidget(button)
    else:
        message_box = QMessageBox()
        message_box.setWindowTitle("Error")
        message_box.setText("Heslo není správné.")
        message_box.exec_()
        window.close()

#password_label = QLabel("Heslo:", parent=window)
#password_label.move(60, 120)

verify_button = QPushButton("Ověřit", parent=window)
verify_button.clicked.connect(verify_password)
verify_button.move(50, 30)

layout.addWidget(password_entry)
#layout.addWidget(password_label)
layout.addWidget(verify_button)
"""

vitripicking = QLabel("Vi Tri Picking")
vitripicking.move(100, 100)

zonaPripravy = (250, 142)
tridaPripravy = (261, 173)
adresaPripr = (658, 228)
radekVt = (403, 310)
artikl = (159, 150)
zbozi = (232, 129)


def vlozZbozi():
    pyautogui.hotkey('tab')
    pyautogui.typewrite('00')
    pyautogui.hotkey('tab')
    pyautogui.typewrite('000')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.typewrite('1')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.typewrite('00000')
    time.sleep(2)
    pyautogui.hotkey('alt', 'c')
    time.sleep(3)
    pyautogui.hotkey('enter')
    time.sleep(3)


def vlozPripravy():
    pyautogui.click(zonaPripravy, duration=0.5)
    pyautogui.typewrite('VC1')
    pyautogui.hotkey('enter')
    pyautogui.doubleClick(tridaPripravy, duration=0.5)
    pyautogui.hotkey('enter')


def adjust_text_height():
    lines = len(vitripicking.get("1.0", "end").split("\n"))
    vitripicking.config(height=lines)
    vitripicking.bind("<Key>", adjust_text_height)


def get_vitripicking():
    text_input = str(vitripicking.toPlainText()).strip()
    data_vitripicking = [line.strip() for line in text_input.split("\n") if line.strip()]
    return data_vitripicking

def get_pickingunit():
    text_input = str(pickingunit.toPlainText()).strip()
    data_pickingunit = [line.strip() for line in text_input.split("\n") if line.strip()]
    return data_pickingunit

def get_mnb():
    text_input = str(mnb.toPlainText()).strip()
    data_mnb = [line.strip() for line in text_input.split("\n") if line.strip()]
    return data_mnb


def make_picking(data_vitripicking, data_pickingunit, data_mnb):
    for i in data_vitripicking:
        for j in data_pickingunit:
            for k in data_mnb:
                vlozPripravy()
                pyautogui.doubleClick(zbozi[0], zbozi[1])
                pyautogui.tripleClick(adresaPripr, duration=0.5)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.write(str(i))
                pyautogui.hotkey('alt', 't')
                time.sleep(3)
                pyautogui.click(radekVt, duration=0.5)
                pyautogui.doubleClick(radekVt)
                pyautogui.write('cuong')
                pyautogui.hotkey('enter')
                pyautogui.hotkey('tab')
                pyautogui.write('200')
                pyautogui.hotkey('tab')
                pyautogui.write(str(k))
                pyautogui.hotkey('tab')
                pyautogui.typewrite('00')
                pyautogui.hotkey('tab')
                pyautogui.typewrite('000')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.typewrite(str(j))
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.hotkey('tab')
                pyautogui.typewrite('00000')
                time.sleep(2)
                pyautogui.hotkey('alt', 'c')
                time.sleep(2)
                pyautogui.hotkey('enter')
                time.sleep(2)
                time.sleep(0.5)



def multiple_commands():
    int_data_pickingposition = get_vitripicking()
    int_data_pickingunit = get_pickingunit()
    int_data_mnb = get_mnb()
    make_picking(int_data_pickingposition, int_data_pickingunit, int_data_mnb)




vitripicking = QTextEdit(parent=window)
vitripicking.insertPlainText("Insert picking position here")
vitripicking.show()
layout.addWidget(vitripicking)

pickingunit = QTextEdit(parent=window)
pickingunit.insertPlainText("Insert picking unit here")
pickingunit.show()
layout.addWidget(pickingunit)

mnb = QTextEdit(parent=window)
mnb.insertPlainText("Insert product code here")
mnb.show()
layout.addWidget(mnb)

button = QPushButton("Make Picking", parent=window)
button.clicked.connect(multiple_commands)
button.show()
layout.addWidget(button)



window.setLayout(layout)
window.show()
sys.exit(app.exec())
