from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ImageButton(QAbstractButton):

    menu_button = 0
    menu_focused = None

    def __init__(self, button_id, parent):
        super().__init__(parent)

        pixel_ratio = QWindow().devicePixelRatio()

        self.pixmap_defaults = QPixmap('resources/{0}_button_defaults.png'.format(button_id))
        self.pixmap_defaults.setDevicePixelRatio(pixel_ratio)
		
        self.pixmap_press = QPixmap('resources/{0}_button_press.png'.format(button_id))
        self.pixmap_press.setDevicePixelRatio(pixel_ratio)
	
		
    def paintEvent(self, event):

        if self.menu_focused == None:
           pixmap = self.pixmap_defaults
		   
        if self.isDown(): self.menu_focused = self.pixmap_press	
        else : self.menu_focused = self.pixmap_defaults
      		
		   
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.menu_focused)

 

 
		