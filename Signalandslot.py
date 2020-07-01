from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('click')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('buna basdin!!')
    alert.exec_()
button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
