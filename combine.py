from moviepy.editor import *

# Set the directory containing the mp3 files
mp3_dir = "C:/Users/Aouub/Desktop/YT_Downloader/mp3/"

# Create a list of all mp3 files in the directory
mp3_files = [f for f in os.listdir(mp3_dir) if f.endswith('.mp3')]

# Sort the mp3 files by name (optional)
mp3_files.sort()

# Create a list of AudioFileClip objects from the mp3 files
clips = [AudioFileClip(mp3_dir + f) for f in mp3_files]

# Concatenate the audio clips into a single AudioFileClip
concatenated_audio = concatenate_audioclips(clips)

# Create a new video clip with a black background and the concatenated audio
video = VideoFileClip("output.mp4").set_audio(concatenated_audio)

# Save the new video clip with the combined audio
video.write_videofile("combined.mp4")
