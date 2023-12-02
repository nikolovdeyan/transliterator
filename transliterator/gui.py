"""
A GUI for the transliterator based on PySimpleGUI.
"""
import os
import PySimpleGUI as sg

from transliterator.trans import transliterate

import logging
logging.basicConfig(level=logging.DEBUG)

sg.SetOptions (
    font = ("Helvetica", 11),
    element_padding = (8, 8),
)

WIN_WIDTH = 950
WIN_HEIGHT = 750

def make_window():
    sg.theme(sg.user_settings_get_entry("theme", None))
    layout = [
        [sg.Menu([["File", ["Theme", "Exit"]], ["Help", "About"],])],
        [sg.Push(), sg.Text("Transliterator", size=(16,1), font=("Helvetica", 16, "bold")), sg.Push()],
        [sg.Text("Place your cyrillic text here and press <Transliterate>")],
        [sg.Multiline(size=(70,12), key="-BG TEXT-", autoscroll=True)],
        [sg.Multiline(size=(70,12), key="-EN TEXT-", autoscroll=True)],
        [sg.Button("Transliterate", s=9), sg.Button("Copy", s=9), sg.Button("Clear", s=9), sg.Button("Exit", s=9)],
    ]
    return sg.Window("Transliterator", layout, keep_on_top=True, finalize=True)

def main():
    sg.user_settings_filename(filename="settings.json")
    window = make_window()

    while True: 
        event, values = window.read()
        logging.debug(f"|EVENT| {event:20}|VALUES| {values}")

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Transliterate":
            cyrillic_text = values["-BG TEXT-"]
            transliterated_text = transliterate(cyrillic_text)
            window["-EN TEXT-"].update(transliterated_text)
        if event == "Copy":
            sg.clipboard_set(values["-EN TEXT-"])
        if event == "Clear":
            window["-EN TEXT-"].update("")
            window["-BG TEXT-"].update("")
        if event == "Theme":
            ev, vals = sg.Window("Choose Theme", [[sg.Combo(sg.theme_list(), k="-THEME LIST-"), sg.OK(), sg.Cancel()]]).read(close=True)
            if ev == "OK":
                window.close()
                sg.user_settings_set_entry("theme", vals["-THEME LIST-"])
                window = make_window()
        if event == "About":
            sg.popup("Transliterator", "Version: 1.0", "Copyright (c) Deyan Nikolov")
            # ev, vals = sg.Window("About", [[sg.Text("About")],[sg.OK()]]).read(close=True)
            # if ev == "OK":
            #     window.close()
            #     window = make_window()

    window.close()