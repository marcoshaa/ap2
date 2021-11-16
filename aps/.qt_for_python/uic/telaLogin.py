# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telaLogin.ui'
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
        Dialog.resize(388, 392)
        Dialog.setStyleSheet(u"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 191, 101))
        self.label.setPixmap(QPixmap(u":/imgN1/img/imgTela1.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 170, 41, 31))
        self.label_2.setPixmap(QPixmap(u":/imgN1/img/login.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 220, 31, 31))
        self.label_3.setPixmap(QPixmap(u":/imgN1/img/padlock.png"))
        self.label_3.setScaledContents(True)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 170, 181, 22))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 230, 181, 22))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 300, 75, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 300, 101, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(270, 300, 81, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"DIGITE SEU LOGIN", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"DIGITE SUA SENHA", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"ENTRAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"CADASTRAR", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"BIOMETRIA", None))
    # retranslateUi

