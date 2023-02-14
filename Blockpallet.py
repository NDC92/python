import sys
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QMessageBox)
import pyautogui
import time

def program_blockpallet():
    pyautogui.PAUSE = 0.5

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = QWidget()
    window.setWindowTitle("Block pallet")

    layout = QHBoxLayout()

    password_entry = QLineEdit(parent=window)
    password_entry.setEchoMode(QLineEdit.Password)
    password_entry.move(20, 80)

    vitripicking = QLabel("Vi Tri Picking")
    vitripicking.move(100, 100)

    prvniPalet = (420, 285)
    cisloPalet = (232, 181)
    status = (465, 530)
    vyber = (821, 287)
    tridaStavu = (74, 467)

    def adjust_text_height():
        lines = len(vitripicking.get("1.0", "end").split("\n"))
        vitripicking.config(height=lines)
        vitripicking.bind("<Key>", adjust_text_height)

    def get_code_palet():
        text_input = str(codepallet.toPlainText()).strip()
        data_code_palet = text_input.split("\n")
        return data_code_palet

    def block_palet(data_code_palet):
        for i in data_code_palet:
            pyautogui.tripleClick(cisloPalet, duration=0.7)
            # pyautogui.press("%")
            pyautogui.typewrite(str(i))
            pyautogui.hotkey('alt', 't')
            pyautogui.click(prvniPalet, duration=0.7)
            pyautogui.moveTo(status, duration=0.7)
            pyautogui.click(status, duration=0.7)
            pyautogui.click(status, duration=0.7)
            pyautogui.write('cuong')
            pyautogui.hotkey('enter')
            pyautogui.click(vyber)
            pyautogui.hotkey('alt', 'w')
            pyautogui.click(tridaStavu)
            pyautogui.write('RET')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.write('FOURN')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('tab')
            pyautogui.hotkey('alt', 'c')
            pyautogui.hotkey('enter')
            time.sleep(1)

    def multiple_commands():
        int_data = get_code_palet()
        block_palet(int_data)

    codepallet = QTextEdit(parent=window)
    codepallet.insertPlainText("Insert code pallet here")
    codepallet.show()
    layout.addWidget(codepallet)

    button = QPushButton("Block Pallet", parent=window)
    button.clicked.connect(multiple_commands)
    button.show()
    layout.addWidget(button)

    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    import sys
    program_blockpallet()


