# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
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

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Next Departure')
        self.root.configure(bg='#181A1D')
        self.root.geometry(f'480x320')
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        myFont = font.Font(family='Small Fonts', size=15)
        self.label.configure(text=getTime(), fg='#ffffff', bg='#181A1D', font=myFont)
        self.root.after(1000, self.update_clock)

app=App()

