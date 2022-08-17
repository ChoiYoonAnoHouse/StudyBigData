import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: 
        super().__init__()
        uic.loadUi('./pyqt02/basic01.ui', self)
        self.initUi()
    
    def initUi(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked) # 시그널 연결
        
    def btn1_clicked(self):
        self.label.setText('메세지 : btn1 버튼 클릭!!!!')
        QMessageBox.critical(self,'signal','self.btn1_clicked!') # X 표시 아이콘 나옴. 에러창


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()
    
    
    
    

