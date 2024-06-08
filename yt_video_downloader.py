from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        high_res_stream = streams.get_highest_resolution()
        high_res_stream.download(output_path=save_path)
        print("Video Downloaded Successfuly!")

    except Exception as e:
        print(e)


#url = input("Enter URL : ")
# save_path = input("Enter Path to save Video : ")

# download_video(url, save_path)


def open_gui():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Enter YouTube URL : ")
    save_dir = open_gui()
    
    if save_dir:
        print("Started Download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location!.")
