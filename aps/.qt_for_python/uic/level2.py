# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'level2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import imgN1_rc

class Ui_level_2(object):
    def setupUi(self, level_2):
        if not level_2.objectName():
            level_2.setObjectName(u"level_2")
        level_2.resize(701, 625)
        level_2.setStyleSheet(u"")
        self.centralwidget = QWidget(level_2)
        self.centralwidget.setObjectName(u"centralwidget")
        self.intro_level2 = QLabel(self.centralwidget)
        self.intro_level2.setObjectName(u"intro_level2")
        self.intro_level2.setGeometry(QRect(0, -10, 701, 601))
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.intro_level2.setFont(font)
        self.intro_level2.setStyleSheet(u"")
        self.intro_level2.setPixmap(QPixmap(u":/imgN1/img/n2.jpg"))
        self.intro_level2.setScaledContents(True)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 80, 651, 391))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(12)
        self.textBrowser.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 30, 291, 41))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.voltaN2 = QPushButton(self.centralwidget)
        self.voltaN2.setObjectName(u"voltaN2")
        self.voltaN2.setGeometry(QRect(250, 510, 141, 41))
        font3 = QFont()
        font3.setPointSize(20)
        self.voltaN2.setFont(font3)
        self.voltaN2.setStyleSheet(u"background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        level_2.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(level_2)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 701, 21))
        level_2.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(level_2)
        self.statusbar.setObjectName(u"statusbar")
        level_2.setStatusBar(self.statusbar)

        self.retranslateUi(level_2)

        QMetaObject.connectSlotsByName(level_2)
    # setupUi

    def retranslateUi(self, level_2):
        level_2.setWindowTitle(QCoreApplication.translate("level_2", u"MainWindow", None))
        self.intro_level2.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("level_2", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Times New Roman'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Incentivos fiscais de imposto de renda</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">	A Empresa e sua controlada Hermasa Navega\u00e7\u00e3o da Amaz\u00f4nia Ltda, s\u00e3o benefici\u00e1"
                        "rias de incentivos fiscais de imposto de renda. Os incenticos foram concedidos pela Suprerintend\u00eancia de Desenvolvimento da Amaz\u00f4nia(SUDAM), at\u00e9 2028, e consistem no direito \u00e0 redu\u00e7\u00e3o de 75% do imposto de renda e adicional n\u00e3o reembols\u00e1vel calculado sobre o lucro tribut\u00e1rio nas atividades de transporte e transbordo de gr\u00e3os, armazenagem, servi\u00e7os portu\u00e1rios, importa\u00e7\u00e3o e comercioaliza\u00e7\u00e3o de fertilizantes, extra\u00e7\u00e3o e comercializa\u00e7\u00e3o de \u00f3leo de soja bruto e degomado e farelo de soja. O incentivo promove investimento em projetos de instala\u00e7\u00e3o, expans\u00e3o, moderniza\u00e7\u00e3o ou diverfifica\u00e7\u00e3o na regi\u00e3o.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">	O imposto de renda \u00e9 apurado de acordo com a legisla\u00e7\u00e3o fiscal vigente e a parcela"
                        " relativa ao beneficio \u00e9 registrada em contrapartida de uma conta de resultado.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">	Impostos de 2020 pagos pelo Grupo;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Resultado antes do imposto de renda e da consolida\u00e7\u00e3o social no periodo de 2020 = 1.312.471</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px"
                        "; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Al\u00edquotas fiscais combinadas  34% = 446.240</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">(+/-) Ajustes dos impostos referente:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Deprecia\u00e7\u00e3o derivada de custo atribu\u00eddo = 216</span>"
                        "</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Efeito de convers\u00e3o para moeda de apresenta\u00e7\u00e3o = 227.659</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Resultado de equival\u00eancia patrimonial = 114.398</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Deprecia\u00e7\u00e3o incentivada na aquisi\u00e7\u00e3o de imobilizados = 545</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Resultado de investimentos no exterior = 26.809</span></p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Perdas na realiza\u00e7\u00e3o de investimentos = 2.390</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Multas n\u00e3o dedut\u00edveis = 121</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Subs\u00eddios governamentais = 23.871</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Provis\u00f5es e revers\u00f5es receitas = 100</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fami"
                        "ly:'MS Shell Dlg 2';\">Estorno e credito de imposto = 6.504</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Deprecia\u00e7\u00e3o fiscal x vida \u00fatil econ\u00f4mica = 469</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Outras adi\u00e7\u00f5es/exclus\u00f5es = 2.297</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Total = (100.639)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margi"
                        "n-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">(+/-)Imposto de renda e contribui\u00e7\u00e3o diferidos = 188.926</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">(-) Imposto de renda e contribui\u00e7\u00e3o correntes = (289.565)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">(=) Imposto de renda e contribui\u00e7\u00e3o no resultado = (100.639)</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("level_2", u"  INFORMA\u00c7\u00c3O FISCAL", None))
        self.voltaN2.setText(QCoreApplication.translate("level_2", u"voltar", None))
    # retranslateUi

