import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QLineEdit, QApplication, QLabel, QPushButton, QComboBox)

                             
class ConvertorSpeed(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('konvertor_speed.ui', self)
        self.res.clicked.connect(self.result)

    def result(self):
        try:
            v = float(self.input.text())
            if self.input_step_2.currentText() == "минута":
                v /= 60
            elif self.input_step_2.currentText() == "Час":
                v /= 3600
            elif self.input_step_2.currentText() == "Сутки":
                v /= 3600 * 24
            elif self.input_step_2.currentText() == "Неделя":
                v /= 3600 * 24 * 7
            elif self.input_step_2.currentText() == "Месяц":
                v /= 3600 * 24 * 30
            elif self.input_step_2.currentText() == "Год":
                v /= 3600 * 24 *365
            elif self.input_step_2.currentText() == "Милисекунда":
                v /= 1 / 1000
            elif self.input_step_2.currentText() == "Миг":
                v /= 1 / 100
            elif self.input_step_2.currentText() == "Тик":
                v /= 1 / 10
            elif self.input_step_2.currentText() == "Фортнайт":
                v /= 3600 * 24 * 14
            elif self.input_step_2.currentText() == "Академ. час":
                v /= 60 * 45
            elif self.input_step_2.currentText() == "Терция":
                v / 1 / 60
            elif self.input_step_2.currentText() == "Аттосекунда":
                v /= 10 ** (-18)
            if self.input_step.currentText() == "Километр":
                v *= 1000
            elif self.input_step.currentText() == "Дециметр":
                v *= 0.1
            elif self.input_step.currentText() == "Сантиметр":
                v *= 0.01
            elif self.input_step.currentText() == "Миллиметр":
                v *= 0.001
            elif self.input_step.currentText() == "Микрометр":
                v *= 0.000001
            elif self.input_step.currentText() == "Нанометр":
                v *= 0.000000001
            elif self.input_step.currentText() == "Пикометр":
                v *= 10 ** (-9)
            elif self.input_step.currentText() == "Фемтометр":
                v *= 10 ** (-15)
            elif self.input_step.currentText() == "Лига":
                v *= 1000 * 4.82
            elif self.input_step.currentText() == "Миля":
                v *= 1609.34
            elif self.input_step.currentText() == "Морская миля":
                v * 1852
            elif self.input_step.currentText() == "r Земли":
                v *= 6371000
            elif self.input_step.currentText() == "r Солнца":
                v *= 6.96 * 10 ** 8
            elif self.input_step.currentText() == "Свет. год":
                v *= 9460730472583800
            elif self.input_step.currentText() == "Свет. сутки":
                v *= 9460730472583800 / 365
            elif self.input_step.currentText() == "Свет. месяц":
                v *= 9460730472583800 / 365 * 30
            elif self.input_step.currentText() == "Свет. час":
                v *= 9460730472583800 / 365 / 24
            elif self.input_step.currentText() == "Свет. минута":
                v *= 9460730472583800 / 365 / 24 / 60
            elif self.input_step.currentText() == "Свет. секунда":
                v *= 9460730472583800 / 365 / 24 / 3600
            elif self.input_step.currentText() == "Свет. неделя":
                v *= 9460730472583800 / 365 / 24 * 7
            elif self.input_step.currentText() == "А. е.":
                v *= 149597870700
            elif self.input_step.currentText() == "Парсек":
                v *= 3.09e+16
            elif self.input_step.currentText() == "Ярд":
                v *= 0.91
            elif self.input_step.currentText() == "Дюйм":
                v *= 2.54 / 100
            if self.output_step.currentText() == "Километр":
                v /= 1000
            elif self.output_step.currentText() == "Дюйм":
                v /= 2.54 / 100
            elif self.output_step.currentText() == "Ярд":
                v /= 0.91
            elif self.output_step.currentText() == "Дециметр":
                v /= 0.1
            elif self.output_step.currentText() == "Сантиметр":
                v /= 0.01
            elif self.output_step.currentText() == "Миллиметр":
                v /= 0.001
            elif self.output_step.currentText() == "Микрометр":
                v /= 0.000001
            elif self.output_step.currentText() == "Нанометр":
                v /= 0.000000001
            elif self.output_step.currentText() == "Пикометр":
                v /= 10 ** (-9)
            elif self.output_step.currentText() == "Фемтометр":
                v /= 10 ** (-15)
            elif self.output_step.currentText() == "Лига":
                v /= 1000 * 4.82
            elif self.output_step.currentText() == "Миля":
                v /= 1609.34
            elif self.output_step.currentText() == "Морская миля":
                v /= 1852
            elif self.output_step.currentText() == "r Земли":
                v /= 6371000
            elif self.output_step.currentText() == "r Солнца":
                v /= 6.957 * 10 ** 8
            elif self.output_step.currentText() == "Свет. год":
                v /= 9460730472583800
            elif self.output_step.currentText() == "Свет. сутки":
                v /= 9460730472583800 / 365
            elif self.output_step.currentText() == "Свет. месяц":
                v /= 9460730472583800 / 365 * 30
            elif self.output_step.currentText() == "Свет. час":
                v /= 9460730472583800 / 365 / 24
            elif self.output_step.currentText() == "Свет. минута":
                v /= 9460730472583800 / 365 / 24 / 60
            elif self.output_step.currentText() == "Свет. секунда":
                v /= 9460730472583800 / 365 / 24 / 3600
            elif self.output_step.currentText() == "Свет. неделя":
                v /= 9460730472583800 / 365 / 24 * 7
            elif self.output_step.currentText() == "А. е.":
                v /= 149597870700
            elif self.output_step.currentText() == "Парсек":
                v /= 3.09e+16
            if self.output_step_2.currentText() == "минута":
                v *= 60
            elif self.output_step_2.currentText() == "Час":
                v *= 3600
            elif self.output_step_2.currentText() == "Сутки":
                v *= 3600 * 24
            elif self.output_step_2.currentText() == "Неделя":
                v *= 3600 * 24 * 7
            elif self.output_step_2.currentText() == "Месяц":
                v *= 3600 * 24 * 30
            elif self.output_step_2.currentText() == "Год":
                v *= 3600 * 24 *365
            elif self.output_step.currentText() == "Милисекунда":
                v *= 1 / 1000
            elif self.output_step_2.currentText() == "Миг":
                v *= 1 / 100
            elif self.output_step_2.currentText() == "Тик":
                v *= 1 / 10
            elif self.output_step_2.currentText() == "Фортнайт":
                v *= 3600 * 24 * 14
            elif self.output_step_2.currentText() == "Академ. час":
                v *= 60 * 45
            elif self.output_step_2.currentText() == "Терция":
                v *= 1 / 60
            elif self.output_step_2.currentText() == "Аттосекунда":
                v *= 10 ** (-18)
            self.output.setText(str(v))
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ConvertorSpeed()
    ex.show()
    sys.exit(app.exec())
