from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from source.ImageButton import *

class Player(QLabel):
 
    x = 10
    y = 350 
    player_number = 0
    player_life = 3
    immunity = 0
    immobilized = False
    score = 0
 
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
	  
      
        if self.immobilized == False and self.player_life > 0:
           if self.x + x > 568: return 	
           if self.x + x < 10: return 
           if self.y + y < 1: return	
           if self.y + y > 358: return			 
           self.x = self.x + x
           self.y = self.y + y
           self.setGeometry(self.x , self.y, 62, 122)
 
    def _collide(self, cars):
	
        if self._immune_after_death() == True or self.player_life < 1:
            return False
          
	    #Player rectangle
        rect1 = [self.x, self.y, self.x+62, self.y+122] 

        for car in cars:

			#Car rectangle
            rect2 = [car.x, car.y, car.x+58, car.y+118]

			
            if rect1[0] < rect2[2] and rect1[2] > rect2[0] and rect1[1] < rect2[3] and rect1[3]  > rect2[1]:
                self.player_life -= 1	
                print("Player ", self.player_number, "| lives ", self.player_life)
                self._reposition_after_death()				
                return True				
        
        return False
        
    def _collide_obstacle(self, obstacle):
	
        if self._immune_after_death() == True or self.player_life < 1:
            return False
          
	    #Player rectangle
        rect1 = [self.x, self.y, self.x+62, self.y+122] 

        #Obstacle rectangle
        rect2 = [obstacle.x, obstacle.y, obstacle.x+68, obstacle.y+24]	

			
        if rect1[0] < rect2[2] and rect1[2] > rect2[0] and rect1[1] < rect2[3] and rect1[3]  > rect2[1]:
            self.player_life -= 1	
            print("Player ", self.player_number, "| lives ", self.player_life)
            self._reposition_after_death()				
            return True				

        return False
        
    def _collide_mud(self, mud):
	
        if self._immune_after_death() == True or self.player_life < 1:
            return False
          
	    #Player rectangle
        rect1 = [self.x, self.y, self.x+62, self.y+122] 

        #Mud rectangle
        rect2 = [mud.x, mud.y, mud.x+50, mud.y+50]	

			
        if rect1[0] < rect2[2] and rect1[2] > rect2[0] and rect1[1] < rect2[3] and rect1[3]  > rect2[1]:
            self._immobilize_player()
            print("Player ", self.player_number, "is in the mud")			
            return True				
        else:
            self.immobilized = False
        return False

    def _reposition_after_death(self):
        if self.player_number == 1:
            self.x = 170
        else:
            self.x = 410
        self.y = 350
        self.immunity = 500
        self.immobilized = False
        self.setGeometry( self.x , self.y, 62, 122)
        
    def _immobilize_player(self):
        
        self.immobilized = True
 
    def _immune_after_death(self):
    
           
        if self.immunity > 0:
            opacityEffect = QGraphicsOpacityEffect()
            opacityEffect.setOpacity(0.5)
            self.setGraphicsEffect(opacityEffect)
            self.immunity = self.immunity - 1
            return True
        else:
            opacityEffect = QGraphicsOpacityEffect()
            opacityEffect.setOpacity(1)
            self.setGraphicsEffect(opacityEffect)
            return False

    def _collide_player(self, other_player):
	
        if self._immune_after_death() == True or other_player.player_life < 1 or self.player_life < 1:
            return False
          
	    #Player rectangle
        rect1 = [self.x, self.y, self.x+58, self.y+118] 
        
        #Other player rectangle
        rect2 = [other_player.x, other_player.y, other_player.x+58, other_player.y+118]
            
			
        if rect1[0] < rect2[2] and rect1[2] > rect2[0] and rect1[1] < rect2[3] and rect1[3]  > rect2[1]:
            self.player_life -= 1	
            other_player.player_life -= 1        
            self._reposition_after_death()	
            other_player._reposition_after_death()  
            print("Both players died")
            print("Player ", self.player_number, "| lives ", self.player_life)
            print("Player ", other_player.player_number, "| lives ", other_player.player_life)			
            return True				

        return False
 
 
    def _update_score(self):
        self.score += 1
			