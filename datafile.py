import sqlite3
import Ui_ChangePlaylistName

class dataClass : 
    def __init__(self) :
        #데이터 호출용 생성자
        self.conn = sqlite3.connect('data.db')
        self.cur = self.conn.cursor()

        #Ui 전용 생성자
        self.ChangeBox = Ui_ChangePlaylistName.Ui_ChangePlaylistName()

    def ChangePlaylistName(self) : #재생목록 이름 바꾸는 함수

        self.cur.execute("UPDATE user6 SET lose='" + str(updatenum) + "' WHERE id='" + self.idmemory + "' ")
        result = self.cur.fetchall()

        if (len(result) != 0) :
            self.playlistname = result
            self.videocount = 0
            print(result)
            

    