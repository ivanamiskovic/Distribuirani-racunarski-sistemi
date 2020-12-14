from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from source.Player import *
from source.Road import *

class GameWindow(QWidget):
 
    road = None
    player1 = None
    player2 = None
    number_of_players = 0

    def __init__(self):
        super().__init__()
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        
        self.show()
        
    def new_game(self, player_num):
           
        self.number_of_players = player_num

        self.road_add()
        
        self.player_add()
        
    #Adding the road
    def road_add(self):
        self.road = Road(self)
        self.road.play()
        
    #Adding player cars to the game
    def player_add(self):

        if self.number_of_players == 1:
            self.player1 = Player(self,1)
        else:
            self.player1 = Player(self,1)
            self.player2 = Player(self,2)	  