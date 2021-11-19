from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.nivel1 import nivel1
from modulos.login import login


class tela_1(QMainWindow):
    def __init__(self,*args,**argvs):
        super(tela_1,self).__init__(*args,**argvs)
        self.ui = nivel1()
        self.ui.setupUi(self) 
        self.ui.voltaN1.clicked.connect(self.voltaLogin)

    def voltaLogin(self):
        voltaLogin = login()
        voltaLogin.exec_()