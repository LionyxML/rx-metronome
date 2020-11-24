#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import simpleaudio as sa
from threading import Thread
import time

is_playing = False
tick_sound = sa.WaveObject.from_wave_file("./audio/tick.wav")

class PlayUntilStop: 
    def __init__(self): 
        self._running = True
      
    def terminate(self): 
        self._running = False
      
    def run(self):
        time_to_sleep = 60.0/time_selector.get()
        while self._running: 
            tick_sound.play()
            time.sleep(time_to_sleep)

def quit():
    root.destroy()

def sobre():
    mb.showinfo("rx-metronome", '''

    rx-metronome

    A really simple and beautifully tk metronome.

    Version: 0.1

    Author : Rahul M. Juliato
             rahuljuliato.com

''')

def update_selection(value):
    selected_value.set(str("%3d" % time_selector.get()) + " bpm")
    pass

def play():
    global is_playing
    if is_playing == False:
        global player
        player = PlayUntilStop()
        thread_play = Thread(target=player.run)
        thread_play.start()
        is_playing = True

def stop():
    global is_playing
    if is_playing == True:
        player.terminate()
        is_playing = False


root = tk.Tk()
root.wm_title('rx-metronome v0.1')
root.wm_minsize(400, 220)
root.grid_anchor(anchor='c')

barramenu = tk.Menu(root)
file_menu = tk.Menu(barramenu, tearoff=800)
file_menu.add_command(label="About", command=sobre)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)
barramenu.add_cascade(label="File", menu=file_menu)

root.config(menu=barramenu)

time_selector = tk.Scale(root, orient="horizontal", from_=40, to=218,
                    showvalue=0, command=update_selection, length=250)
time_selector.grid(row=2, column=1, columnspan=2, pady=10)
time_selector.set(80)

selected_value = tk.StringVar(root)
selected_value.set("80 bpm")

time_label = tk.Label(root, textvariable=selected_value)
time_label.grid(row=1, column=1, columnspan=2, pady=10)
time_label.config(font=("", 40))

play_button = tk.Button(root, text="▶", command=play)
play_button.grid(row=3, column=2, sticky='WE', pady=10)

stop_button = tk.Button(root, text="◼", command=stop)
stop_button.grid(row=3, column=1, sticky='WE')

root.mainloop()



