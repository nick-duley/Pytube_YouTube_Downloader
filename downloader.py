import tkinter as tk
from pytube import YouTube
import sys

#Download YouTube video
def downloadVid():
	global input_URL
	string = input_URL.get()
	yt = YouTube(str(string))
	
	stream = yt.streams.fmt_streams

	num = 0
	for s in stream:
		print(str(num) + ": " + str(s))
		num += 1

	i = int(input("Enter the number of the video: "))
	video = stream[i]
	video.download()
	sys.exit()

#Graphical interface
root = tk.Tk()

root.geometry("500x100") 

w = tk.Label(root, text="Youtube Downloader")
w.pack()

input_URL = tk.Entry(root, bd=5, width=3008)
input_URL.pack(side=tk.TOP)

button = tk.Button(root,text="Download",fg="red",command=downloadVid)
button.pack(side=tk.BOTTOM)

root.mainloop()
