from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.telaLogin import telaLogin
from modulos.cadastro import cadastrar 


class login(QDialog):
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = telaLogin()
        self.ui.setupUi(self)
        self.ui.btCad.clicked.connect(self.cad)

    def cad(self):
        cad = cadastrar()
        cad.exec_()




