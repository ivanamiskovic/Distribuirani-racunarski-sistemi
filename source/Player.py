from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from source.ImageButton import *

class Player(QLabel):
 
    x = 10
    y = 350 

 
    def __init__(self, parent, p_n):
        super().__init__(parent)
		
        self.player_number = p_n
        
        if self.player_number == 1:
            pixmap = QPixmap('resources/player1.png')
            self.x = 170
        else:
            pixmap = QPixmap('resources/player2.png')
            self.x = 410

        self.setPixmap(pixmap)
        self.setGeometry( self.x , self.y, 62, 122)
		

    def play(self, interval=10):
        self._timer = QTimer(interval=interval, timeout=self._animation_step)
        self._timer.start()
		
    def _animation_step(self):
        self.y = self.y + 1
        self.setGeometry( 80 + 10, self.y, 62, 122)
        print(self.track)

    def _move(self,x,y):
	  
        if self.x + x > 568: return 	
        if self.x + x < 10: return 
        if self.y + y < 1: return	
        if self.y + y > 358: return			 
        self.x = self.x + x
        self.y = self.y + y
        self.setGeometry(self.x , self.y, 62, 122)
 

			