from PyQt5 import QtCore, QtGui, QtWidgets


class telaLogin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(388, 392)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 10, 191, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgN1/img/imgTela1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 170, 41, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/imgN1/img/login.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 31, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/imgN1/img/padlock.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.loginLogin = QtWidgets.QLineEdit(Dialog)
        self.loginLogin.setGeometry(QtCore.QRect(130, 170, 181, 22))
        self.loginLogin.setObjectName("loginLogin")
        self.loginSenha = QtWidgets.QLineEdit(Dialog)
        self.loginSenha.setGeometry(QtCore.QRect(130, 230, 181, 22))
        self.loginSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginSenha.setObjectName("loginSenha")
        self.btEntrar = QtWidgets.QPushButton(Dialog)
        self.btEntrar.setGeometry(QtCore.QRect(50, 300, 75, 31))
        self.btEntrar.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.btEntrar.setObjectName("btEntrar")
        self.btCad = QtWidgets.QPushButton(Dialog)
        self.btCad.setGeometry(QtCore.QRect(140, 300, 101, 31))
        self.btCad.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.btCad.setObjectName("btCad")
        self.btBio = QtWidgets.QPushButton(Dialog)
        self.btBio.setGeometry(QtCore.QRect(270, 300, 81, 31))
        self.btBio.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.btBio.setObjectName("btBio")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TELA DE LOGIN"))
        self.loginLogin.setPlaceholderText(_translate("Dialog", "DIGITE SEU LOGIN"))
        self.loginSenha.setPlaceholderText(_translate("Dialog", "DIGITE SUA SENHA"))
        self.btEntrar.setText(_translate("Dialog", "ENTRAR"))
        self.btCad.setText(_translate("Dialog", "CADASTRAR"))
        self.btBio.setText(_translate("Dialog", "BIOMETRIA"))

import template.imgN1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = telaLogin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
