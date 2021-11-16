from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.telacadast import telaCad


class cadastrar(QDialog):
    def __init__(self,*args,**argvs):
        super(cadastrar,self).__init__(*args,**argvs)
        self.ui = telaCad()
        self.ui.setupUi(self) 