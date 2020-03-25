from __future__ import unicode_literals
from ClipMaster.ClipMaster import ClipMaster
import os
import youtube_dl


cm = ClipMaster()

#conversion
cm.clip('captured.webm').to_mp4('videoCon.mp4')
#cut
cm.clip('videoCon.mp4').cut_to("cutAa.mp4","3","30")
os.remove('videoCon.mp4')
#print(cm.clip('cutAa.mp4').video_info('video_size'))
#>Video size [1366, 768]
#>0 24
cm.clip('cutAa.mp4').crop('crop_vd.mp4',(0,24),(1366,768))
os.remove('cutAa.mp4')
video_size = cm.clip('crop_vd.mp4').video_info("video_duration")
#print("Video size",video_size)


def YoutubeDownload(link,filename):
	ydl_opts = {}
	ydl_opts["outtmpl"]= filename

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([link])

YoutubeDownload('https://www.youtube.com/watch?v=J0BPoofmPkw','sound.mp4')

cm.clip('sound.mp4').to_mp3('audio.mp3','0',str(int(video_size)))
os.remove('sound.mp4')
cm.clip('crop_vd.mp4').audio('audio.mp3').bind_to('output.mp4')
os.remove('crop_vd.mp4')
os.remove('audio.mp3')

cm.clip('output.mp4').add_logo('robist.png','watermarked.mp4')
os.remove('output.mp4')