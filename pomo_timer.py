"""
Description:
Using PySimpleGUI to make a Pomodoro Timer


Build Instructions:
To run:
python pom_timer.py

To create installer (MAC ONLY):
py2applet --make-setup pom_timer.py
python setup.py py2app

TODO:
base on internal time to prevent drift and other timing issues
resolve issue of timer ending and skipping 1 second while playing sound

"""

import PySimpleGUI as sg
import os
import sys

# import time as t

sg.theme("DarkBrown4")
pomodoro = 25
sec = int(pomodoro * 60)
minn, secc = divmod(sec, 60)
time_format = "{:02d}:{:02d}".format(minn, secc)
start_btn = "Start"


layout = [
    [sg.Text(text="Pomodoro Timer", font="Arial 15", justification="center")],
    [
        sg.Text(
            text=time_format,
            size=(8, 1),
            font="Arial 45",
            key="-OUT-",
            justification="center",
        )
    ],
    [
        sg.Button(
            button_text="Start",
            font="Arial 20",
            disabled=False,
            key="btn1",
            size=(8, 1),
        ),
        sg.Button(
            button_text="Reset",
            font="Arial 20",
            disabled=True,
            key="btn2",
            size=(8, 1)
        ),
    ],
]

window = sg.Window("Pomodoro Timer", layout)

running = False
while True:
    event, values = window.read(timeout=1000)
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    if event == "btn1":
        if running:
            running = False
            window["btn1"].update("Start")
        else:
            running = True
            window["btn1"].update("Pause")
        window["btn2"].update(disabled=False)
        if time_format == "00:00":
            running = False
    if running is True:
        minn, secc = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(minn, secc)
        window["-OUT-"].update(time_format)
        window["btn2"].update(disabled=False)
        sec -= 1
    if event == "btn2":
        running = False
        sec = int(pomodoro * 60)
        minn, secc = divmod(sec, 60)
        time_format = "{:02d}:{:02d}".format(minn, secc)
        window["-OUT-"].update(time_format)
        window["btn1"].update("Start")
        window["btn2"].update(disabled=True)
    if time_format == "00:01":
        if sys.platform.startswith("darwin"):
            os.system('say "got it done"')
        elif sys.platform.startswith("linux"):
            os.system('spd-say "got it done"')
        time_format = "00:00"
        window["-OUT-"].update(time_format)
        running = False

window.close()
