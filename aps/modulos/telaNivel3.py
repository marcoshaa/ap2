from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.nivel3 import nivel3
from modulos.login import login

class tela_3(QMainWindow):
    def __init__(self,*args,**argvs):
        super(tela_3,self).__init__(*args,**argvs)
        self.ui = nivel3()
        self.ui.setupUi(self) 
        self.ui.voltaN3.clicked.connect(self.voltaLogin)

    def voltaLogin(self):
        voltaLogin = login()
        voltaLogin.exec_()

