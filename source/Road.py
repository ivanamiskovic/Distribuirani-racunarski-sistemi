import sys
import time
import multiprocessing
from time import sleep
from multiprocessing import Pool, Process, current_process, Lock, Queue
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def worker(qIn,qOut):
    while True :
        y = qIn.get()
		
        y = y + 0.6
        if y >= 0:
            y = -640		
		
        qOut.put(y)	

class Road(QLabel):

    x = 0
    y = -640
    queueIn = None
    queueOut = None
    p1 = None

    def __init__(self,parent):
        super().__init__(parent)	
		
        pixmap = QPixmap('resources/road1.jpg')
		
        self.setPixmap(pixmap)
        self.setGeometry(0, 0, 640, 1280)
        
        self.queueIn = Queue()
        self.queueOut = Queue()		
        self.p1 = Process(target=worker, args=[self.queueIn,self.queueOut])
        self.p1.start()


    def play(self, interval=10):
        self._timer = QTimer(interval=interval, timeout=self._animation_step)
        self._timer.start()
		
    def _animation_step(self):
        self.queueIn.put(self.y)
        self.y = self.queueOut.get()
        self.setGeometry(0, self.y, 640, 1280)

        
    def closeEvent(self, event):
        if self.p1.is_alive():
           self.p1.terminate()
        self._timer.stop()     
 
		   
 			   