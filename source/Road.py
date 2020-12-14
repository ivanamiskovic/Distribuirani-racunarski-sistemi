import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Road(QLabel):

    x = 0
    y = -640
    t = 0.6

    def __init__(self,parent):
        super().__init__(parent)	
		
        pixmap = QPixmap('resources/road1.jpg')
		
        self.setPixmap(pixmap)
        self.setGeometry(0, 0, 640, 1280)


    def play(self, interval=10):
        self._timer = QTimer(interval=interval, timeout=self._animation_step)
        self._timer.start()
		
    def _animation_step(self):
        self.y = self.y + self.t
        self.setGeometry(0, self.y, 640, 1280)
        if self.y >= 0:
            self.y = -640
        
    def closeEvent(self, event):
        self._timer.stop()     
 
		   
 			   