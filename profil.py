# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profil.ui'
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
        self.label.setGeometry(QtCore.QRect(0, 50, 751, 401))
        self.label.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 51))
        self.label_2.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 111, 111))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-image:url(:/newPrefix/icons8-personne-homme-100.png);\n"
                                      "background-color:url(icons8-personne-homme-40.png);\n"
                                      "background-repeat: no-repeat;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.idlabel = QtWidgets.QLabel(Form)
        self.idlabel.setGeometry(QtCore.QRect(370, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName("idlabel")
        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(370, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setObjectName("nomLabel")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(370, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(370, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(200, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(200, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(200, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(200, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.adresseLabel = QtWidgets.QLabel(Form)
        self.adresseLabel.setGeometry(QtCore.QRect(370, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setObjectName("adresseLabel")
        self.teleLabel = QtWidgets.QLabel(Form)
        self.teleLabel.setGeometry(QtCore.QRect(370, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teleLabel.setFont(font)
        self.teleLabel.setObjectName("teleLabel")
        self.passLabel = QtWidgets.QLabel(Form)
        self.passLabel.setGeometry(QtCore.QRect(370, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")
        self.emailLabel = QtWidgets.QLabel(Form)
        self.emailLabel.setGeometry(QtCore.QRect(370, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.modiferidbtn = QtWidgets.QPushButton(Form)
        self.modiferidbtn.setGeometry(QtCore.QRect(520, 120, 26, 26))
        self.modiferidbtn.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modiferidbtn.setText("")
        self.modiferidbtn.setObjectName("modiferidbtn")
        self.modifierNombt = QtWidgets.QPushButton(Form)
        self.modifierNombt.setGeometry(QtCore.QRect(520, 160, 26, 26))
        self.modifierNombt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierNombt.setText("")
        self.modifierNombt.setObjectName("modifierNombt")
        self.modifierAdresseBt = QtWidgets.QPushButton(Form)
        self.modifierAdresseBt.setGeometry(QtCore.QRect(520, 240, 26, 26))
        self.modifierAdresseBt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierAdresseBt.setText("")
        self.modifierAdresseBt.setObjectName("modifierAdresseBt")
        self.modifierTeelbt = QtWidgets.QPushButton(Form)
        self.modifierTeelbt.setGeometry(QtCore.QRect(520, 200, 26, 26))
        self.modifierTeelbt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierTeelbt.setText("")
        self.modifierTeelbt.setObjectName("modifierTeelbt")
        self.modifierpasswordbt = QtWidgets.QPushButton(Form)
        self.modifierpasswordbt.setGeometry(QtCore.QRect(520, 320, 26, 26))
        self.modifierpasswordbt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierpasswordbt.setText("")
        self.modifierpasswordbt.setObjectName("modifierpasswordbt")
        self.modifierEmailbt = QtWidgets.QPushButton(Form)
        self.modifierEmailbt.setGeometry(QtCore.QRect(520, 280, 26, 26))
        self.modifierEmailbt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierEmailbt.setText("")
        self.modifierEmailbt.setObjectName("modifierEmailbt")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 380, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Id Gestionnaire:"))
        self.idlabel.setText(_translate("Form", "1"))
        self.nomLabel.setText(_translate("Form", "Omaima ouahline"))
        self.label_6.setText(_translate("Form", "Nom Complet:"))
        self.label_9.setText(_translate("Form", "Adresse:"))
        self.label_10.setText(_translate("Form", "Téléphone:"))
        self.label_11.setText(_translate("Form", "E-mail:"))
        self.label_12.setText(_translate("Form", "Password:"))
        self.adresseLabel.setText(_translate("Form", "rabat"))
        self.teleLabel.setText(_translate("Form", "06 12 20 27 83"))
        self.passLabel.setText(_translate("Form", "**************"))
        self.emailLabel.setText(_translate("Form", "nom@gmail.com"))
        self.pushButton_2.setText(_translate("Form", "Actualiser"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())