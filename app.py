import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

def download():
    try:
        ytLink = videoLink.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        invalidLabel.configure(text="Invalid link.")
        
    completeLabel.configure(text="Download complete!")
#App frame
mainwindow = ctk.CTk()
mainwindow.geometry("900x600")
mainwindow.title("Youtube video downloader")


#Title of the page
label = ctk.CTkLabel(mainwindow, text="Insert the video link",text_color='white', font=('Aptos', 18))
label.pack(padx=20, pady=20)

#Get the video url
url_var = tk.StringVar()
videoLink = ctk.CTkEntry(mainwindow, width=350, height=40, textvariable=url_var)
videoLink.pack()

#Download completed
completeLabel = ctk.CTkLabel(mainwindow, text="")
completeLabel.pack()

#Invalid link
invalidLabel = ctk.CTkLabel(mainwindow, text="")
invalidLabel.pack()

#Download button
downloadButton = ctk.CTkButton(mainwindow, text="Download video!",command=download, font=('Aptos', 18))
downloadButton.pack(padx=20, pady=5)

mainwindow.mainloop()
