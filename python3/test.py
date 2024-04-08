import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel
import subprocess

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ansible GUI')
        
        self.playbook_lineedit = QLineEdit(self)
        self.playbook_lineedit.setPlaceholderText('Путь к playbook')
        
        self.vars_lineedit = QLineEdit(self)
        self.vars_lineedit.setPlaceholderText('Переменные vars в формате key=value')

        self.run_button = QPushButton('Запустить', self)
        self.run_button.clicked.connect(self.run_playbook)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Путь к playbook:'))
        layout.addWidget(self.playbook_lineedit)
        layout.addWidget(QLabel('Переменные vars:'))
        layout.addWidget(self.vars_lineedit)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def run_playbook(self):
        playbook_path = self.playbook_lineedit.text()
        vars_str = self.vars_lineedit.text()

        command = f'ansible-playbook {playbook_path}'
        if vars_str:
            command += f' --extra-vars "{vars_str}"'

        process = subprocess.Popen(command, shell=True)
        process.wait()
        print('Playbook выполнен.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())