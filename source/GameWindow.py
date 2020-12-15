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
        
        self.obstacle_add()
        
        self.mud_add()

        self.cars_add()
        
        self.player_add()
        
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