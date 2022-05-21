# Bloons TD 6 Automation Script

## About

> Disclaimer: This is a personal project intended for educational purposes only.
> I am not responsible if anything goes wrong on your end. However, feel free to
> modify the script for your own use.

A Python script I wrote to help me grind collection events in Bloons TD 6.

## Requirements

- Have all monkeys and at least their tier 4 upgrades unlocked
- Have Benjamin unlocked
- Have all monkey knowledge unlocked and enabled
- Have Dark Castle unlocked
- Screen size set to 1600 x 900

This script will probably not work for you if you do not meet these
requirements. However, feel free to modify the script for your own use as the
disclaimer says.

## Running

- Install Python 3 or higher - https://www.python.org/
- Install pyautogui - `$ py -m pip install pyautogui` (This may vary depending
  on your OS, but you can just google "how to install python modules")
- Open Bloons TD 6 and then go to Dark Castle on easy difficulty
- Copy `main.py`
- Run the script - `$ py main.py`

You may have noticed that instead of leaving the game after completion, the game
will just restart. If you want to increase your diamond crate efficiency, do not
close or leave the game.

For convenience, make sure your level is high so you can keep it running
overnight. I did not add checks for level up screens.

## FAQ

### Why not use hotkeys?

Hotkeys used to work at some point, but Ninja Kiwi might have added some sort of
patch to disable automated key presses from pyautogui.

### Will this work on my mobile device?

No.

### Does this script work on Linux and macOS?

Try it and see.
