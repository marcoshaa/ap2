from PyQt5 import QtCore, QtGui, QtWidgets

class nivel1(object):
    def setupUi(self, level_1):
        level_1.setObjectName("level_1")
        level_1.resize(698, 640)
        level_1.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(level_1)
        self.centralwidget.setObjectName("centralwidget")
        self.intro_level1 = QtWidgets.QLabel(self.centralwidget)
        self.intro_level1.setGeometry(QtCore.QRect(180, 0, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.intro_level1.setFont(font)
        self.intro_level1.setObjectName("intro_level1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 481, 41))
        self.label.setMinimumSize(QtCore.QSize(351, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.voltaN1 = QtWidgets.QPushButton(self.centralwidget)
        self.voltaN1.setGeometry(QtCore.QRect(260, 560, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.voltaN1.setFont(font)
        self.voltaN1.setStyleSheet("background-color: rgb(0, 102, 0);\n"
"alternate-background-color: rgb(0, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.voltaN1.setObjectName("voltaN1")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 120, 611, 421))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 711, 691))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/imgN1/img/n1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.intro_level1.raise_()
        self.label.raise_()
        self.voltaN1.raise_()
        self.textEdit.raise_()
        level_1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(level_1)
        self.statusbar.setObjectName("statusbar")
        level_1.setStatusBar(self.statusbar)

        self.retranslateUi(level_1)
        QtCore.QMetaObject.connectSlotsByName(level_1)

    def retranslateUi(self, level_1):
        _translate = QtCore.QCoreApplication.translate
        level_1.setWindowTitle(_translate("level_1", "NIVEL 1"))
        self.intro_level1.setText(_translate("level_1", "Produção Agricola"))
        self.label.setText(_translate("level_1", "Conheça o Grupo Andre MAGGI"))
        self.voltaN1.setText(_translate("level_1", "voltar"))
        self.textEdit.setHtml(_translate("level_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    As atividades do grupo se inicou em São Miguel do Iguaçú (PR). Sua renda baseava-se em produção de soja, sementes e na comercialização de safras. Em 1979 com a aquisição de terras no Mato Grosso possibilitou a expansão de suas produçoes de soja e implementação do algodão e do milho a safras.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    Após a aquisição, o grupo mudo sua sede para Rondonópolis (MT), onde foi realizando aquisições de terras e aumentando o numero de fazendas. Atualmente o grupo conta com 10 fazendas apenas no territorio do Mato Grosso, estando nos municipios de; Sapezal, Campo Novo Dos Parecis, Querência, Itiquira e Rondonópolis.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    O grupo vem aumentando gradualmente o volume de suas safras. A nas safras 2016/2017, a Soja em uma área de 163 mil hectares produziu 569 toneladas; Semente de Soja em uma área de 10,20 mil hectares produziu 20,36 toneladas; Milho em uma área  de 63,24 mil hectares porduziu 357,48 toneladas; Algodão em uma área de 52,69 mil hectares produziu 233,17 toneladas.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    A empresa atualmente fornece para o mercado interno e externo, tendo frota de caminhões para o abastecimento interno, e possuindo rotas maritimas para exportação. A empresa AMAGGI na divisão agro são mais de 3.000 funcionarios entre produção e na comercialização.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    Com a demanda da expanção houve um aumento na frota dos maquinarios, na divisão agro possuem 30 colheitadeiras axial, 15 tratores, 15 plantadeiras de 24 linhase mais de 21 autopropelidos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
import imgN1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    level_1 = QtWidgets.QMainWindow()
    ui = nivel1()
    ui.setupUi(level_1)
    level_1.show()
    sys.exit(app.exec_())
