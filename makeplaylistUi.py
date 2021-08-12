from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MakePlaylist(object):

    def __init__(self) :
        self.Dialog = QtWidgets.QDialog()
        self.setupUi()
        print("signup ui success")

    def setupUi(self):
        
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(332, 122)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.PutInPlaylistName = QtWidgets.QLineEdit(self.Dialog)
        self.PutInPlaylistName.setGeometry(QtCore.QRect(30, 30, 271, 31))
        self.PutInPlaylistName.setObjectName("lineEdit")

        self.retranslateUi(self.Dialog)
        self.buttonBox.accepted.connect(self.Dialog.accept)
        self.buttonBox.rejected.connect(self.Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "재생목록 생성"))
        self.PutInPlaylistName.setText(_translate("Dialog", "재생목록 1"))

