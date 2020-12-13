import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from source.StartWindow import *

def main():

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling) #set scaling attribute
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps) #set high dpi icon
    app = QApplication(sys.argv) #create new application

    startwindow = StartWindow() #create new instance of main window
    startwindow.show() #make instance visible
    startwindow.raise_() #raise instance to top of window stack
    sys.exit(app.exec_()) #monitor application for events

if __name__ == '__main__':
    main()
