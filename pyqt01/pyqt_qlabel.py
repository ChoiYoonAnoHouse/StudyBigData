import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    #생성자
    def __init__(self) -> None: #None은 리턴할 필요가 없을 때 None 만약 str을 쓴다면 str을 return 한다는 이야기. 생성자는 기본적으로 return 값이 없어서 None인 것이
        super().__init__()
        self.initUI()
        # self.setupUI()

    # 화면 정의를 위한 사용자 함수
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 100, 630, 400) # 창의 위치를 모니터 좌상단으로부터 가로 300px, 세로 100px, 창의 크기는 가로 640px, 세로 400px
        self.setWindowTitle('QLabel!!!')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./PyQt01/image/lion.png')) #윈도우 아이콘 지정
        label1 = QLabel('', self)
        label2 = QLabel('', self)
        label1.setStyleSheet(
            'border-width: 3px;'
            'border-style: solid;' # 스타일은 실선
            'border-color: blue;' # 색깔은 파란색
            'image: url(./pyqt01/image/image1.png)'
        )
        label2.setStyleSheet(
            'border-width: 3px;'
            'border-style: dot-dot-dash;' # 스타일은 실선
            'border-color: red;' # 색깔은 파란색
            'image: url(./pyqt01/image/image2.png)'
            )




        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)


        
        

        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()