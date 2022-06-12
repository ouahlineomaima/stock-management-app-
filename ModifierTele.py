# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifierTele.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
from PyQt5.QtWidgets import *


def loaddata(self):
    gest = get_gestionnaire(Ui_Form.gestid)
    self.adresseLabel.setText(gest.address)
    self.nomLabel.setText(gest.nom_complet)
    self.passLabel.setText("*"*10)
    self.EmailLabel.setText(gest.email)
    self.idLabel.setText(Ui_Form.gestid)
    self.teletextfield.setText(gest.telephone)


def go_back():
    Ui_Form.widget.setFixedWidth(Ui_Form.previouswidth)
    Ui_Form.widget.setFixedHeight(Ui_Form.previousheight)
    Ui_Form.widget.setCurrentIndex(Ui_Form.previousindex)


def validate(self):
    try:
        gest = get_gestionnaire(Ui_Form.gestid)
        tele = self.teletextfield.text()
        x = int(tele)
        if tele == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Veuillez saisir d'abord un numéro de téléphone.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
        elif len(tele) != 10:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Veuillez saisir 10 chiffres exactement.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
        elif not tele.startswith("05", 0, 2) and not tele.startswith("06", 0, 2) and not tele.startswith("07", 0, 2):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Veuillez saisir un numéro valide.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
        elif tele == gest.telephone:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText(
                "Vous n'avez effectuer aucun changement. Veuillez changer le telephone ou cliquer sur le boutton retour.")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
        else:
            cursor, db = get_connection()
            request = f"UPDATE `gestionstock`.`gestionnaire` SET `telephone` = '{tele}' WHERE (`idgestionnaire` = '{Ui_Form.gestid}')"
            cursor.execute(request)
            db.commit()
            cursor.close()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            # setting message for Message Box
            msg.setText("Votre nom a été changé avec succès.")

            # setting Message box window title
            msg.setWindowTitle("Opération réussie")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()
            go_back()
    except BaseException as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        # setting message for Message Box
        msg.setText("Veuillez saisir que des chiffres.")

        # setting Message box window title
        msg.setWindowTitle("Opération échouée")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()


class Ui_Form(object):
    widget = ""
    previousheight = ""
    previouswidth = ""
    previousindex = ""
    gestid = ""

    def __init__(self):
        self.Form = QtWidgets.QWidget()
        self.setupUi(self.Form)
        loaddata(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 50, 751, 451))
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

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(200, 200, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(200, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.passLabel = QtWidgets.QLabel(Form)
        self.passLabel.setGeometry(QtCore.QRect(370, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passLabel.setFont(font)
        self.passLabel.setObjectName("passLabel")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(200, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(200, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.nomLabel = QtWidgets.QLabel(Form)
        self.nomLabel.setGeometry(QtCore.QRect(370, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nomLabel.setFont(font)
        self.nomLabel.setObjectName("nomLabel")

        self.idLabel = QtWidgets.QLabel(Form)
        self.idLabel.setGeometry(QtCore.QRect(370, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")

        self.EmailLabel = QtWidgets.QLabel(Form)
        self.EmailLabel.setGeometry(QtCore.QRect(370, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.EmailLabel.setFont(font)
        self.EmailLabel.setObjectName("EmailLabel")

        self.adresseLabel = QtWidgets.QLabel(Form)
        self.adresseLabel.setGeometry(QtCore.QRect(370, 240, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.adresseLabel.setFont(font)
        self.adresseLabel.setObjectName("adresseLabel")

        self.teletextfield = QtWidgets.QLineEdit(Form)
        self.teletextfield.setGeometry(QtCore.QRect(370, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.teletextfield.setFont(font)
        self.teletextfield.setStyleSheet("border-radius:4px")
        self.teletextfield.setObjectName("teletextfield")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 200, 26, 26))
        self.pushButton_2.setStyleSheet(
            "background-image:url(:/newPrefix/icons8-coche-23.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: validate(self))

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 380, 151, 32))
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
        self.label_6.setText(_translate("Form", "Nom Complet:"))
        self.label_3.setText(_translate("Form", "Id Gestionnaire:"))
        self.label_10.setText(_translate("Form", "Téléphone:"))
        self.label_12.setText(_translate("Form", "Password:"))
        self.passLabel.setText(_translate("Form", "**************"))
        self.label_9.setText(_translate("Form", "Adresse:"))
        self.label_11.setText(_translate("Form", "E-mail:"))
        self.nomLabel.setText(_translate("Form", "Omaima Ouahline"))
        self.idLabel.setText(_translate("Form", "1"))
        self.EmailLabel.setText(_translate("Form", "nom@gmail.com"))
        self.adresseLabel.setText(_translate("Form", "rabat"))
        self.pushButton_3.setText(_translate("Form", "Retour"))
        self.label_20.setText(_translate("Form", "          Profil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Form = QtWidgets.QWidget()
    ui = Ui_Form()
    #ui.setupUi(Form)
    Ui_Form.Form.show()
    sys.exit(app.exec_())
