from PyQt5 import QtCore, QtGui, QtWidgets


class telaCad(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 379)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 481, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgN1/img/telacad.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 31, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/imgN1/img/login.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 31, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/imgN1/img/login.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 140, 41, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/imgN1/img/padlock.png"))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 181, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 150, 181, 22))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 110, 181, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 290, 151, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 190, 181, 22))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 190, 31, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/imgN1/img/chave.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 241, 21))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CADASTRO"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "CADASTRE SEU NOME"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "CADASTRE SUA SENHA"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "CADASTRE SEU LOGIN"))
        self.pushButton_4.setText(_translate("Dialog", "CADASTRAR"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "DEFINA O NIVEL DE ACESSO"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">CADASTRAR NOVO USUARIO<br/></p></body></html>"))
import template.imgN1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = telaCad()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
