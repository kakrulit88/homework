# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/edit_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(400, 313)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)
        self.degree_of_roasting_lineEdit = QtWidgets.QLineEdit(Form1)
        self.degree_of_roasting_lineEdit.setObjectName("degree_of_roasting_lineEdit")
        self.gridLayout.addWidget(self.degree_of_roasting_lineEdit, 3, 0, 1, 1)
        self.volume_lineEdit = QtWidgets.QLineEdit(Form1)
        self.volume_lineEdit.setObjectName("volume_lineEdit")
        self.gridLayout.addWidget(self.volume_lineEdit, 11, 0, 1, 1)
        self.ground_or_beans_lineEdit = QtWidgets.QLineEdit(Form1)
        self.ground_or_beans_lineEdit.setObjectName("ground_or_beans_lineEdit")
        self.gridLayout.addWidget(self.ground_or_beans_lineEdit, 5, 0, 1, 1)
        self.price_lineEdit = QtWidgets.QLineEdit(Form1)
        self.price_lineEdit.setObjectName("price_lineEdit")
        self.gridLayout.addWidget(self.price_lineEdit, 9, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(Form1)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout.addWidget(self.name_lineEdit, 1, 0, 1, 1)
        self.description_of_taste_lineEdit = QtWidgets.QLineEdit(Form1)
        self.description_of_taste_lineEdit.setObjectName("description_of_taste_lineEdit")
        self.gridLayout.addWidget(self.description_of_taste_lineEdit, 7, 0, 1, 1)
        self.save_pushButton = QtWidgets.QPushButton(Form1)
        self.save_pushButton.setObjectName("save_pushButton")
        self.gridLayout.addWidget(self.save_pushButton, 12, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Form"))
        self.label_3.setText(_translate("Form1", "молотый/в зернах"))
        self.label_4.setText(_translate("Form1", "описание вкуса"))
        self.label_5.setText(_translate("Form1", "цена"))
        self.label_6.setText(_translate("Form1", "объем упаковки"))
        self.label.setText(_translate("Form1", "название сорта"))
        self.label_2.setText(_translate("Form1", "степень обжарки"))
        self.save_pushButton.setText(_translate("Form1", "Сохранить"))
