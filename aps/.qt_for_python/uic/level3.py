# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'level3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import imgN1_rc

class Ui_level_3(object):
    def setupUi(self, level_3):
        if not level_3.objectName():
            level_3.setObjectName(u"level_3")
        level_3.resize(800, 574)
        level_3.setStyleSheet(u"")
        self.centralwidget = QWidget(level_3)
        self.centralwidget.setObjectName(u"centralwidget")
        self.intro_Level3 = QLabel(self.centralwidget)
        self.intro_Level3.setObjectName(u"intro_Level3")
        self.intro_Level3.setGeometry(QRect(-10, 0, 801, 571))
        font = QFont()
        font.setPointSize(50)
        self.intro_Level3.setFont(font)
        self.intro_Level3.setStyleSheet(u"")
        self.intro_Level3.setPixmap(QPixmap(u":/imgN1/img/n3.jpg"))
        self.intro_Level3.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 181, 51))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 110, 541, 401))
        font2 = QFont()
        font2.setPointSize(12)
        self.textBrowser.setFont(font2)
        self.voltaN3 = QPushButton(self.centralwidget)
        self.voltaN3.setObjectName(u"voltaN3")
        self.voltaN3.setGeometry(QRect(600, 300, 141, 41))
        font3 = QFont()
        font3.setPointSize(20)
        self.voltaN3.setFont(font3)
        self.voltaN3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        level_3.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(level_3)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        level_3.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(level_3)
        self.statusbar.setObjectName(u"statusbar")
        level_3.setStatusBar(self.statusbar)

        self.retranslateUi(level_3)

        QMetaObject.connectSlotsByName(level_3)
    # setupUi

    def retranslateUi(self, level_3):
        level_3.setWindowTitle(QCoreApplication.translate("level_3", u"MainWindow", None))
        self.intro_Level3.setText("")
        self.label.setText(QCoreApplication.translate("level_3", u" Agrot\u00f3xico", None))
        self.textBrowser.setHtml(QCoreApplication.translate("level_3", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	O grupo AMAGGI n\u00e3o faz apenas o consumo de agrot\u00f3ximos como o Glisofato; eles realizam a venda de produtos para reabiliar o solo e manuten\u00e7\u00e3o da planta\u00e7\u00e3o. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Prdutos Quimicos utilizados:<br /><span style=\" font-family:'Ubuntu','Helvetica','A"
                        "rial','sans-serif'; font-weight:296; color:#363636; background-color:#ffffff;\">\u2013 Hexano</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Poliuretano</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Glifosfato</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Aflatoxina</span></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0\u00c1cido Clor\u00eddrico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0\u00c1lcool Et\u00edlico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Solu\u00e7\u00e3o Acet\u00f4nica</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px;"
                        " margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0\u00c1cido Sulf\u00farico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Eter Petr\u00f3leo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Hidr\u00f3xido S\u00f3dio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0NO2 Am\u00f4nia</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0\u00c1cido Sulfonico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Hipoclorito S\u00f3dio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-fami"
                        "ly:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0\u00c1lcool Met\u00edlico</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Cloreto Trifeniltetra</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; color:#363636;\">\u2013\u00a0Hidr\u00f3xido S\u00f3dio</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:150%; background-color:#ffffff;\"><span style=\" font-family:'Ubuntu','Helvetica','Arial','sans-serif'; font-weight:296; "
                        "color:#363636;\">\u2013\u00a0Iodeto Pot\u00e1ssio</span></p></body></html>", None))
        self.voltaN3.setText(QCoreApplication.translate("level_3", u"voltar", None))
    # retranslateUi

