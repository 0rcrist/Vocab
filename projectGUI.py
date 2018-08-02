import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, qApp, QAction, QGridLayout, \
    QStackedLayout,QLabel
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QActionEvent
import GUIGUI
from GUIGUI import VocabGui

'''
class ToolBar(QMainWindow):
    def __init__(self):
        super().__init__()

    def bar(self):
        menu = self.menuBar()

        menu.addMenu('&File')
'''

class Window(QWidget):          #window class is an instance of QWidget

    def __init__(self):
        super().__init__()      #call on constructor for QWidget


        self.initialWindow()    #QWidget.initialWindow()


    def initialWindow(self):
        self.resize(1000,1000)      #we pass in a QWidget object to this this is our window

        self.moveToCenter()             #call function that centers our window

        #self.setWindowTitle("  Vocabulary of Musicians")

        #self.setWindowIcon(QIcon(r'C:\Users\Emilio\Pictures\Wallpaper\music-note-icon'))


        grid = QGridLayout()

        grid.setSpacing(10)

        grid.addWidget(QWidget(), 1, 1)

        graph = GUIGUI.VocabGui({'el': 1500, 'ella':10, 'yo':5000, 'noso':20000, 'tak': 2000, 'h':1000, 'f':1500, 'l':20000, 'p':7800})

        grid.addWidget(graph, 2, 1)

        grid.addWidget(Axis(graph.Max),3,1)

        self.setLayout(grid)

        #self.show()



        '''
        qmw = QMainWindow()             #create QMainWindow obj

        topBar = qmw.menuBar()

        fileBtn = topBar.addMenu('File')

        fileBtn.addAction("New vocab...")

        qmw.setMenuWidget()

        qmw.show()

        self.set




        #qmw.show()



        #extra = ToolBar()
        
        '''


    def moveToCenter(self):
        frame = self.frameGeometry()

        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())

    '''
   class ToolBar(QMainWindow):
        def __init__(self):
            super().__init__()

        def bar(self):
            menu = self.menuBar()

            menu.addMenu('&File')'''


class Axis(QWidget):
    def __init__(self, num):
        super().__init__()
        label = QLabel(self)
        label.setText(str(num))
        label.setGeometry(950, 0, 100, 50)
        label2 = QLabel(self)
        label2.setText(str(int(num / 2)))
        label2.setGeometry(460, 0, 100, 50)
        label3 = QLabel(self)
        label3.setText('0')
        label3.setGeometry(0, 0, 100, 50)

    def paintEvent(self,event):
        qp = QtGui.QPainter()
        qp.begin(self)
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawLine(0,0, 1000, 0)
        qp.end()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    program = Window()

    '''class ToolBar(QMainWindow):
        def __init__(self):
            super().__init__()

        class ToolBar(QMainWindow):
            def __init__(self):
                super().__init__()

            def bar(self):
                menu = self.menuBar()

                menu.addMenu('&File')
        def bar(self):
            menu = self.menuBar()

            menu.addMenu('&File')'''
    sys.exit(app.exec_())
