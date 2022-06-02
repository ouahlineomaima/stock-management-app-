# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajouterProduit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 40, 751, 411))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(13,12,60)")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 151, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 272, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 212, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:4px")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.quantiteLabel = QtWidgets.QLabel(Form)
        self.quantiteLabel.setGeometry(QtCore.QRect(159, 212, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.quantiteLabel.setFont(font)
        self.quantiteLabel.setStyleSheet("color:rgb(70,68,68)")
        self.quantiteLabel.setObjectName("quantiteLabel")
        self.prixLabel = QtWidgets.QLabel(Form)
        self.prixLabel.setGeometry(QtCore.QRect(159, 272, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.prixLabel.setFont(font)
        self.prixLabel.setStyleSheet("color:rgb(70,68,68)")
        self.prixLabel.setObjectName("prixLabel")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 320, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 197, 119);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:4px\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(159, 151, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nomLabel.setObjectName("nomLabel")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 320, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.idProduitLabel = QtWidgets.QLabel(Form)
        self.idProduitLabel.setGeometry(QtCore.QRect(159, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idProduitLabel.setFont(font)
        self.idProduitLabel.setStyleSheet("color:rgb(70,68,68)")
        self.idProduitLabel.setObjectName("idProduitLabel")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(340, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 0, 44, 42))
        self.pushButton_3.setStyleSheet("background-image:url(:/newPrefix/PFA Dev/icons8-personne-homme-40.png);\n"
"background-repeat: no-repeat;\n"
"background-color:rgb(13,12,60)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "          Ajouter Un Produit"))
        self.quantiteLabel.setText(_translate("Form", "Quanitite:"))
        self.prixLabel.setText(_translate("Form", "Prix Unitaire:"))
        self.pushButton_2.setText(_translate("Form", "Retour"))
        self.nomLabel.setText(_translate("Form", "Nom:"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.idProduitLabel.setText(_translate("Form", "ID Produit:"))

import ferf_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

