import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from moviepy.editor import VideoFileClip
from sys import argv
from os import system
from datetime import datetime, timedelta
from re import search
import sys

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Personal Video Cutter : Shashank Shekhar Sahoo'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.filename = " "
        self.start = 0
        self.stop = 0
        self.clipname = " "

    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        filename = self.getTextVideo()
        start = self.getIntegerStart()
        stop = self.getIntegerStop()
        clipname = self.getTextClip()
        self.start = start
        self.stop = stop
        self.clipname = clipname
        self.filename = filename
        self.show()
        video_length = self.video_properties()
        print(f"This video has time span of {video_length} seconds")
        
        self.video_cutter()


        
        
    def getIntegerStart(self):
        i, okPressed = QInputDialog.getInt(self, "Clip Start Time","Enter Start Time:", 28, 0, 100, 1)
        if okPressed:
            print(i)
        return i

    def getIntegerStop(self):
        i, okPressed = QInputDialog.getInt(self, "Clip Stop Time","Enter Stop Time:", 50, 0, 100, 1)
        if okPressed:
            print(i)
        return i
            
        
    def getTextVideo(self):
        text, okPressed = QInputDialog.getText(self, "Desried Target Filename","Enter target filename with extension:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
        return text
    
    def getTextClip(self):
        text, okPressed = QInputDialog.getText(self, "Desried Clipped Filename","Enter clipped filename with extension:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
        return text
    
    def video_properties(self):
        #filename = self.filename
        my_clip = VideoFileClip(self.filename)
        print("Duration of video : ", my_clip.duration)
        print("FPS : ", my_clip.fps)
        my_clip.close()
        return my_clip.duration


    def video_cutter(self):
        my_clip = VideoFileClip(self.filename)
        new_clip = my_clip.subclip(self.start,self.stop)
        print('new clip duration : ',new_clip.duration)
        new_clip.write_videofile(self.clipname, codec = "libx264", fps=25)
        new_clip.close()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

        
