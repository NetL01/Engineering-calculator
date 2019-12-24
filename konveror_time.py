import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLineEdit, QApplication, QLabel, QPushButton, QComboBox)

                             
class ConvertorTime(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('konvertor_time.ui', self)
        self.res.clicked.connect(self.result)

    def result(self):
        try:
            t = float(self.input.text())
            if self.input_step.currentText() == "минута":
                t *= 60
            elif self.input_step.currentText() == "Час":
                t *= 3600
            elif self.input_step.currentText() == "Сутки":
                t *= 3600 * 24
            elif self.input_step.currentText() == "Неделя":
                t *= 3600 * 24 * 7
            elif self.input_step.currentText() == "Месяц":
                t *= 3600 * 24 * 30
            elif self.input_step.currentText() == "Год":
                t *= 3600 * 24 *365
            elif self.input_step.currentText() == "Милисекунда":
                t *= 1 / 1000
            elif self.input_step.currentText() == "Миг":
                t *= 1 / 100
            elif self.input_step.currentText() == "Тик":
                t *= 1 / 10
            elif self.input_step.currentText() == "Фортнайт":
                t *= 3600 * 24 * 14
            elif self.input_step.currentText() == "Академический час":
                t *= 60 * 45
            elif self.input_step.currentText() == "Терция":
                t *= 1 / 60
            elif self.input_step.currentText() == "Аттосекунда":
                t *= 10 ** (-18)
            if self.output_step.currentText() == "минута":
                t /= 60
            elif self.output_step.currentText() == "Час":
                t /= 3600
            elif self.output_step.currentText() == "Сутки":
                t /= 3600 * 24
            elif self.output_step.currentText() == "Неделя":
                t /= 3600 * 24 * 7
            elif self.output_step.currentText() == "Месяц":
                t /= 3600 * 24 * 30
            elif self.output_step.currentText() == "Год":
                t /= 3600 * 24 *365
            elif self.output_step.currentText() == "Милисекунда":
                t /= 1 / 1000
            elif self.output_step.currentText() == "Миг":
                t /= 1 / 100
            elif self.output_step.currentText() == "Тик":
                t /= 1 / 10
            elif self.output_step.currentText() == "Фортнайт":
                t /= 3600 * 24 * 14
            elif self.output_step.currentText() == "Академический час":
                t /= 60 * 45
            elif self.output_step.currentText() == "Терция":
                t /= 1 / 60
            elif self.output_step.currentText() == "Аттосекунда":
                t /= 10 ** (-18)
            self.output.setText(str(t))
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ConvertorTime()
    ex.show()
    sys.exit(app.exec())
