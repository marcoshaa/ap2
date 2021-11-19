from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


from modulos.principal import tela_1
from modulos.telaNivel3 import tela_3
from modulos.telaNivel2 import tela_2
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
        self.ui.btEntrar.clicked.connect(self.nivelAcess)


    def chamaCad(self):# chama a tela de cadastro, função do botao cadastar
        chamaCad = cadastrar()
        chamaCad.exec_()

#__________________CONECTA NO BANCO DE DADOS PARA VALIDAR O ACESSO DO USUARIO____________________________#
    def login(self):
        db = banco_db("cadastro.db")

        nomeUsuario = self.ui.loginLogin.text()
        senhaUsuario = self.ui.loginSenha.text()
        
        if nomeUsuario == "" or senhaUsuario =="":
            QMessageBox.warning(QMessageBox(),"ALERTA","PREENCHA TODOS OS CAMPOS!!")
        else:
            dados = db.pegar_dados("SELECT login,senha,nivel FROM cadastro WHERE login ='{}' and senha = '{}'".format(nomeUsuario,senhaUsuario)) 
            
            if dados:
                QMessageBox.information(QMessageBox(),"Login Realizado","LOGIN VALIDADO")

#________________________VALIDA O NIVELDE ACESSO PARA ABRIR A TELA QUE O USUARIO TEM PERMISSÃO_______________#

    def nivelAcess(self):
        db = banco_db("cadastro.db")

        nomeUsuario = self.ui.loginLogin.text()
        dados = db.pegarNivel("SELECT nivel FROM cadastro WHERE login ='{}'".format(nomeUsuario)) 
        nivel = db.cursor.fetchall()
        print(nivel[0][0])#pega no banco de dados o nivel, [0][0] serve para dar o print na 1°lista da 1°tupla.

        if nivel[0][0] == 1:
            self.ui.btEntrar.clicked.connect(self.chamaT1)
        
        elif nivel[0][0] ==2:
            self.ui.btEntrar.clicked.connect(self.chamaT2)
            
        elif nivel[0][0] == 3:
            self.ui.btEntrar.clicked.connect(self.chamaT3)

        else:
            QMessageBox.warning(QMessageBox(),"ALERTA","NIVEL DE ACESSO NAO LOCALIZADO!!")

    def chamaT1(self):
        window = tela_1()
        window.show()
        
    def chamaT2(self):
        window = tela_2()
        window.show()

    def chamaT3(self):
        window = tela_3()
        window.show()



