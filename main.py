import PyQt5
import random
from PyQt5 import uic
from PIL import Image, ImageDraw
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import os


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.do_paint = False

    def draw(self):
        b = 240
        new_image = Image.new("RGB", (200, 200), (b, b, b))
        drawer = ImageDraw.Draw(new_image)
        a = random.randrange(10, 100)
        drawer.ellipse(((a, a), (200 - a, 200 - a)), 'yellow')
        new_image.save('ball.png')

        self.pixmap = QPixmap('ball.png')
        self.image = QLabel(self)
        self.image.move(100, 10)
        self.image.resize(200, 200)
        self.image.setPixmap(self.pixmap)
        self.image.show()

        os.remove('ball.png')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())