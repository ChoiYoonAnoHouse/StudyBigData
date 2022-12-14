import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: 
        super().__init__()
        self.initUi()
    
    def initUi(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 640, 400) 
        self.setWindowTitle('Q Push Button!! 예제')
        self.show()

    def addControls(self) -> None:
        self.label = QLabel('메세지 :', self)
        self.label.setGeometry(10, 10, 600, 40)
        self.btn1 = QPushButton('클릭', self)
        self.btn1.setGeometry(510,350,120,40)
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결

    # event = signal(파이썬 용어)
    def btn1_clicked(self):
        # QMessageBox.information(self,'signal','self.btn1_clicked!') # 첫번째 내용은 창 제목, 두번째 내용은 창 내용. 일반적인 정보 창
        # QMessageBox.warning(self,'signal','self.btn1_clicked!') # 경고 표시 아이콘으로 나옴. 경고창
        self.label.setText('메세지 : btn1 버튼 클릭!!!!')
        QMessageBox.critical(self,'signal','self.btn1_clicked!') # X 표시 아이콘 나옴. 에러창

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
    
    
    
    

