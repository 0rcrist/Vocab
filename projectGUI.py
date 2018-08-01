import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, qApp, QAction, QGridLayout, \
    QStackedLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QActionEvent
import GUIGUI

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

        grid.addWidget(GUIGUI.VocabGui({'el': 1500, 'ella':10, 'yo':5000, 'noso':20000, 'tak': 2000, 'h':1000, 'f':1500, 'l':20000, 'p':7800}), 2, 1)

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
