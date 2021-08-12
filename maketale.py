import sqlite3
import Ui_MakePlaylist
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class classMakeTable : 
    def __init__(self) :
        #데이터 연결
        self.conn = sqlite3.connect('data.db')
        self.cur = self.conn.cursor()

        self.makeplaylistUi = Ui_MakePlaylist.Ui_MakePlaylist() #재생목록이름 정하는 팝업창 UI
        self.makeplaylistUi.buttonBox.accepted.connect(self.makeplaylistURLTable)


    def makeplaylistTable(self) : #베이스 테이블 제작 부분
        self.cur.execute("CREATE TABLE PlaylistTable (plylistnumber TEXT PRIMARY KEY, playlistname TEXT)") #재생목록 생성 관련 db
        self.conn.commit()
        self.conn.close()
        

    def makeplaylistURLTable_ONLYFRIST(self) : #재생목록 만드는 함수 맨처음만 실행
        playlistnameValue = str(self.makeplaylistUi.PutInPlaylistName.text()) #입력된 재생목록 이름을 저장하는 지역변수
        print(playlistnameValue) #확인 문구

        self.cur.execute("INSERT INTO PlaylistTable VALUES('1', '" +playlistnameValue+ "')")
        self.cur.execute("CREATE TABLE '" + playlistnameValue + "' (videonumber TEXT PRIMARY KEY, videourl TEXT)") #재생목록 테이블 만들기
        self.conn.commit()
        self.conn.close()


    def makeplaylistURLTable(self) : #재생목록 만드는 함수
        playlistnameValue = str(self.makeplaylistUi.PutInPlaylistName.text()) #입력된 재생목록 이름을 저장하는 지역변수
        print(playlistnameValue) #확인 문구
        self.cur.execute("SELECT * FROM PlaylistTable ORDER BY ROWID DESC LIMIT 1") #마지막 재생목록 칼럼 불러오기
        result = self.cur.fetchall()
        playlistnum = str(int(result[0][0]) + 1) #맨앞 데이터 = 현재 생성된 데이터 

        self.cur.execute("INSERT INTO PlaylistTable VALUES('" +playlistnum+ "', '" +playlistnameValue+ "')") #테이블에 재생목록 관련 데이터 삽입
        self.cur.execute("CREATE TABLE '" + playlistnameValue + "' (videonumber TEXT PRIMARY KEY, videourl TEXT)") #재생목록 테이블 만들기
        result = self.cur.fetchall()
        print(result)
        self.conn.commit()
        self.conn.close()
        print("테이블생성 완료")

    def popupdilog(self) : 
        self.makeplaylistUi.Dialog.show()

    def check(self) :
        playlistnameValue = str(self.makeplaylistUi.PutInPlaylistName.text())
        print(playlistnameValue)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)    #pyqt사용할때 기본문법
    a = classMakeTable()
    a.popupdilog()
    # a.makeplaylistTable()
    sys.exit(app.exec_())   # x를 눌러서 프로그램을 껐을때 app이라는걸 삭제하겠다라는것(메모리에서)

