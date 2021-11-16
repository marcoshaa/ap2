# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import imgN1_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(440, 379)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 481, 471))
        self.label.setPixmap(QPixmap(u":/imgN1/img/telacad.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 60, 31, 41))
        self.label_2.setPixmap(QPixmap(u":/imgN1/img/login.png"))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 100, 31, 41))
        self.label_3.setPixmap(QPixmap(u":/imgN1/img/login.png"))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 140, 41, 41))
        self.label_4.setPixmap(QPixmap(u":/imgN1/img/padlock.png"))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 70, 181, 22))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 150, 181, 22))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(120, 110, 181, 22))
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(130, 290, 151, 51))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(0, 102, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 190, 181, 22))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 190, 31, 31))
        self.label_5.setPixmap(QPixmap(u":/imgN1/img/chave.png"))
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 20, 241, 21))
        self.label_6.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"CADASTRE SEU NOME", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"CADASTRE SUA SENHA", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"CADASTRE SEU LOGIN", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"CADASTRAR", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"DEFINA O NIVEL DE ACESSO", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">CADASTRAR NOVO USUARIO<br/></p></body></html>", None))
    # retranslateUi

