# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ruby(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 342)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-260, -150, 1251, 521))
        self.label.setStyleSheet("background-color:black")
        self.label.setObjectName("label")
        self.ani1 = QtWidgets.QLabel(Dialog)
        self.ani1.setGeometry(QtCore.QRect(180, 120, 131, 101))
        self.ani1.setStyleSheet("mix-blend-mode: lighten")
        self.ani1.setText("")
        self.ani1.setPixmap(QtGui.QPixmap("image_processing20210913-12239-1ov2meu.gif"))# remove this image and add your img name in same folder
        self.ani1.setScaledContents(True)
        self.ani1.setWordWrap(False)
        self.ani1.setObjectName("ani1")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(150, 280, 75, 23))
        self.start.setObjectName("start")
        self.quit = QtWidgets.QPushButton(Dialog)
        self.quit.setGeometry(QtCore.QRect(270, 280, 75, 23))
        self.quit.setObjectName("quit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ruby"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.start.setText(_translate("Dialog", "Start"))
        self.quit.setText(_translate("Dialog", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Ruby()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

