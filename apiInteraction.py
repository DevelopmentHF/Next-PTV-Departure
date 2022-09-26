# Gets train information from Hampton to Flinders
# Henry Fielding 2022

#! /usr/bin/python3

from ctypes import windll
import requests
import time
from datetime import datetime
from signature import *
from PIL import Image, ImageDraw, ImageFont
from cgitb import text
import tkinter as tk
from tkinter import ANCHOR, PhotoImage, ttk
from tkinter.messagebox import showinfo
import time
import tkinter.font as font


def getTime():

    # Opens departure data
    depart_data = requests.get(getURL('/v3/departures/route_type/0/stop/1086?direction_id=1&max_results=1')).json()
    time_data = depart_data['departures'][0]['scheduled_departure_utc']

    # Gets individual time elements from `time_data`
    date = time_data[:10]
    UTC_ToD = time_data[11:-1]
    AEST_ToD = str((int(UTC_ToD[:2]) + 10)) + ':' + UTC_ToD[3:]
    calc_AEST_ToD = datetime.strptime(AEST_ToD, "%H:%M:%S")

    # Gets curent AEST time
    now = datetime.now()
    curr_time = now.strftime("%H:%M:%S")
    calc_curr_time = datetime.strptime(curr_time, "%H:%M:%S")

    # Calculates time until the next train arrives at station
    time_interval = calc_AEST_ToD - calc_curr_time

    # Prints information
    print(time_data)
    print(f'Time till departure = {time_interval}')
    return f'Time till departure = {time_interval}'



while (True):
    # Makes text not blurry
    windll.shcore.SetProcessDpiAwareness(1)

    # Opens a 'main' / 'root' window
    root = tk.Tk()
    root.configure(bg='#181A1D')

    # Font
    myFont = font.Font(family='Small Fonts', size=15)

    # Enter name
    name_label = tk.Label(root, text=f'{getTime()}', fg='#ffffff', bg='#181A1D', font=myFont)
    name_label.place(relx=0.5, rely=0.1, anchor='center')

    # Creates a title for the window
    root.title('Next Departure')

    window_width = 480
    window_height = 320

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Changes icon of window > requires .ico file
    # root.iconbitmap('./icon.ico')

    root.after(5000,lambda:root.destroy())
    # Keeps the window open until closed manually
    root.mainloop()





