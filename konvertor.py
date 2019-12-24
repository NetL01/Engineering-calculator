import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLineEdit, QApplication, QLabel, QPushButton, QComboBox)
                             
class Convertor(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('konvertor.ui', self)
        self.res.clicked.connect(self.result)

    def result(self):
        try:
            m = float(self.input.text())
            if self.input_step.currentText() == "Грамм":
                m /= 1000
            elif self.input_step.currentText() == "Тонна":
                m *= 1000
            elif self.input_step.currentText() == "Центнер":
                m *= 100
            elif self.input_step.currentText() == "Карат":
                m = m / 10000 *2
            elif self.input_step.currentText() == "Стоун":
                m *= 6.35029
            elif self.input_step.currentText() == "Фунт английский":
                m *= 0.45
            elif self.input_step.currentText() == "Унция":
                m *= 0.028
            elif self.input_step.currentText() == "Гран американский":
                m *= 6.48 * 10 ** (-5)
            elif self.input_step.currentText() == "Короткая тонна":
                m *= 907.18474
            elif self.input_step.currentText() == "Тройский фунт":
                m /= 2.6792
            elif self.input_step.currentText() == "Тройская унция":
                m *= 0.031
            elif self.input_step.currentText() == "Гран британский":
                m *= 0.0000648
            elif self.input_step.currentText() == "Пуд":
                m *= 16.38
            elif self.input_step.currentText() == "Фунт русский":
                m *= 0.45
            elif self.input_step.currentText() == "Золотник":
                m *= 4.266 / 1000
            elif self.input_step.currentText() == "Доля":
                m *= 4.44 * 10 ** (-5)
            elif self.input_step.currentText() == "Английская тонна":
                m *= 1016.0469088
            elif self.input_step.currentText() == "Марка":
                m *= 249 / 1000
            if self.output_step.currentText() == "Грамм":
                m *= 1000
            elif self.output_step.currentText() == "Тонна":
                m /= 1000
            elif self.output_step.currentText() == "Центнер":
                m /= 100
            elif self.output_step.currentText() == "Карат":
                m = m * 10000 / 2
            elif self.output_step.currentText() == "Стоун":
                m /= 6.35029
            elif self.output_step.currentText() == "Фунт английский":
                m /= 0.45
            elif self.output_step.currentText() == "Унция":
                m /= 0.028
            elif self.output_step.currentText() == "Гран американский":
                m /= 6.48 * 10 ** (-5)
            elif self.output_step.currentText() == "Короткая тонна":
                m /= 907.18474
            elif self.output_step.currentText() == "Тройский фунт":
                m /= 2.6792
            elif self.output_step.currentText() == "Тройская унция":
                m /= 0.031
            elif self.output_step.currentText() == "Гран британский":
                m /= 0.0000648
            elif self.output_step.currentText() == "Пуд":
                m /= 16.38
            elif self.output_step.currentText() == "Фунт русский":
                m /= 0.45
            elif self.output_step.currentText() == "Золотник":
                m /= 4.266 / 1000
            elif self.output_step.currentText() == "Доля":
                m /= 4.44 * 10 ** (-5)
            elif self.output_step.currentText() == "Английская тонна":
                m /= 1016.0469088
            elif self.output_step.currentText() == "Марка":
                m /= 249 / 1000
            self.output.setText(str(m))
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Convertor()
    ex.show()
    sys.exit(app.exec())
