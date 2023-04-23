import cv2
import os
from mutagen.mp3 import MP3
import numpy as np
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 15.0
width, height = 1280, 720
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# Path to the directory containing the images
path = 'C:/Users/Aouub/Desktop/YT_Downloader/images'
audio_path = 'C:/Users/Aouub/Desktop/YT_Downloader/mp3'

# Iterate over the files in the directory
for filename in sorted(os.listdir(path)):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the image
        img = cv2.imread(os.path.join(path, filename))

        # Get the image dimensions
        img_height, img_width, _ = img.shape

        # Calculate the aspect ratios
        video_aspect_ratio = width / height
        img_aspect_ratio = img_width / img_height

        # If the image is wider than the video, resize it based on the video width
        if img_aspect_ratio > video_aspect_ratio:
            new_width = width
            new_height = int(new_width / img_aspect_ratio)
        # Otherwise, resize it based on the video height
        else:
            new_height = height
            new_width = int(new_height * img_aspect_ratio)

        # Resize the image to fit within the video dimensions
        img = cv2.resize(img, (new_width, new_height))

        # Calculate the padding to center the image within the video frame
        h_padding = (width - new_width) // 2
        v_padding = (height - new_height) // 2

        # Create a black background to fill the video frame
        bg = np.zeros((height, width, 3), dtype=np.uint8)

        # Paste the resized image onto the black background with padding
        bg[v_padding:v_padding+new_height, h_padding:h_padding+new_width] = img

        # Get the duration of the corresponding audio file
        audio_filename = os.path.splitext(filename)[0] + '.mp3'
        audio_file = os.path.join(audio_path, audio_filename)
        audio_duration = MP3(audio_file).info.length

        # Write the frame to the video for the corresponding duration
        for i in range(int(audio_duration * fps)):
            out.write(bg)

# Release the video writer and close the video file
out.release()
cv2.destroyAllWindows()
