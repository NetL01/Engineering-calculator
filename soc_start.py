import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from SOCC import Ui_MainWindow


def SOCC(base_in, base_out, n):
    c=''
    if '-' in str(n):
        c='-'
        n = ''.join(list(str(n))[1:])    
    try:    
        base = [i for i in '0123456789ABCDEFGHIJKLMюNOPQRSTUVWXYZ']
        if base_out == 10:
            a = 0
            n = str(n).split('.')
            for i in range(1,len(n[0])+1):
                if n[0][-i] not in base[0:base_in]:
                    return 'error'
                a+=int(base.index(n[0][-i]))*base_in**(i - 1)
            if len(n) != 1:
                for i in range(1,len(n[1])+1):
                    if n[1][-i] not in base[0:base_in]:
                        return 'error'
                    a+=int(base.index(n[1][-i]))*base_in**(-i)
            return float(c+str(a))
        elif base_in == 10:
            n = str(n).split('.')
            if len(n) == 1:
                n.append('0')
            n[0] = int(n[0])
            n[1] = float('0.'+n[1])
            b=[]
            while n[0] != 0:
                b += [base[n[0] % base_out]]
                n[0] //= base_out
            b = b[::-1]
            if n[1] != 0:        
                b += ['.']
                while n[1] != 0:
                    n[1] = n[1] * base_out
                    b += [base[int(n[1])]]
                    n[1] -= int(n[1])
            b = ''.join(b)
            return c+str(b)
        else:
            return SOCC(10, base_out, SOCC(base_in, 10, n))
    except Exception as a:
        print(a)

class SoccStart(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
    def run(self):
        try:
            a = str(SOCC(self.spinBox.value(), self.spinBox_2.value(), self.lineEdit.text()))
            self.label_4.setText(''.join(list(a)[0:84]))
        except Exception as a:
            print(a)
app = QApplication(sys.argv)
ex = SoccStart()
ex.show()
sys.exit(app.exec()) 
