import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 200, 700, 700)
        self.setWindowTitle('Программа')
        self.pushButton = QPushButton(self)
        self.pushButton.move(300, 50)
        self.pushButton.setText("Кнопка")
        self.pushButton.resize(100, 50)
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
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        size = random.randint(30, 300)
        qp.drawEllipse(100, 200, size, size)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        size = random.randint(30, 300)
        qp.drawEllipse(300, 500, size, size)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        size = random.randint(30, 300)
        qp.drawEllipse(400, 400, size, size)
        qp.setBrush(QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        size = random.randint(30, 300)
        qp.drawEllipse(150, 300, size, size)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())