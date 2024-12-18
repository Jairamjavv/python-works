import PySimpleGUI as psg
from typing import List, Tuple, Dict, Any

# Define the layout with more specific type annotations
layout: List[List[psg.Element]] = [
    [
        psg.Text("Enter the youtube URL to download"),
        psg.Text("Choose:"),
        psg.Radio("Video", group_id="vyd_options", default=True, key="-VIDEO-"),
        psg.Radio("Audio", group_id="vyd_options", key="-AUDIO-"),
    ]
]

# Create the window for the layout
window: psg.Window = psg.Window("VYD Downloader", layout=layout)

# Create event loop to process "events" and get the "values" of the inputs
while True:
    event: str
    values: Dict[str, Any]
    event, values = window.read()

    # If user closes window or clicks cancel
    if event == psg.WIN_CLOSED or event == "Cancel":
        break

    print("Application opened")

window.close()
