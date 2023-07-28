import moviepy.editor
from pathlib import Path

#Path to your video file
video_file = Path('nameofyourvideofile.mp4')

#Variable for video file
video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio

#Writes new audio
audio.write_audiofile(f'{video_file.stem}.mp3')
