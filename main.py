import sys
import random
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor("yellow"))
        size = random.randint(1, 300)
        qp.drawEllipse(100, 200, size, size)
        size = random.randint(1, 300)
        qp.drawEllipse(300, 500, size, size)
        size = random.randint(1, 300)
        qp.drawEllipse(400, 400, size, size)
        size = random.randint(1, 300)
        qp.drawEllipse(150, 300, size, size)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())