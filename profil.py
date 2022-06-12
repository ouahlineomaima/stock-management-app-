# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profil.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
import modifierNom
import ModifierTele
import modifierAdresse
import modifierEmail
import modifierPassword


def loaddata(self):
    gest = get_gestionnaire(Ui_Form.gestid)
    self.adresseLabel.setText(gest.address)
    self.teleLabel.setText(gest.telephone)
    self.passLabel.setText("*"*10)
    self.emailLabel.setText(gest.email)
    self.idlabel.setText(Ui_Form.gestid)
    self.nomLabel.setText(gest.nom_complet)


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def go_to_modify_name(self):
    try:
        modifierNom.Ui_Form.widget = Ui_Form.widget
        modifierNom.Ui_Form.previousheight = self.Form.frameGeometry().height()
        modifierNom.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        modifierNom.Ui_Form.previousindex = self.widget.currentIndex()
        modifierNom.Ui_Form.gestid = Ui_Form.gestid
        modifyname = modifierNom.Ui_Form()
        Ui_Form.widget.addWidget(modifyname.Form)
        Ui_Form.widget.setFixedWidth(modifyname.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(modifyname.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


def go_to_modify_tele(self):
    try:
        ModifierTele.Ui_Form.widget = Ui_Form.widget
        ModifierTele.Ui_Form.previousheight = self.Form.frameGeometry().height()
        ModifierTele.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        ModifierTele.Ui_Form.previousindex = self.widget.currentIndex()
        ModifierTele.Ui_Form.gestid = Ui_Form.gestid
        modifytele = ModifierTele.Ui_Form()
        Ui_Form.widget.addWidget(modifytele.Form)
        Ui_Form.widget.setFixedWidth(modifytele.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(modifytele.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


def go_to_modify_address(self):
    try:
        modifierAdresse.Ui_Form.widget = Ui_Form.widget
        modifierAdresse.Ui_Form.previousheight = self.Form.frameGeometry().height()
        modifierAdresse.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        modifierAdresse.Ui_Form.previousindex = self.widget.currentIndex()
        modifierAdresse.Ui_Form.gestid = Ui_Form.gestid
        modifyaddress = modifierAdresse.Ui_Form()
        Ui_Form.widget.addWidget(modifyaddress.Form)
        Ui_Form.widget.setFixedWidth(modifyaddress.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(modifyaddress.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


def go_to_modify_email(self):
    try:
        modifierEmail.Ui_Form.widget = Ui_Form.widget
        modifierEmail.Ui_Form.previousheight = self.Form.frameGeometry().height()
        modifierEmail.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        modifierEmail.Ui_Form.previousindex = self.widget.currentIndex()
        modifierEmail.Ui_Form.gestid = Ui_Form.gestid
        modifyemail = modifierEmail.Ui_Form()
        Ui_Form.widget.addWidget(modifyemail.Form)
        Ui_Form.widget.setFixedWidth(modifyemail.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(modifyemail.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


def go_to_modify_pswd(self):
    try:
        modifierPassword.Ui_Form.widget = Ui_Form.widget
        modifierPassword.Ui_Form.previousheight = self.Form.frameGeometry().height()
        modifierPassword.Ui_Form.previouswidth = self.Form.frameGeometry().width()
        modifierPassword.Ui_Form.previousindex = self.widget.currentIndex()
        modifierPassword.Ui_Form.gestid = Ui_Form.gestid
        modifypswd = modifierPassword.Ui_Form()
        Ui_Form.widget.addWidget(modifypswd.Form)
        Ui_Form.widget.setFixedWidth(modifypswd.Form.frameGeometry().width())
        Ui_Form.widget.setFixedHeight(modifypswd.Form.frameGeometry().height())
        Ui_Form.widget.setCurrentIndex(Ui_Form.widget.__len__() - 1)
    except BaseException as e:
        print(e)


class Ui_Form(object):
    widget = ""
    previousheight = ""
    previouswidth = ""
    previousindex = ""
    loginwidth = ""
    loginheight = ""
    gestid = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        loaddata(self)

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

        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 751, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(255, 255, 255);\n"
                                   "background-color:rgb(13,12,60)")
        self.label_20.setObjectName("label_20")

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
        self.idlabel.setGeometry(QtCore.QRect(370, 120, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idlabel.setFont(font)
        self.idlabel.setObjectName("idlabel")

        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(370, 160, 180, 31))
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
        self.adresseLabel.setGeometry(QtCore.QRect(370, 240, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setObjectName("adresseLabel")

        self.teleLabel = QtWidgets.QLabel(Form)
        self.teleLabel.setGeometry(QtCore.QRect(370, 200, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.teleLabel.setFont(font)
        self.teleLabel.setObjectName("teleLabel")

        self.passLabel = QtWidgets.QLabel(Form)
        self.passLabel.setGeometry(QtCore.QRect(370, 320, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")

        self.emailLabel = QtWidgets.QLabel(Form)
        self.emailLabel.setGeometry(QtCore.QRect(370, 280, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")

        self.modifierNombt = QtWidgets.QPushButton(Form)
        self.modifierNombt.setGeometry(QtCore.QRect(600, 160, 26, 26))
        self.modifierNombt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierNombt.setText("")
        self.modifierNombt.setObjectName("modifierNombt")
        self.modifierNombt.clicked.connect(lambda: go_to_modify_name(self))

        self.modifierAdresseBt = QtWidgets.QPushButton(Form)
        self.modifierAdresseBt.setGeometry(QtCore.QRect(600, 240, 26, 26))
        self.modifierAdresseBt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierAdresseBt.setText("")
        self.modifierAdresseBt.setObjectName("modifierAdresseBt")
        self.modifierAdresseBt.clicked.connect(lambda: go_to_modify_address(self))

        self.modifierTeelbt = QtWidgets.QPushButton(Form)
        self.modifierTeelbt.setGeometry(QtCore.QRect(600, 200, 26, 26))
        self.modifierTeelbt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierTeelbt.setText("")
        self.modifierTeelbt.setObjectName("modifierTeelbt")
        self.modifierTeelbt.clicked.connect(lambda: go_to_modify_tele(self))

        self.modifierpasswordbt = QtWidgets.QPushButton(Form)
        self.modifierpasswordbt.setGeometry(QtCore.QRect(600, 320, 26, 26))
        self.modifierpasswordbt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierpasswordbt.setText("")
        self.modifierpasswordbt.setObjectName("modifierpasswordbt")
        self.modifierpasswordbt.clicked.connect(lambda: go_to_modify_pswd(self))

        self.modifierEmailbt = QtWidgets.QPushButton(Form)
        self.modifierEmailbt.setGeometry(QtCore.QRect(600, 280, 26, 26))
        self.modifierEmailbt.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-crayon-23.png)")
        self.modifierEmailbt.setText("")
        self.modifierEmailbt.setObjectName("modifierEmailbt")
        self.modifierEmailbt.clicked.connect(lambda: go_to_modify_email(self))

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 380, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(35, 193, 228);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: loaddata(self))

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 380, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 197, 119);\n"
                                        " color:rgb(255, 255, 255);\n"
                                        "border-radius:4px")
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(lambda: go_back())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_20.setText(_translate("Form", "          Profil"))
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
        self.pushButton_3.setText(_translate("Form", "Retour"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Form = QtWidgets.QWidget()
    ui = Ui_Form()
    #ui.setupUi(Form)
    ui.Form.show()
    sys.exit(app.exec_())
