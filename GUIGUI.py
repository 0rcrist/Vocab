import sys
from PyQt5 import QtWidgets as Qw
from PyQt5 import QtCore as Qc
import random as rd
from PyQt5 import QtGui

class VocabGui(Qw.QWidget):

    def __init__(self, dic):
        super().__init__()
        #self.title = 'Vocab'
        self.dic= dic
        self.getMaxMin()
        self.resize(1000, 500)
        self.setAutoFillBackground(True)
        self.initUI()

    def initUI(self):
        #self.setWindowTitle(self.title)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qc.Qt.white)
        self.setPalette(p)
        for  key,value in self.dic.items():
            self.ob = Circles(self, key, value, self.Max)
        label = Qw.QLabel(self)
        label.setText(str(self.Max))
        label.setGeometry(960,460,100,50)
        label2 = Qw.QLabel(self)
        label2.setText(str(int(self.Max/2)))
        label2.setGeometry(480,460,100,50)
        label3= Qw.QLabel(self)
        label3.setText('0')
        label3.setGeometry(5,460,100,50)
        self.show()


    def getMaxMin(self):
        self.Max = max([x for x in self.dic.values()])
        if self.Max >= 10000:
            self.Max += 5000
        else: self.Max+=500

    def addAuthor(self, name, num):
        self.dic[name] = num
        self.initUI()

class Circles(Qw.QWidget):
    def __init__(self, parent, key,value, max):
        Qw.QWidget.__init__(self,parent)
        self.name = key
        self.value = int(value)
        self.setGeometry((self.value/max)*1000, rd.randrange(50,450), 15, 15)
        self.initW()
        self.setAutoFillBackground(True)
        self.setToolTip(self.name+"\nWords: " + str(self.value))
        #self.show()

    def initW(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), Qc.Qt.red)
        self.setPalette(p)


if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    ex = VocabGui({'el': 1500, 'ella':10, 'yo':5000, 'noso':20000, 'tak': 2000, 'h':1000, 'f':1500, 'l':20000,'p':7800})
    sys.exit(app.exec_())