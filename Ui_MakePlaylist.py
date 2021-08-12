from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

class Ui_MakePlaylist(object):

    def __init__(self) :
        self.conn = sqlite3.connect('data.db')
        self.cur = self.conn.cursor()
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
        self.cur.execute("SELECT * FROM PlaylistTable ORDER BY ROWID DESC LIMIT 1") #마지막 재생목록 칼럼 불러오기
        result = self.cur.fetchall()
        playlistnum = str(int(result[0][0]) + 1) #맨앞 데이터 = 현재 생성된 데이터 

        self.PutInPlaylistName.setText(_translate("Dialog", "재생목록 "+(playlistnum)))