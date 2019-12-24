import sys
from os import system
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from calc36 import Ui_MainWindow
from math import sin, cos, tan, asin, acos, atan, log2, log10, log, factorial, pi


def SOCC(base_in, base_out, n): #system of calculation convector
    c=''
    if '-' in str(n):
        c='-'
        n = ''.join(list(str(n))[1:])    
    try:    
        base = [i for i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ']
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
                i = 0
                while n[1] != 0:
                    i += 1
                    n[1] = n[1] * base_out
                    b += [base[int(n[1])]]
                    n[1] -= int(n[1])
                    if i > 100:
                        break
            b = ''.join(b)
            return c+str(b)
        else:
            return SOCC(10, base_out, SOCC(base_in, 10, n))
    except Exception as a:
        print(a)


class Calculator(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ev = []
        #Цифры
        self.Button0.clicked.connect(self.run)
        self.Button1.clicked.connect(self.run)
        self.Button2.clicked.connect(self.run)
        self.Button3.clicked.connect(self.run)
        self.Button4.clicked.connect(self.run)
        self.Button5.clicked.connect(self.run)
        self.Button6.clicked.connect(self.run)
        self.Button7.clicked.connect(self.run)
        self.Button8.clicked.connect(self.run)
        self.Button9.clicked.connect(self.run)
        self.ButtonA.clicked.connect(self.run)
        self.ButtonB.clicked.connect(self.run)
        self.ButtonC.clicked.connect(self.run)
        self.ButtonD.clicked.connect(self.run)
        self.ButtonE.clicked.connect(self.run)
        self.ButtonF_2.clicked.connect(self.run)
        self.ButtonG.clicked.connect(self.run)
        self.ButtonH.clicked.connect(self.run)
        self.ButtonI.clicked.connect(self.run)
        self.ButtonJ.clicked.connect(self.run)
        self.ButtonK.clicked.connect(self.run)
        self.ButtonL.clicked.connect(self.run)
        self.ButtonM.clicked.connect(self.run)
        self.ButtonN.clicked.connect(self.run)
        self.ButtonO.clicked.connect(self.run)
        self.ButtonP.clicked.connect(self.run)
        self.ButtonQ.clicked.connect(self.run)
        self.ButtonR.clicked.connect(self.run)
        self.ButtonS.clicked.connect(self.run)
        self.ButtonT_2.clicked.connect(self.run)
        self.ButtonU.clicked.connect(self.run)
        self.ButtonV.clicked.connect(self.run)
        self.ButtonW.clicked.connect(self.run)
        self.ButtonX.clicked.connect(self.run)
        self.ButtonY.clicked.connect(self.run)
        self.ButtonZ.clicked.connect(self.run)       
        
        #
        self.ButtonBack.clicked.connect(self.run)
        self.ButtonCos.clicked.connect(self.run)
        self.ButtonCube.clicked.connect(self.run)
        self.ButtonDel.clicked.connect(self.run)
        self.ButtonDelenie.clicked.connect(self.run)
        self.ButtonDiv.clicked.connect(self.run)
        self.ButtonMod.clicked.connect(self.run)
        self.ButtonProizvedenie.clicked.connect(self.run)
        self.ButtonRavno.clicked.connect(self.rez)
        self.ButtonRaznica.clicked.connect(self.run)
        self.ButtonSin.clicked.connect(self.run)
        self.ButtonSqrt.clicked.connect(self.run)
        self.ButtonSqrt_2.clicked.connect(self.run)
        self.ButtonSqrt_3.clicked.connect(self.run)
        self.ButtonSquare.clicked.connect(self.run)
        self.ButtonStepen.clicked.connect(self.run)
        self.ButtonSumma.clicked.connect(self.run)
        self.ButtonT.clicked.connect(self.run)
        self.ButtonTg.clicked.connect(self.run)
        self.ButtonS1.clicked.connect(self.run)
        self.ButtonS2.clicked.connect(self.run)        
        self.ButtonF.clicked.connect(self.run)        
        self.Buttonlog2.clicked.connect(self.run)        
        self.ButtonPi.clicked.connect(self.run)        
        self.ButtonASin.clicked.connect(self.run)        
        self.ButtonACos.clicked.connect(self.run)        
        self.ButtonATg.clicked.connect(self.run)        
        #Menu
        self.action2_2.triggered.connect(self.s2)
        self.action8.triggered.connect(self.s8)
        self.action10.triggered.connect(self.s10)
        self.action16.triggered.connect(self.s16)
        self.action_4.triggered.connect(self.s)
        self.action_2.triggered.connect(self.mass_convector)
        self.action_6.triggered.connect(self.length_convector)
        self.action_9.triggered.connect(self.time_convector)
        self.action_10.triggered.connect(self.speed_convector)
        self.action.triggered.connect(self.system_of_calculation_convector)
        
    def s2(self):
        open('system.txt', 'w').write(str(2))
    def s8(self):
        open('system.txt', 'w').write(str(8))
    def s10(self):
        open('system.txt', 'w').write(str(10))
    def s16(self):
        open('system.txt', 'w').write(str(16))
    def s(self):
        system('python SV.py')
    def mass_convector(self):
        system('python konvertor.py')
    def length_convector(self):
        system('python konvertor_len.py')
    def time_convector(self):
        system('python konveror_time.py')
    def speed_convector(self):
        system('python konveror_speed.py')
    def system_of_calculation_convector(self):
        system('python soc_start.py')
        
    
            
    def run(self):
        if self.sender().text() == '<--':
            self.ev = self.ev[:-1]
        elif self.sender().text() == 'С':
            self.ev = []
        elif self.sender().text() == 'x':
            self.ev += ['*']
        elif self.sender().text() == 'mod':
            self.ev += ['%']
        elif self.sender().text() == 'div':
            self.ev += ['//']
        elif self.sender().text() == '√':
            self.ev += ['**0.5']
        elif self.sender().text() == '3√':
            self.ev += ['**(1/3)']
        elif self.sender().text() == 'y√':
            self.ev += ['**(1/']
        elif self.sender().text() == 'x^2':
            self.ev += ['**2']
        elif self.sender().text() == 'x^3':
            self.ev += ['**3']
        elif self.sender().text() == 'x^y':
            self.ev += ['**']
        elif self.sender().text() == 'sin':
            self.ev += ['sin(']
        elif self.sender().text() == 'cos':
            self.ev += ['cos(']
        elif self.sender().text() == 'tan':
            self.ev += ['tan(']
        elif self.sender().text() == 'asin':
            self.ev += ['asin(']
        elif self.sender().text() == 'acos':
            self.ev += ['acos(']
        elif self.sender().text() == 'atan':
            self.ev += ['atan(']      
        elif self.sender().text() == 'log2':
            self.ev += ['log2(']
        elif self.sender().text() == 'log10':
            self.ev += ['log10(']
        elif self.sender().text() == 'logX':
            self.ev += ['log(']            
        elif self.sender().text() == '!':
            self.ev += ['factorial(']
        elif self.sender().text() == 'pi':
            self.ev += [str(pi)]
        else:
            self.ev += [self.sender().text()]      
        self.label.setText(''.join(self.ev))

    def rez(self):
        sistem = int(open('system.txt', 'r').read())
        if sistem != 10:
            fl = True
            for i in range(len(self.ev)):
                if self.ev[i] not in ['(', ')', '+', '-', '/', '*', '%', '//', '**0.5', '**(1/3)', '**(1/', '**2', '**3', '**', 'sin(', 'cos(', 'tan(', 'asin(', 'acos(', 'atan(', 'log2(', 'log10(', 'log(', 'factorial(', str(pi)] and fl:
                    fl = not fl
                    self.ev[i] = "SOCC(sistem, 10, '"+self.ev[i]
                if self.ev[i] in ['(', ')', '+', '-', '/', '*', '%', '//', '**0.5', '**(1/3)', '**(1/', '**2', '**3', '**', 'sin(', 'cos(', 'tan(', 'asin(', 'acos(', 'atan(', 'log2(', 'log10(', 'log(', 'factorial(', str(pi)] and not fl:
                    fl = not fl
                    self.ev[i-1] = self.ev[i-1]+"')"
                if self.ev[i] not in ['(', ')', '+', '-', '/', '*', '%', '//', '**0.5', '**(1/3)', '**(1/', '**2', '**3', '**', 'sin(', 'cos(', 'tan(', 'asin(', 'acos(', 'atan(', 'log2(', 'log10(', 'log(', 'factorial(', str(pi)] and i == len(self.ev)-1:
                    self.ev[i] = self.ev[i]+"')"
        try:
            prim = ''.join(self.ev)
            print(prim)
            r = str(eval(prim))
            print(r)
            if sistem != 10:
                r = ''.join(list(str(SOCC(10, sistem, float(r))))[0:27])
            self.label.setText(r)
            self.ev = list(r)
        except Exception as a:
            print(a)
            self.label.setText('Error')
            self.ev = []
open('system.txt', 'w').write(str(10))
app = QApplication(sys.argv)
ex = Calculator()
ex.show()
sys.exit(app.exec())
