import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 클래스 OOP
class qTemplate(QWidget):
    #생성자
    def __init__(self) -> None: #None은 리턴할 필요가 없을 때 None 만약 str을 쓴다면 str을 return 한다는 이야기. 생성자는 기본적으로 return 값이 없어서 None인 것이
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300, 100, 630, 400) # 창의 위치를 모니터 좌상단으로부터 가로 300px, 세로 100px, 창의 크기는 가로 640px, 세로 400px
        self.setWindowTitle('QTemplate!!!')
        self.show()

    
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()