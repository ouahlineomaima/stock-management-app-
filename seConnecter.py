# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seConnecter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Data import *
import hashlib
import sys
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 491)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 451, 491))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(450, 0, 301, 491))
        self.label_3.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(54, 54, 54)")
        self.label.setObjectName("label")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(70,68,68)")
        self.label_4.setObjectName("label_4")

        self.idfield = QtWidgets.QLineEdit(Form)
        self.idfield.setGeometry(QtCore.QRect(170, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.idfield.setFont(font)
        self.idfield.setStyleSheet("border-radius:4px")
        self.idfield.setObjectName("idfield")

        self.nomfield = QtWidgets.QLineEdit(Form)
        self.nomfield.setGeometry(QtCore.QRect(170, 190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nomfield.setFont(font)
        self.nomfield.setStyleSheet("border-radius:4px")
        self.nomfield.setObjectName("nomfield")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(70,68,68)")
        self.label_5.setObjectName("label_5")

        self.passwordfield = QtWidgets.QLineEdit(Form)
        self.passwordfield.setGeometry(QtCore.QRect(170, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.passwordfield.setFont(font)
        self.passwordfield.setStyleSheet("border-radius:4px")
        self.passwordfield.setObjectName("passwordfield")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 260, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(70,68,68)")
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 350, 191, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(85, 255, 0);\n"
                                      " color:rgb(255, 255, 255);\n"
                                      "border-radius:4px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sign_in)

        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(570, 220, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(85, 255, 0);")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(540, 240, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(255,255,255)")
        self.label_9.setObjectName("label_9")

        self.imageLabel = QtWidgets.QLabel(Form)
        self.imageLabel.setGeometry(QtCore.QRect(520, 30, 161, 141))
        self.imageLabel.setAutoFillBackground(False)
        self.imageLabel.setStyleSheet("background-image:url(:/newPrefix/supermarcher.jpg);\n"
                                      "border-radius:40px")
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap(":/newPrefix/supermarket.png"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def sign_in(self):
        id = self.idfield.text()
        nom = self.nomfield.text()
        passwd = self.passwordfield.text()
        gest = get_gestionnaire(id)
        if gest is not None:
            if nom == gest.nom_complet:
                if hashlib.md5(passwd.encode()).hexdigest() == gest.password:
                    if id == "0000":  # admin part
                        pass
                    else:  # normal gest part
                        pass
                else:  # wrong passwd
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)

                    # setting message for Message Box
                    msg.setText("Mot de pass incorrect")

                    # setting Message box window title
                    msg.setWindowTitle("Opération échouée")

                    # declaring buttons on Message Box
                    msg.setStandardButtons(QMessageBox.Ok)

                    # start the app
                    retval = msg.exec_()
            else:  # wrong name
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)

                # setting message for Message Box
                msg.setText("Nom incorrect")

                # setting Message box window title
                msg.setWindowTitle("Opération échouée")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()
        else:  # wrong information
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            # setting message for Message Box
            msg.setText("Aucun gestionnaire ne correspond à l'id saisi")

            # setting Message box window title
            msg.setWindowTitle("Opération échouée")

            # declaring buttons on Message Box
            msg.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg.exec_()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Authentification"))
        self.label_4.setText(_translate("Form", "ID:"))
        self.label_5.setText(_translate("Form", "Nom Complet:"))
        self.label_6.setText(_translate("Form", "Mot de Passe:"))
        self.pushButton.setText(_translate("Form", "Se Connecter "))
        self.label_8.setText(_translate("Form", "Ou&Ta"))
        self.label_9.setText(_translate("Form", "Supermarket"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
