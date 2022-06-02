# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajouterService.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import ferf_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 488)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 751, 441))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(338, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(338, 240, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(338, 180, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:4px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.teleLabel = QtWidgets.QLabel(Form)
        self.teleLabel.setGeometry(QtCore.QRect(157, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teleLabel.setFont(font)
        self.teleLabel.setStyleSheet("color:rgb(70,68,68)")
        self.teleLabel.setObjectName("teleLabel")
        self.adresseLabel = QtWidgets.QLabel(Form)
        self.adresseLabel.setGeometry(QtCore.QRect(157, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setStyleSheet("color:rgb(70,68,68)")
        self.adresseLabel.setObjectName("adresseLabel")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(157, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nomLabel.setObjectName("nomLabel")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 290, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                      " color:rgb(255, 255, 255);\n"
                                      "border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "background-color:rgb(13,12,60)")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 0, 44, 42))
        self.pushButton_3.setStyleSheet("background-image:url(:/newPrefix/icons8-personne-homme-40.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-color:rgb(13,12,60)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.teleLabel.setText(_translate("Form", "Telephone:"))
        self.adresseLabel.setText(_translate("Form", "Adresse:"))
        self.pushButton_2.setText(_translate("Form", "Retour"))
        self.nomLabel.setText(_translate("Form", "Nom Complet:"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.label_3.setText(_translate(
            "Form", "          Ajouter Un Gestionnaire"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
