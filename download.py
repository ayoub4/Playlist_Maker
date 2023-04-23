import os
from pytube import YouTube
from moviepy.editor import *

# Set the directory where you want to save the mp3 files
save_path = 'C:/Users/Aouub/Desktop/YT_Downloader/mp3'

# Loop to get YouTube video links from the user
links = []
while True:
    link = input("Enter a YouTube video link or type 'done' to start downloading: ")
    if link == 'done':
        break
    else:
        links.append(link)

# Download the videos and convert them to mp3
for link in links:
    try:
        # Create a YouTube object and download the video
        yt = YouTube(link)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path=save_path)

        # Get the filename of the downloaded video
        video_filename = stream.default_filename

        # Convert the video to mp3 using moviepy
        mp4_file = os.path.join(save_path, video_filename)
        mp3_file = os.path.join(save_path, video_filename.split('.')[0] + '.mp3')
        video = AudioFileClip(mp4_file)
        video.write_audiofile(mp3_file)

        # Delete the original mp4 file
        os.remove(mp4_file)

        print(f"The video at {link} has been downloaded and converted to mp3 at {mp3_file}.")
    except Exception as e:
        print(f"An error occurred while downloading {link}: {str(e)}")
