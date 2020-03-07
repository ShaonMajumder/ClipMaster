from moviepy.editor import *

clip = (VideoFileClip("output.mp4")
        .subclip((0,36),(0,42))
        .resize(0.8))
clip.write_gif("sample.gif")