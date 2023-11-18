import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_Form


class RandomCircles(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_random_circle)
        self.circle_coordinates = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for x, y, radius in self.circle_coordinates:
            painter.drawEllipse(x, y, radius, radius)

    def draw_random_circle(self):
        self.circle_coordinates = []
        radius = random.randint(20, 100)
        x = random.randint(10, 452)
        y = random.randint(10, 294)
        self.circle_coordinates.append((x, y, radius))
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomCircles()
    window.show()
    sys.exit(app.exec_())
