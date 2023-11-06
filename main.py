import pytube
import os
from pytube import YouTube

link = input("enter your link: ")
yt = YouTube(link)
type = int(input("please enter file type, 1. video or 2. for audio: "))

def video():
    streams = yt.streams.filter(progressive=True)
    for i, stream in enumerate(streams):
        print(f"available resolution:\n{i+1}. Quality:{stream.resolution}, Format:{stream.mime_type} ")
    choice = int(input("enter number of chosen quality: "))
    selected_stream = streams[choice-1]
    selected_stream.download()
def audio():
    streams = yt.streams.filter(only_audio=True).first().download()
    base, ext = os.path.splitext(streams)
    new_file = base + '.mp3'
    os.rename(streams, new_file)
if type == 1:
    video()
    print("downloaded")
elif type == 2:
    audio()
    print("downloaded")
else: print("invalid input")
