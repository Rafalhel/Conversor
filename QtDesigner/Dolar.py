# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dolar.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Conversor(object):
    def setupUi(self, Conversor):
        Conversor.setObjectName("Conversor")
        Conversor.setWindowModality(QtCore.Qt.WindowModal)
        Conversor.setEnabled(True)
        Conversor.resize(430, 148)
        self.centralwidget = QtWidgets.QWidget(Conversor)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 111, 20))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 50, 121, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 50, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 121, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 21, 16))
        self.label_3.setObjectName("label_3")
        Conversor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Conversor)
        self.statusbar.setObjectName("statusbar")
        Conversor.setStatusBar(self.statusbar)

        self.retranslateUi(Conversor)
        QtCore.QMetaObject.connectSlotsByName(Conversor)
        self.setFixedSize(460, 150)

    def retranslateUi(self, Conversor):
        _translate = QtCore.QCoreApplication.translate
        Conversor.setWindowTitle(_translate("Conversor", "Conversor"))
        self.lineEdit.setPlaceholderText(_translate("Conversor", "Valor a ser convertido"))
        self.comboBox.setItemText(0, _translate("Conversor", "Dolar"))
        self.comboBox.setItemText(1, _translate("Conversor", "Euro"))
        self.comboBox.setItemText(2, _translate("Conversor", "Bitcoin"))
        self.pushButton.setText(_translate("Conversor", "Converter"))
        self.label_3.setText(_translate("Conversor", "R$"))
