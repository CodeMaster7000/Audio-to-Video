import imageio
import os
from moviepy import editor
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path

audio_path = os.path.join(os.getcwd(), "audio.mp3")
video_path = os.path.join(os.getcwd(), "videos")
images_path = os.path.join(os.getcwd(), "images")
audio = MP3(audio_path)
audio_length = audio.info.length
list_of_images = []
for image_file in os.listdir(images_path):
    if image_file.endswith('.png') or image_file.endswith('.jpg'):
        image_path = os.path.join(images_path, image_file)
        image = Image.open(image_path).resize((400, 400), Image.ANTIALIAS)
        list_of_images.append(image)
duration = audio_length/len(list_of_images)
imageio.mimsave('images.gif', list_of_images, fps=1/duration)
video = editor.VideoFileClip("images.gif")
audio = editor.AudioFileClip(audio_path)
final_video = video.set_audio(audio)
os.chdir(video_path)
final_video.write_videofile(fps=60, codec="libx264", filename="video.mp4")
