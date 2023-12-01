"""
A GUI for the transliterator based on PySimpleGUI.
"""

from trans import transliterate
import PySimpleGUI as sg
import logging
logging.basicConfig(level=logging.DEBUG)

sg.SetOptions (
    font = ("Helvetica", 12, "bold"),
    element_padding = (8, 8),
)

WIN_WIDTH = 950
WIN_HEIGHT = 800

def launch_gui():
    layout = [[sg.Text('Place text to transliterate here')],
              [sg.Multiline(size=(80,15), key="-BG TEXT-", autoscroll=True)],
              [sg.Multiline(size=(80,15), key="-ENG TEXT-", autoscroll=True)],
              [sg.Button("Transliterate"), sg.Button("Exit")]]

    window = sg.Window("Transliterator", layout, size=(WIN_WIDTH, WIN_HEIGHT), keep_on_top=True, finalize=True)

    while True: 
        event, values = window.read()
        logging.debug(f"|EVENT| {event:20}|VALUES| {values}")

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Transliterate":
            cyrillic_text = values["-BG TEXT-"]
            transliterated_text = transliterate(cyrillic_text)
            window['-ENG TEXT-'].update(transliterated_text)

    window.close()

if __name__ == '__main__':
    launch_gui()
