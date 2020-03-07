import moviepy.editor as mpe
my_clip = mpe.VideoFileClip('cut.mp4')
audio_background = mpe.AudioFileClip('Song_of_Mirrors.mp3')
final_audio = mpe.CompositeAudioClip([ audio_background])
final_clip = my_clip.set_audio(final_audio)
final_clip.write_videofile("output.mp4")