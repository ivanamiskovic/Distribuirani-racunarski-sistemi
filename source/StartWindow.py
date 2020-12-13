import sys       
import multiprocessing
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

from source.HomeWindow import *
from source.GameWindow import *
from source.ScoreWindow import *

class StartWindow(QMainWindow):
    APP_TITLE = "Cars Racing"
    
    def __init__(self, *args, **kwargs):

        super(StartWindow, self).__init__(*args, **kwargs)
        self.setupUi()

    def setupUi(self):
	
        QFontDatabase.addApplicationFont('resources/Glass_TTY_VT220.ttf')
        
        self.setWindowTitle(self.APP_TITLE)
        self.setFixedSize(640, 480)

        #Kreiramo StackLayout
        self.stacked_layout = QStackedLayout()       

        #Kreiramo HomeWindow
        self.home_window = HomeWindow()
        #HomeWindow dodajemo na StackLayout
        self.stacked_layout.addWidget(self.home_window)
		
        #Kreiramo GameWindow
        self.game_window = GameWindow()
        #GameWindow dodajemo na StackLayout
        self.stacked_layout.addWidget(self.game_window)
        
        #Kreiramo ScoreWindow
        self.score_window = ScoreWindow()
        #ScoreWindow dodajemo na StackLayout
        self.stacked_layout.addWidget(self.score_window)

        #set the central widget to display the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        #Konekcije za button-e u Meni-ju
        self.home_window.main_play_button.clicked.connect(self.start)
        self.home_window.main_multi_button.clicked.connect(self.multiplayer)
        self.home_window.main_score_button.clicked.connect(self.score)
        self.home_window.main_quit_button.clicked.connect(self.quit)

        self.keys_pressed = set()	
		
        self.status = 'home'
		
        self.timer = QBasicTimer()
        self.timer.start(16, self)		

    def timerEvent(self, event):
	
        if self.status == 'game_window': 	
        
            if Qt.Key_Escape in self.keys_pressed:
                print('ESC')			
                self.keys_pressed.remove(Qt.Key_Escape)	
                self.game_window.close()
                self.status = 'home'
                self.stacked_layout.setCurrentWidget(self.home_window)
					
        
    def start(self):
       
        print('start')
        self.status = 'game_window'
        self.stacked_layout.setCurrentWidget(self.game_window)
        
    def multiplayer(self):
        
        print('multiplayer')
        self.status = 'game_window'
        self.stacked_layout.setCurrentWidget(self.game_window)
        
    def score(self):

        print('score')
        self.status = 'score_window'
        self.stacked_layout.setCurrentWidget(self.score_window)

    def quit(self):

        print('quit')
        self.close()
		
    def keyReleaseEvent(self, event):
        
        if 	event.key() in self.keys_pressed:	
           self.keys_pressed.remove(event.key())		
		
    def keyPressEvent(self, event):
        
        self.keys_pressed.add(event.key())

    def closeEvent(self, event):

        print('close')









 
			
			
