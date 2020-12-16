from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from source.Player import *
from source.Road import *
from source.Car import *
from source.Obstacle import *
from source.Mud import *

class GameWindow(QWidget):
 
    road = None
    player1 = None
    player2 = None
    number_of_players = 0
    cars = []
    obstacle = None
    mud = None
    end = False
    better_player = 0
    worse_player = 0

    def __init__(self):
        super().__init__()
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        
        self.font = QFont()
        self.font.setFamily(QFontDatabase.applicationFontFamilies(0)[0])
        self.font.setStyleStrategy(QFont.PreferQuality)
        self.font.setHintingPreference(QFont.PreferFullHinting)
        self.font.setPixelSize(50)
        self.font.setWeight(QFont.Normal)
        
        self.fontEnd = QFont()
        self.fontEnd.setFamily(QFontDatabase.applicationFontFamilies(0)[0])
        self.fontEnd.setStyleStrategy(QFont.PreferQuality)
        self.fontEnd.setHintingPreference(QFont.PreferFullHinting)
        self.fontEnd.setPixelSize(100)
        self.fontEnd.setWeight(QFont.Normal)
        
        self.show()
        
    def new_game(self, player_num):
           
        self.number_of_players = player_num

        self.road_add()
        
        self.obstacle_add()
        
        self.mud_add()

        self.cars_add()
        
        self.player_add()
        
        self.player_score_life_startup()
        
    #################################
    #MAIN GAME THREAD
    def game_start(self): 
        
        #Generating new cars after they go too far down
        for x in range(len(self.cars)):
           if self.cars[x].y > 550:
              self.cars[x].generate_a_car(self.cars, x, self.obstacle)
              print("generated a new car")
        
        #Generating a new obstacle after it goes to far down
        if self.obstacle.y > 550:
           self.obstacle.generate_an_obstacle()
           print("generated a new obstacle")
           
        #Generating a new mud pond after it goes to far down
        if self.mud.y > 550:
           self.mud.generate_a_mud_pond()
           print("generated a new mud pond")   
        
        #Collision checking between player and other cars
        self.player1._collide(self.cars)
        if self.number_of_players == 2:
            self.player2._collide(self.cars)
        #Collision checking between player and the obstacle
        self.player1._collide_obstacle(self.obstacle) 
        if self.number_of_players == 2:
            self.player2._collide_obstacle(self.obstacle)
        #Collision checking between player and the mud pond
        self.player1._collide_mud(self.mud) 
        if self.number_of_players == 2:
            self.player2._collide_mud(self.mud)
        #Collision checking between players
        if self.number_of_players == 2:
            self.player1._collide_player(self.player2)   
            
        #Check if players are dead
        if self.player1.player_life < 1:
            self.player1.close()
        else:
            self.player1._update_score()
        if self.number_of_players == 2:
            if self.player2.player_life < 1:
                self.player2.close()
            else:
                self.player2._update_score()
        
        
        for x in range(self.number_of_players):
            if x == 0:
                self.player_score_label.setText("{0}".format(self.player1.score))
                self.player_life_label.setText("{0}♥".format(self.player1.player_life))
            elif x == 1:
                self.player_score_label2.setText("{0}".format(self.player2.score))
                self.player_life_label2.setText("{0}♥".format(self.player2.player_life))
        
        #Check if game is over        
        if self.number_of_players == 2:
            if self.player1.player_life < 1 and self.player2.player_life < 1:
                self.end_game()
        else:
            if self.player1.player_life < 1:
                self.end_game()        
    #################################
        
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
    
    #Adding starting enemy cars to the game
    def cars_add(self):
        
        print("Starting adding cars")
        i = 0
        while i < 6:
		              
            car = Car(self, self.cars, i, self.obstacle)
            car.play()
            self.cars.append(car)
            print("car added ", car)
            print("starting position y = ", car.y)
            print("starting track = ", car.track)
            print("---------------------------")
            i = i + 1	
    
    #Adding an obstacle    
    def obstacle_add(self): 
        self.obstacle = Obstacle(self)
        print("obstacle added", self.obstacle)
        self.obstacle.play()
        
    #Adding a mud pond    
    def mud_add(self): 
        self.mud = Mud(self)
        print("mud added", self.mud)
        self.mud.play()    
        
    #Connecting player scores to the labels
    def player_score_life_startup(self):
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(2)
        shadow.setOffset(2)
        
        shadow2 = QGraphicsDropShadowEffect(self)
        shadow2.setBlurRadius(2)
        shadow2.setOffset(2)
        
        shadow3 = QGraphicsDropShadowEffect(self)
        shadow3.setBlurRadius(2)
        shadow3.setOffset(2)
        
        shadow4 = QGraphicsDropShadowEffect(self)
        shadow4.setBlurRadius(2)
        shadow4.setOffset(2)
        
        self.player_score_label = QLabel(self)
        self.player_score_label.setFixedWidth(640)	
        self.player_score_label.move(-200, 20)
        self.player_score_label.setAlignment(Qt.AlignCenter)
        self.player_score_label.setText("0")		
        self.player_score_label.setFont(self.font)
        self.player_score_label.setStyleSheet('color: purple')
        self.player_score_label.setGraphicsEffect(shadow)
        #self.player_score_label.hide()
        
        self.player_life_label = QLabel(self)
        self.player_life_label.setFixedWidth(640)	
        self.player_life_label.move(-50, 20)
        self.player_life_label.setAlignment(Qt.AlignCenter)
        self.player_life_label.setText("0")		
        self.player_life_label.setFont(self.font)
        self.player_life_label.setStyleSheet('color: purple')
        self.player_life_label.setGraphicsEffect(shadow3)
        
        if self.number_of_players == 2:
           self.player_score_label2 = QLabel(self)
           self.player_score_label2.setFixedWidth(640)
           self.player_score_label2.move(200, 20)
           self.player_score_label2.setAlignment(Qt.AlignCenter)
           self.player_score_label2.setText("0")
           self.player_score_label2.setFont(self.font)
           self.player_score_label2.setStyleSheet('color: limegreen')
           self.player_score_label2.setGraphicsEffect(shadow2)
           #self.player_score_label2.hide()
           
           self.player_life_label2 = QLabel(self)
           self.player_life_label2.setFixedWidth(640)	
           self.player_life_label2.move(50, 20)
           self.player_life_label2.setAlignment(Qt.AlignCenter)
           self.player_life_label2.setText("0")		
           self.player_life_label2.setFont(self.font)
           self.player_life_label2.setStyleSheet('color: limegreen')
           self.player_life_label2.setGraphicsEffect(shadow4)
        
        

    #Game over - score showing 
    def end_game(self):
        
        if self.number_of_players == 2:
            if self.player1.score > self.player2.score:
                self.better_player = self.player1.score
                self.worse_player = self.player2.score
            else:
                self.better_player = self.player2.score 
                self.worse_player = self.player1.score                
        else:
            self.better_player = self.player1.score
            
        self.end = True
        
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(2)
        shadow.setOffset(2)
        self.end_label = QLabel(self)
        self.end_label.setFixedWidth(640)	
        self.end_label.move(0, 175)
        self.end_label.setAlignment(Qt.AlignCenter)
        self.end_label.setText("GAME OVER\n(PRESS ESC)")		
        self.end_label.setFont(self.font)
        self.end_label.setStyleSheet('color: yellow')
        self.end_label.setGraphicsEffect(shadow)
        self.end_label.show()
        
    def closeEvent(self, event):

        n = len(self.cars)	
        while  n != 0:
            self.cars[0].close()		
            del self.cars[0]
            n = len(self.cars)
        
        if self.obstacle != None: 
            self.obstacle.close()        
            del self.obstacle
        if self.mud != None:
            self.mud.close()
            del self.mud
        if self.road != None:
            self.road.close()
            del self.road
       
        if self.number_of_players == 1 and self.player1 != None:           
            del self.player1
        else:
            if self.player1 != None and self.player2 != None:
                del self.player1
                del self.player2
                
                self.road = None
        
        print("closeGameWindow")
        self.player1 = None
        self.player2 = None
        self.cars = []
        self.obstacle = None
        self.mud = None
        self.number_of_players = 0
        self.end = False
        