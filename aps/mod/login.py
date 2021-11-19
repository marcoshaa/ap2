from PyQt5.QtCore import showbase
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *

from template.telaLogin import telaLogin
from mod.cadastro import cadastrar 
from db.banco import banco_db
from template.nivel1 import nivel1
from template.nivel2 import nivel2
from template.nivel3 import nivel3

 #________________________________________________________________________________________________________#  
 
class tela_1(QMainWindow):
    def __init__(self,*args,**argvs):
        super(tela_1,self).__init__(*args,**argvs)
        self.ui = nivel1()
        self.ui.setupUi(self) 
        self.ui.voltaN1.clicked.connect(self.voltaLogin)

    def voltaLogin(self):
        voltaLogin = login()
        voltaLogin.exec_()
        
def chamaT1(self):
        chamat1 = tela_1()
        chamat1.show()

 #________________________________________________________________________________________________________# 
       
class tela_2(QMainWindow):
    def __init__(self,*args,**argvs):
        super(tela_2,self).__init__(*args,**argvs)
        self.ui = nivel2()
        self.ui.setupUi(self) 
        self.ui.voltaN2.clicked.connect(self.voltaLogin)

    def voltaLogin(self):
        voltaLogin = login()
        voltaLogin.exec_()

def chamaT2(self):
    chamat2 = tela_2()
    chamat2.show()

 #________________________________________________________________________________________________________#  

class tela_3(QMainWindow):
    def __init__(self,*args,**argvs):
        super(tela_3,self).__init__(*args,**argvs)
        self.ui = nivel3()
        self.ui.setupUi(self) 
        self.ui.voltaN3.clicked.connect(self.voltaLogin)

    def voltaLogin(self):
        voltaLogin = login()
        voltaLogin.exec_()

def chamaT3(self):
    chamat3 = tela_2()
    chamat3.show()

 #________________________________________________________________________________________________________#  


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
            chamaT1(self)

        elif nivel[0][0] ==2:
           chamaT2(self)

        elif nivel[0][0] == 3:
            chamaT3(self)

        else:
            QMessageBox.warning(QMessageBox(),"ALERTA","NIVEL DE ACESSO NAO LOCALIZADO!!")
   
        