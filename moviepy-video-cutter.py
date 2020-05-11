from moviepy.editor import VideoFileClip

my_clip = VideoFileClip("WizKhalifa.mp4")
print("Duration of video : ", my_clip.duration)
print("FPS : ", my_clip.fps)

new_clip = my_clip.subclip(20,100)
print('new clip duration : ',new_clip.duration)
new_clip.write_videofile("new_clip.mp4", codec = "libx264", fps=25)
new_clip.close()