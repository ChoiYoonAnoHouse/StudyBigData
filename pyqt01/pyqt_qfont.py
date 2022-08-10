import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    #생성자
    def __init__(self) -> None: #None은 리턴할 필요가 없을 때 None 만약 str을 쓴다면 str을 return 한다는 이야기. 생성자는 기본적으로 return 값이 없어서 None인 것이
        super().__init__()
        self.initUI()
        # self.setupUI()

    def initUI(self) -> None:
        self.setGeometry(300, 100, 630, 400) # 창의 위치를 모니터 좌상단으로부터 가로 300px, 세로 100px, 창의 크기는 가로 640px, 세로 400px
        self.setWindowTitle('QTemplate!!!')
        self.text = '아름다운 세상이야~'
        self.show()

    def paintEvent(self, event) -> None:
        paint = QPainter()
        paint.begin(self)
        #그림을 그리는 함수를 추가
        self.drawText(event, paint) # self는 자기 스스로 즉 def의 클래스 자체를 말한다.
        paint.end()

    # 텍스트를 그리기 위한 사용자 함수
    def drawText(self, event, paint) -> None:
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('WD어느봄날에', 20))
        paint.drawText(105, 100, 'HELL WORLD~')
        paint.setPen(QColor(0,250,10))
        paint.setFont(QFont('DearHoneybatang', 10))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)
    
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()