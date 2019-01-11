# pySoundBoard
A simple Pygame sound board for adding sound effects while recording podcasts. The goal is to create something similar to [Farrago](https://rogueamoeba.com/farrago/) with the look and feel of a DJ control board.

## Current Status
![](screenshots/screenshot.png)

## Usage
* `Click` toggle Play/Stop
* `P` toggle Pause/Unpause all sounds
* `S` Stop all sounds
* `F` Fadeout all sounds (3 seconds)
* `ESC` Exit
* `Alt`+`Click` To drag window (in Linux)

Place your sounds in the sound folder. Edit the file named `paths.txt` to point to sound files. The soundboard will read this file and load sounds accordingly. Buttons with sounds loaded will light in green. Buttons with no sounds loaded will remain in grey. When you hover a button an orange outline will appear. Finally when a sound is playing the button's color will stay in yellow color.

Some sample sounds have been included.

Enjoy!