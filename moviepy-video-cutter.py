from moviepy.editor import VideoFileClip
from sys import argv
from os import system
from datetime import datetime, timedelta
from re import search
import sys


def video_properties(filename):

    my_clip = VideoFileClip(filename)
    print("Duration of video : ", my_clip.duration)
    print("FPS : ", my_clip.fps)
    my_clip.close()
    return my_clip.duration

def video_cutter(filename, start, end, clipname):
    my_clip = VideoFileClip(filename)
    new_clip = my_clip.subclip(start,end)
    print('new clip duration : ',new_clip.duration)
    new_clip.write_videofile(clipname, codec = "libx264", fps=25)
    new_clip.close()



if __name__ == '__main__':

    if len(argv) == 2:
        script, filename = argv 
        video_length = video_properties(filename)
        print(f"This video has time span of {video_length} seconds")
        start = input("Enter Starting time of clip : ")
        end = input("Enter Stopping time of clip : ")
        clipname = input("Enter custom name of clip file with ectension : ")

        if int(start) < int(end):
            video_cutter(filename, start, end, clipname)
        else:
            print("Invaild duration time, please try agian")
    else:
        print("Invaild command, read help() and try again\n")
