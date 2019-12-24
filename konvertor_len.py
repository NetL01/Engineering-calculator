import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLineEdit, QApplication, QLabel, QPushButton, QComboBox)
                             
class ConvertorLen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('konvertor_len.ui', self)
        self.res.clicked.connect(self.result)

    def result(self):
        try:
            l = float(self.input.text())
            if self.input_step.currentText() == "Километр":
                l *= 1000
            elif self.input_step.currentText() == "Дециметр":
                l *= 0.1
            elif self.input_step.currentText() == "Сантиметр":
                l *= 0.01
            elif self.input_step.currentText() == "Миллиметр":
                l *= 0.001
            elif self.input_step.currentText() == "Микрометр":
                l *= 0.000001
            elif self.input_step.currentText() == "Нанометр":
                l *= 0.000000001
            elif self.input_step.currentText() == "Пикометр":
                l *= 10 ** (-9)
            elif self.input_step.currentText() == "Фемтометр":
                l *= 10 ** (-15)
            elif self.input_step.currentText() == "Лига":
                l *= 1000 * 4.82
            elif self.input_step.currentText() == "Миля":
                l *= 1609.34
            elif self.input_step.currentText() == "Морская миля":
                l *= 1852
            elif self.input_step.currentText() == "Радиус Земли":
                l *= 6371000
            elif self.input_step.currentText() == "Радиус Солнца":
                l *= 6.960 * 10 ** 8
            elif self.input_step.currentText() == "Световой год":
                l *= 9460730472583800
            elif self.input_step.currentText() == "Световые сутки":
                l *= 9460730472583800 / 365
            elif self.input_step.currentText() == "Световой месяц":
                l *= 9460730472583800 / 365 * 30
            elif self.input_step.currentText() == "Световой час":
                l *= 9460730472583800 / 365 / 24
            elif self.input_step.currentText() == "Световая минута":
                l *= 9460730472583800 / 365 / 24 / 60
            elif self.input_step.currentText() == "Световая секунда":
                l *= 9460730472583800 / 365 / 24 / 3600
            elif self.output_step.currentText() == "Световая неделя":
                l /= 9460730472583800 / 365 / 24 * 7
            elif self.input_step.currentText() == "Астрономическая единица":
                l *= 149597870700
            elif self.input_step.currentText() == "Парсек":
                l *= 3.09e+16
            elif self.input_step.currentText() == "Ярд":
                l *= 0.91
            elif self.input_step.currentText() == "Дюйм":
                l *= 2.54 / 100
            if self.output_step.currentText() == "Километр":
                l /= 1000
            elif self.output_step.currentText() == "Дюйм":
                l /= 2.54 / 100
            elif self.output_step.currentText() == "Ярд":
                l /= 0.91
            elif self.output_step.currentText() == "Дециметр":
                l /= 0.1
            elif self.output_step.currentText() == "Сантиметр":
                l /= 0.01
            elif self.output_step.currentText() == "Миллиметр":
                l /= 0.001
            elif self.output_step.currentText() == "Микрометр":
                l /= 0.000001
            elif self.output_step.currentText() == "Нанометр":
                l /= 0.000000001
            elif self.output_step.currentText() == "Пикометр":
                l /= 10 ** (-9)
            elif self.output_step.currentText() == "Фемтометр":
                l /= 10 ** (-15)
            elif self.output_step.currentText() == "Лига":
                l /= 1000 * 4.82
            elif self.output_step.currentText() == "Миля":
                l /= 1609.34
            elif self.output_step.currentText() == "Морская миля":
                l /= 1852
            elif self.output_step.currentText() == "Радиус Земли":
                l /= 6371000
            elif self.output_step.currentText() == "Радиус Солнца":
                l /= 6.957 * 10 ** 8
            elif self.output_step.currentText() == "Световой год":
                l /= 9460730472583800
            elif self.output_step.currentText() == "Световые сутки":
                l /= 9460730472583800 / 365
            elif self.output_step.currentText() == "Световой месяц":
                l /= 9460730472583800 / 365 * 30
            elif self.output_step.currentText() == "Световой час":
                l /= 9460730472583800 / 365 / 24
            elif self.output_step.currentText() == "Световая минута":
                l /= 9460730472583800 / 365 / 24 / 60
            elif self.output_step.currentText() == "Световая секунда":
                l /= 9460730472583800 / 365 / 24 / 3600
            elif self.output_step.currentText() == "Световая неделя":
                l /= 9460730472583800 / 365 / 24 * 7
            elif self.output_step.currentText() == "Астрономическая единица":
                l /= 149597870700
            elif self.output_step.currentText() == "Парсек":
                l /= 3.09e+16
            self.output.setText(str(l))
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ConvertorLen()
    ex.show()
    sys.exit(app.exec())
