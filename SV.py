import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from SOC import Ui_MainWindow


class SV(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        open('system.txt', 'w').write(str(self.spinBox.value()))
        sys.exit()

app = QApplication(sys.argv)
ex = SV()
ex.show()
sys.exit(app.exec())
