from ClipMaster.ClipMaster import ClipMaster
import subprocess
import os
#ffmpeg.exe -i captured.webm video.mp4


cm = ClipMaster()
cm.clip('captured.webm').to_mp4('videoCon.mp4')
cm.clip('videoCon.mp4').cut_to("cutAa.mp4","3","30")


#convertion
#clip = VideoFileClip('captured.webm')
#clip.write_videofile('Cropvideo.mp4')
#cm.clip('convertedA.mp4')

#cm.clip('captured.webm').convert_to_mp4('convertedmp4.mp4')
#cm.clip('convertedA.mp4').crop_vd('Croped.mp4')
"""
cm.clip('1.mp4').cut_to("cut.mp4",5,354)
cm.clip('cut.mp4').gif_to('sample.gif',35,41)
cm.clip('cut.mp4').audio('Song_of_Mirrors.mp3').bind_to('output.mp4')
#./ffmpeg.exe -i captured.webm video.mp4
"""