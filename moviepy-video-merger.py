'''
from moviepy.editor import VideoFileClip, concatenate_videoclips
#from moviepy.video import VideoClip

video_1 = VideoFileClip("sahu.mp4")
video_2 = VideoFileClip("sahu2.mp4")
#video_3 = VideoFileClip("cut3.mp4")
#video_4 = VideoFileClip("cut4.mp4")

final_video= concatenate_videoclips([video_1, video_2])
final_video.write_videofile("final_video.mp4")

'''

from moviepy.editor import VideoFileClip, concatenate_videoclips
from sys import argv
from os import system
from datetime import datetime, timedelta
from re import search
import sys
import argparse



def video_merger(rawclipfiles_list, merged_filename):

    processed_clips = [VideoFileClip(i) for i in rawclipfiles_list]

    final_video= concatenate_videoclips(processed_clips)
    final_video.write_videofile(merged_filename)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-a', '--arg', nargs='+', type=str)
    parser.add_argument('-m', '--merge', default='foobar.mp4')
    args = vars(parser.parse_args())
    video_merger(args["arg"], args["merge"])
    


    