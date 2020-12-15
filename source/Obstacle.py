import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Obstacle(QLabel):
    
    #74 x 30
    width = 74
    height = 30
    x = 0
    y = 0
    m = 0
    t = 0.6
    track = 1
    
    def __init__(self, parent):
        super().__init__(parent)	
		
        self.generate_an_obstacle()
        
    def play(self, interval=10):
        self._timer = QTimer(interval=interval, timeout=self._animation_step)
        self._timer.start()
		
    def _animation_step(self):
        self.y = self.y + self.t
        self.setGeometry(self.track * 80 + 10, self.y, 74, 30)
        
    def closeEvent(self, event):
        self._timer.stop()
            
    def generate_an_obstacle(self):
    
        start_position = random.randrange(-1000, -200)

        self.track = random.randrange(0, 8)
              
        pixmap = QPixmap('resources/roadblock.png')
        
        self.y = start_position  
        self.x = self.track * 80 + 10           
        self.setPixmap(pixmap)
        self.setGeometry(self.x, self.y, 74, 30)
        	