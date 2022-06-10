# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifierProduitGestionnaire.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)
        self.titlelabel = QtWidgets.QLabel(Form)
        self.titlelabel.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titlelabel.setFont(font)
        self.titlelabel.setStyleSheet("color:rgb(255, 255, 255);\n"
                                      "background-color:rgb(13,12,60)")
        self.titlelabel.setObjectName("titlelabel")
        self.iconeProfil = QtWidgets.QPushButton(Form)
        self.iconeProfil.setGeometry(QtCore.QRect(690, 0, 44, 42))
        self.iconeProfil.setStyleSheet("background-image:url(:/newPrefix/icons8-personne-homme-40.png);\n"
                                       "background-repeat: no-repeat;\n"
                                       "background-color:rgb(13,12,60)")
        self.iconeProfil.setText("")
        self.iconeProfil.setObjectName("iconeProfil")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 751, 401))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(360, 320, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:4px")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 80, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.nvMaxLabel_2 = QtWidgets.QLabel(Form)
        self.nvMaxLabel_2.setGeometry(QtCore.QRect(150, 320, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvMaxLabel_2.setFont(font)
        self.nvMaxLabel_2.setStyleSheet("color:rgb(70,68,68)")
        self.nvMaxLabel_2.setObjectName("nvMaxLabel_2")
        self.nvQuantiteLabel = QtWidgets.QLabel(Form)
        self.nvQuantiteLabel.setGeometry(QtCore.QRect(150, 140, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvQuantiteLabel.setFont(font)
        self.nvQuantiteLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nvQuantiteLabel.setObjectName("nvQuantiteLabel")
        self.nvMinLabel_2 = QtWidgets.QLabel(Form)
        self.nvMinLabel_2.setGeometry(QtCore.QRect(150, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvMinLabel_2.setFont(font)
        self.nvMinLabel_2.setStyleSheet("color:rgb(70,68,68)")
        self.nvMinLabel_2.setObjectName("nvMinLabel_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius:4px")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.nvNomLabel = QtWidgets.QLabel(Form)
        self.nvNomLabel.setGeometry(QtCore.QRect(150, 90, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvNomLabel.setFont(font)
        self.nvNomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nvNomLabel.setObjectName("nvNomLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.nvPrixLabel = QtWidgets.QLabel(Form)
        self.nvPrixLabel.setGeometry(QtCore.QRect(150, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nvPrixLabel.setFont(font)
        self.nvPrixLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nvPrixLabel.setObjectName("nvPrixLabel")
        self.retourButton = QtWidgets.QPushButton(Form)
        self.retourButton.setGeometry(QtCore.QRect(470, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.retourButton.setFont(font)
        self.retourButton.setStyleSheet("QPushButton{\n"
                                        "background-color:rgb(255, 197, 119);\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "border-radius:4px\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.retourButton.setObjectName("retourButton")
        self.validerButton = QtWidgets.QPushButton(Form)
        self.validerButton.setGeometry(QtCore.QRect(150, 380, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.validerButton.setFont(font)
        self.validerButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                         " color:rgb(255, 255, 255);\n"
                                         "border-radius:4px")
        self.validerButton.setObjectName("validerButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titlelabel.setText(_translate(
            "Form", "          Modifier Un Produit"))
        self.nvMaxLabel_2.setText(_translate("Form", "Nouveau Max:"))
        self.nvQuantiteLabel.setText(_translate("Form", "Nouvelle Quantité:"))
        self.nvMinLabel_2.setText(_translate("Form", "Nouveau Min:"))
        self.nvNomLabel.setText(_translate("Form", "Nouveau Nom:"))
        self.nvPrixLabel.setText(_translate("Form", "Nouveau Prix :"))
        self.retourButton.setText(_translate("Form", "Retour"))
        self.validerButton.setText(_translate("Form", "Valider"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
