from pytube import YouTube
import tkinter as tk
from tkinter import ttk, filedialog
import sv_ttk
#from moviepy.video.io.VideoFileClip import VideoFileClip
#import librosa
#import mido
#from mido import MidiFile, MidiTrack, Message
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

root = tk.Tk()
root.title("Youtube Downloader")

def download():
	path = os.getcwd()
	yt = YouTube(link_entry.get())
	title.configure(text=yt.title)
	if res_menu.get() == "Max":
		yd = yt.streams.get_highest_resolution()
		yd.download(path)
		
	elif res_menu.get() == "Audio Only":
		yd = yt.streams.filter(only_audio = True).first()
		yd.download(path)
	else:
		yd = yt.streams.filter(res=res_menu.get()).first()
		yd.download(path)
		

# Downloader

link = ttk.Label(root, text="Url")
link.grid(row=0, column=0)
link_entry = ttk.Entry(root)
link_entry.grid(row=0, column=1)

res_menu = ttk.Combobox(root, state="readonly", values=["Audio Only", "360p", "480p", "720p", "Max"])
res_menu.grid(row=0, column=2)

download_button = ttk.Button(root, text="Download", command=download)
download_button.grid(row=0, column=3)

title = ttk.Label(root, text="")
title.grid(row=1, column=0)


sv_ttk.set_theme("dark")

root.bind('<Shift-Tab>', sv_ttk.toggle_theme)


root.mainloop()
