# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajouterGestionnaire.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 488)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255);\n"
                                 "background-color:rgb(13,12,60)")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 751, 441))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(308, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:4px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(308, 242, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:4px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(127, 181, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setStyleSheet("color:rgb(70,68,68)")
        self.nomLabel.setObjectName("nomLabel")
        self.TeleLabel = QtWidgets.QLabel(Form)
        self.TeleLabel.setGeometry(QtCore.QRect(127, 242, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TeleLabel.setFont(font)
        self.TeleLabel.setStyleSheet("color:rgb(70,68,68)")
        self.TeleLabel.setObjectName("TeleLabel")
        self.idLabel = QtWidgets.QLabel(Form)
        self.idLabel.setGeometry(QtCore.QRect(127, 130, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idLabel.setFont(font)
        self.idLabel.setStyleSheet("color:rgb(70,68,68)")
        self.idLabel.setObjectName("idLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(308, 181, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:4px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(308, 302, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:4px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.adresseLabel = QtWidgets.QLabel(Form)
        self.adresseLabel.setGeometry(QtCore.QRect(127, 302, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setStyleSheet("color:rgb(70,68,68)")
        self.adresseLabel.setObjectName("adresseLabel")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                      " color:rgb(255, 255, 255);\n"
                                      "border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 0, 44, 42))
        self.pushButton_3.setStyleSheet("background-image:url(icons8-personne-homme-40.png);\n"
                                        "background-repeat: no-repeat;\n"
                                        "background-color:rgb(13,12,60)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate(
            "Form", "          Ajouter Un Gestionnaire"))
        self.nomLabel.setText(_translate("Form", "Nom Complet:"))
        self.TeleLabel.setText(_translate("Form", "Telephone:"))
        self.idLabel.setText(_translate("Form", "ID:"))
        self.adresseLabel.setText(_translate("Form", "Adresse:"))
        self.pushButton.setText(_translate("Form", "Valider"))
        self.pushButton_2.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
