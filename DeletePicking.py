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
window.setWindowTitle("Xoa Picking")

layout = QHBoxLayout()

password_entry = QLineEdit(parent=window)
password_entry.setEchoMode(QLineEdit.Password)
password_entry.move(20, 80)


vitripicking = QLabel("Vi Tri Picking")
vitripicking.move(100, 100)


zbozi = (232, 129)


def adjust_text_height():
    lines = len(vitripicking.get("1.0", "end").split("\n"))
    vitripicking.config(height=lines)
    vitripicking.bind("<Key>", adjust_text_height)


def get_mnb():
    text_input = str(mnb.toPlainText()).strip()
    data_mnb = text_input.split("\n")
    return data_mnb


def delete_picking(data_mnb):
    for i in data_mnb:
        pyautogui.doubleClick(zbozi[0], zbozi[1])
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(str(i))
        pyautogui.hotkey('tab')
        pyautogui.typewrite('00')
        pyautogui.hotkey('tab')
        pyautogui.typewrite('000')
        pyautogui.hotkey('alt', 't')
        pyautogui.click(343, 188, duration=0.5)
        pyautogui.hotkey('alt', 'z')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
        time.sleep(0.5)


def multiple_commands():
    int_data = get_mnb()
    delete_picking(int_data)




mnb = QTextEdit(parent=window)
mnb.insertPlainText("Insert picking position here")
mnb.show()
layout.addWidget(mnb)


button = QPushButton("Delete Picking", parent=window)
button.clicked.connect(multiple_commands)
button.show()
layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
