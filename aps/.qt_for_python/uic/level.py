# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'level.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import imgN1_rc

class Ui_level_1(object):
    def setupUi(self, level_1):
        if not level_1.objectName():
            level_1.setObjectName(u"level_1")
        level_1.resize(698, 640)
        level_1.setStyleSheet(u"")
        self.centralwidget = QWidget(level_1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.intro_level1 = QLabel(self.centralwidget)
        self.intro_level1.setObjectName(u"intro_level1")
        self.intro_level1.setGeometry(QRect(180, 0, 321, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.intro_level1.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 481, 41))
        self.label.setMinimumSize(QSize(351, 0))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.voltaN1 = QPushButton(self.centralwidget)
        self.voltaN1.setObjectName(u"voltaN1")
        self.voltaN1.setGeometry(QRect(260, 560, 141, 41))
        font2 = QFont()
        font2.setPointSize(20)
        self.voltaN1.setFont(font2)
        self.voltaN1.setStyleSheet(u"background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 120, 611, 421))
        self.textEdit.setStyleSheet(u"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 0, 711, 691))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/imgN1/img/n1.png"))
        self.label_2.setScaledContents(True)
        level_1.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.intro_level1.raise_()
        self.label.raise_()
        self.voltaN1.raise_()
        self.textEdit.raise_()
        self.statusbar = QStatusBar(level_1)
        self.statusbar.setObjectName(u"statusbar")
        level_1.setStatusBar(self.statusbar)

        self.retranslateUi(level_1)

        QMetaObject.connectSlotsByName(level_1)
    # setupUi

    def retranslateUi(self, level_1):
        level_1.setWindowTitle(QCoreApplication.translate("level_1", u"MainWindow", None))
        self.intro_level1.setText(QCoreApplication.translate("level_1", u"Produ\u00e7\u00e3o Agricola", None))
        self.label.setText(QCoreApplication.translate("level_1", u"Conhe\u00e7a o Grupo Andre MAGGI", None))
        self.voltaN1.setText(QCoreApplication.translate("level_1", u"voltar", None))
        self.textEdit.setHtml(QCoreApplication.translate("level_1", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">	As atividades do grupo se inicou em S\u00e3o Miguel do Igua\u00e7\u00fa (PR). Sua renda baseava-se em produ\u00e7\u00e3o de soja, sementes e na comercializa\u00e7\u00e3o de safras. Em 1979 com a aquisi\u00e7\u00e3o de terras no Mato Grosso possibilitou a expans\u00e3o de suas produ\u00e7oes de soja e implementa\u00e7\u00e3o do algod\u00e3o e do milho a safras.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font"
                        "-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">	Ap\u00f3s a aquisi\u00e7\u00e3o, o grupo mudo sua sede para Rondon\u00f3polis (MT), onde foi realizando aquisi\u00e7\u00f5es de terras e aumentando o numero de fazendas. Atualmente o grupo conta com 10 fazendas apenas no territorio do Mato Grosso, estando nos municipios de; Sapezal, Campo Novo Dos Parecis, Quer\u00eancia, Itiquira e Rondon\u00f3polis.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">	O grupo vem aumentando gradualmente o volume de suas safras. A nas safras 2016/2017, a Soja em uma \u00e1rea de 163 mil hectares produziu 56"
                        "9 toneladas; Semente de Soja em uma \u00e1rea de 10,20 mil hectares produziu 20,36 toneladas; Milho em uma \u00e1rea  de 63,24 mil hectares porduziu 357,48 toneladas; Algod\u00e3o em uma \u00e1rea de 52,69 mil hectares produziu 233,17 toneladas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">	A empresa atualmente fornece para o mercado interno e externo, tendo frota de caminh\u00f5es para o abastecimento interno, e possuindo rotas maritimas para exporta\u00e7\u00e3o. A empresa AMAGGI na divis\u00e3o agro s\u00e3o mais de 3.000 funcionarios entre produ\u00e7\u00e3o e na comercializa\u00e7\u00e3o.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-size:14pt;\">	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">	Com a demanda da expan\u00e7\u00e3o houve um aumento na frota dos maquinarios, na divis\u00e3o agro possuem 30 colheitadeiras axial, 15 tratores, 15 plantadeiras de 24 linhase mais de 21 autopropelidos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.label_2.setText("")
    # retranslateUi

