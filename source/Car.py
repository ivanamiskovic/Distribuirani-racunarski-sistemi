import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Car(QLabel):
    
    #62 x 122
    width = 62
    height = 122
    x = 0
    y = 0
    m = 0
    t = 1
    track = 1
    
    def __init__(self, parent, cars, car_number, obstacle):
        super().__init__(parent)	
		
        self.generate_a_car(cars, car_number, obstacle)

    def play(self, interval=10):
        self._timer = QTimer(interval=interval, timeout=self._animation_step)
        self._timer.start()
		
    def _animation_step(self):
         self.y = self.y + self.t
         self.setGeometry(self.track * 80 + 10, self.y, 62, 122)
         if self.m % 1000 == 0:
            self.t += 0.2
         self.m += 1
            
    def closeEvent(self, event):
        self._timer.stop()
    
    def generate_a_car(self, cars, car_number, obstacle):
    
        no_collision = False
        while (no_collision == False):
           start_position = random.randrange(-1000, -200)
           
           type = random.randrange(1, 7)
           self.track = random.randrange(0, 8)
                  
           if type == 1:
               pixmap = QPixmap('resources/car1.png')
           elif type == 2:
               pixmap = QPixmap('resources/car2.png')
           elif type == 3:
               pixmap = QPixmap('resources/car3.png')
           elif type == 4:
               pixmap = QPixmap('resources/car4.png')
           elif type == 5:
               pixmap = QPixmap('resources/car5.png')
           elif type == 6:
               pixmap = QPixmap('resources/car6.png')
        
           self.y = start_position  
           self.x = self.track * 80 + 10           
           self.setPixmap(pixmap)
           self.setGeometry(self.x, self.y, 62, 122)
        
           if self.collision_self(cars, car_number) == False and self.collision_with_obstacle(obstacle) == False:
               no_collision = True

    def collision_self(self, cars, car_number):

        rect1 = [self.x, self.y, self.x+self.width, self.y+self.height] 
        i = 0
        for car in cars:
            
			#Other car rectangle
            rect2 = [car.x, car.y, car.x + car.width, car.y + car.height]
			
            if rect1[0] < rect2[2] and rect1[2] > rect2[0] and rect1[1] < rect2[3] and rect1[3]  > rect2[1] and i != car_number:  
                print("collision on car generation ", car)            
                return True				
            
            i = i + 1
        return False
 
    def collision_with_obstacle(self, obstacle):
        
        if self.track == obstacle.track:
           print("collision on car generation with obstacle ") 
           return True
    
        return False
        			