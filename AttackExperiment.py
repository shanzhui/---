# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AttackExperiment.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 361, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout_2.addWidget(self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_2.addWidget(self.spinBox)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 260, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 170, 381, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 210, 321, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_3.addWidget(self.checkBox_6)
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_3.addWidget(self.checkBox_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Run Experiment"))
        self.checkBox.setText(_translate("Form", "更新攻击"))
        self.checkBox_2.setText(_translate("Form", "删除攻击"))
        self.checkBox_3.setText(_translate("Form", "随机攻击"))
        self.checkBox_4.setText(_translate("Form", "添加攻击"))
        self.checkBox_6.setText(_translate("Form", "遍历ratio"))
        self.checkBox_5.setText(_translate("Form", "遍历lsb"))
