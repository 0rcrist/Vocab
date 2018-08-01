import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, qApp, QAction, QLineEdit, QPushButton, \
    QGridLayout, QBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
import GUIGUI
import projectGUI



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowSetup()

    def windowSetup(self):
        self.setWindowTitle("   Vocabulary of Musicians")
        self.setGeometry(550,250,1000,1000)
        self.setWindowIcon(QIcon(r'C:\Users\Emilio\Pictures\Wallpaper\music-note-icon'))

        newFileAction = QAction('&New Vocab File...', self)
        newFileAction.setShortcut('Ctrl+N')
        newFileAction.setStatusTip('create new vocab file')
        #newFileAction.triggered.connect()

        loadFileAction = QAction('&Load Vocab File...', self)
        loadFileAction.setShortcut('Ctrl+L')
        loadFileAction.setStatusTip('load an existing vocab file')
        #loadFileAction.triggered.connect()

        saveFileAction = QAction('&Save Vocab File...', self)
        saveFileAction.setShortcut('Ctrl+S')
        saveFileAction.setStatusTip('save the current vocab file')
        #saveFileAction.triggered().connect()


        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newFileAction)
        fileMenu.addAction(loadFileAction)
        fileMenu.addAction(saveFileAction)

        #create our textbox
        self.searchBox = QLineEdit(self)
        self.searchBox.move(50,50)
        self.searchBox.resize(300,45)

        #create search button
        self.searchBtn = QPushButton('Search Artist', self)
        self.searchBtn.move(360, 50)
        self.searchBtn.resize(100,45)
        self.searchBtn.clicked.connect(self.onClick)

        #self.setCentralWidget(GUIGUI.VocabGui({'el': 1500, 'ella':10, 'yo':5000, 'noso':20000, 'tak': 2000, 'h':1000, 'f':1500, 'l':20000, 'p':7800}))

        self.setCentralWidget(projectGUI.Window())

        self.show()

    @pyqtSlot()
    def onClick(self):
        searchBoxArtistVal = self.searchBox.text()
        print(searchBoxArtistVal)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())