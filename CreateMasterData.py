import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox)
import pyautogui
import time

pyautogui.PAUSE = 1

app = QApplication(sys.argv)
app.setStyle("Fusion")
window = QWidget()
window.setWindowTitle("Tao Master Data")

layout = QHBoxLayout()

vitripicking = QLabel("Vi Tri Picking")
vitripicking.move(100, 100)


zbozi = (768, 208)
inportButton = (254, 927)
xacNhan = (739, 596)
kiemTra = (768, 400)
sua = (767,474)


def adjust_text_height():
    lines = len(vitripicking.get("1.0", "end").split("\n"))
    vitripicking.config(height=lines)
    vitripicking.bind("<Key>", adjust_text_height)


def get_mnb():
    text_input = str(mnb.toPlainText()).strip()
    data_mnb = text_input.split("\n")
    return data_mnb


def make_master_data(data_mnb):
    for i in data_mnb:
        pyautogui.click(zbozi)
        pyautogui.typewrite(str(i))
        pyautogui.hotkey('enter')
        pyautogui.click(inportButton)
        time.sleep(2)
        pyautogui.click(xacNhan)
        pyautogui.click(kiemTra)
        pyautogui.click(sua)
        pyautogui.click(xacNhan)
        time.sleep(2)
        pyautogui.hotkey('enter')


def multiple_commands():
    int_data = get_mnb()
    make_master_data(int_data)




mnb = QTextEdit(parent=window)
mnb.insertPlainText("Insert picking position here")
mnb.show()
layout.addWidget(mnb)


button = QPushButton("Make Master Data", parent=window)
button.clicked.connect(multiple_commands)
button.show()
layout.addWidget(button)

window.setLayout(layout)

window.show()

sys.exit(app.exec())
