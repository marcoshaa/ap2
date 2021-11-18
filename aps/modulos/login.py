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
from db.banco import banco_db

class login(QDialog):
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = telaLogin()
        self.ui.setupUi(self)
        self.ui.btCad.clicked.connect(self.chamaCad)
        self.ui.btEntrar.clicked.connect(self.login)

    def chamaCad(self):# chama a tela de cadastro, função do botao cadastar
        chamaCad = cadastrar()
        chamaCad.exec_()

    def login(self):
        db = banco_db("cadastro.db")

        nomeUsuario = self.ui.loginLogin.text()
        senhaUsuario = self.ui.loginSenha.text()
        
        if nomeUsuario == "" or senhaUsuario =="":
            QMessageBox.warning(QMessageBox(),"ALERTA","PREENCHA TODOS OS CAMPOS!!")
        else:
            dados = db.pegar_dados("SELECT login,senha,nivel FROM cadastro WHERE login ='{}' and senha = '{}'".format(nomeUsuario,senhaUsuario))
            print(dados)
            if dados:
                QMessageBox.information(QMessageBox(),"Login Realizado","LOGIN VALIDADO")



