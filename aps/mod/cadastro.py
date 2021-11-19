from sqlite3 import dbapi2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from db.banco import banco_db

from template.telacadast import telaCad


class cadastrar(QDialog):
    def __init__(self,*args,**argvs):
        super(cadastrar,self).__init__(*args,**argvs)
        self.ui = telaCad()
        self.ui.setupUi(self) 
        self.ui.pushButton_4.clicked.connect(self.cadNovo)
    
#____________________VAI NO BANCO E REALIZA A INTRODUÇÃO DOS DADOS________________________#

    def cadNovo(self):
        db = banco_db("cadastro.db")

        Tnome = self.ui.lineEdit.text()
        Tlogin = self.ui.lineEdit_3.text()
        Tsenha = self.ui.lineEdit_2.text()
        Tnivel = self.ui.lineEdit_4.text()
       
#________________________BLOCO DE REPEDIÇÃO CASO HAJA FALTA DE DADOS___________________#

        if Tlogin == "" or Tsenha =="" or Tnome =="" or Tnivel=="":
            QMessageBox.information(QMessageBox(),"ERRO NO CADASTRO", "PREENCHA OS CAMPOS CORRETAMENTE!!")
        else:
            db.inserir_dados("INSERT INTO cadastro (nome, login, senha, nivel) VALUES ('{}','{}','{}','{}')".format(Tnome,Tlogin,Tsenha,Tnivel))
            QMessageBox.information(QMessageBox(),"SUCESSO NO CADASTRO", "CADASTRO CRIADO!!")
    
 

        