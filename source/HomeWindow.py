from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class HomeWindow(QWidget):
 
    def __init__(self):
        super().__init__()
        
        pixel_ratio = QWindow().devicePixelRatio()

        #Postavila sam pozadinsku sliku sa QLabel-om.
        home_background_pixmap = QPixmap('resources/menu.png')

        home_background_pixmap.setDevicePixelRatio(pixel_ratio)
        self.main_background = QLabel(self)
        self.main_background.setPixmap(home_background_pixmap)
        self.main_background.setGeometry(0, 0, 640, 480)

 
        #Kreirala sam Quick game button.
        self.main_play_button = ImageButton('menu1', self)
        self.main_play_button.setGeometry(389, 126, 251, 72)
        
        #Kreirala sam Multiplayer button.
        self.main_multi_button = ImageButton('menu3', self)
        self.main_multi_button.setGeometry(389, 198, 251, 72)
    
        #Kreirala sam Score button.
        self.main_score_button = ImageButton('menu4', self)
        self.main_score_button.setGeometry(389, 270, 251, 72)
		
        #Kreirala sam Quit button.
        self.main_quit_button = ImageButton('menu2', self)
        self.main_quit_button.setGeometry(389, 342, 251, 72)
        
        self.show()
