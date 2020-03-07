from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_time = 22
end_time = 22+10
ffmpeg_extract_subclip("1.mp4", start_time, end_time, targetname="cut.mp4")