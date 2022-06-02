# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichageGestionnaire.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 451)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 761, 451))
        self.label_2.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(610, 120, 131, 32))
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
        self.label_3.setStyleSheet("background-color:rgb(13,12,60)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 10, 151, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color:rgb(255, 197, 119);\n"
" color:rgb(255, 255, 255);\n"
"border-radius:4px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 571, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(690, 0, 44, 42))
        self.pushButton_7.setStyleSheet("background-image:url(:/newPrefix/PFA Dev/icons8-personne-homme-40.png);\n"
"background-repeat: no-repeat;\n"
"background-color:rgb(13,12,60)")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Consulter"))
        self.pushButton_9.setText(_translate("Form", "Se Deconnecter"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Service"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nom"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

