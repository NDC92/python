from Blockpallet import program_blockpallet
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout, QWidget

import sys



class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

        # Vytvořte radio buttony
        self.option1 = QRadioButton("Tạo Picking")
        self.option2 = QRadioButton("Xóa Picking")
        self.option3 = QRadioButton("Chuyển Picking")
        self.option4 = QRadioButton("Tạo Master Data")
        self.option5 = QRadioButton("Block pallet 20R")

        # Vytvořte layout pro radio buttony
        options_layout = QVBoxLayout()
        options_layout.addWidget(self.option1)
        options_layout.addWidget(self.option2)
        options_layout.addWidget(self.option3)
        options_layout.addWidget(self.option4)
        options_layout.addWidget(self.option5)

        self.action_button = QPushButton("Proveď akci")
        self.action_button.clicked.connect(self.perform_action)

        #Vytvořte hlavní layout a přidejte do něj heslo a radio buttony
        main_layout = QVBoxLayout()
        main_layout.addLayout(options_layout)
        main_layout.addWidget(self.action_button)

        #Nastavte hlavní layout okna
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def perform_action(self):
        if self.option1.isChecked():
            program_zkouska()
            pass
        elif self.option2.isChecked():
            # Proveď akci pro možnost 2
            pass
        elif self.option3.isChecked():
             # Proveď akci pro možnost 3
            pass
        elif self.option4.isChecked():
            # Proveď akci pro možnost 4
            pass
        elif self.option5.isChecked():
            program_blockpallet()
            pass



class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        # Definujte správné heslo
        self.password = "mypassword"

        # Vytvořte widget pro zadání hesla
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Vytvořte widget pro zobrazení chybového hlášení
        self.error_label = QLabel("")

        self.login_button = QPushButton("Login")

        self.setCentralWidget(self.login_button)

        self.login_button.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

        # Vytvořte layout pro heslo a tlačítko
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.login_button)

        # Vytvořte hlavní layout a přidejte do něj heslo a radio buttony
        main_layout = QVBoxLayout()
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.error_label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


    def on_pushButton_clicked(self):
        password = self.password_input.text()
        if password == self.password:
            self.error_label.setText("")
            self.dialog.show()
        else:
            self.error_label.setText("Špatné heslo")



def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main = First()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()