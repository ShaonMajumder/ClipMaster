from ClipMaster.ClipMaster import ClipMaster
import subprocess
import os

cm = ClipMaster()
cm.clip('1.mp4').cut_to("cut.mp4",5,354)
cm.clip('cut.mp4').gif_to('sample.gif',35,41)
cm.clip('cut.mp4').audio('Song_of_Mirrors.mp3').bind_to('output.mp4')

