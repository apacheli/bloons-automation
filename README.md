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

If you are a low level player, this script will probably not work for you if you
do not meet these requirements. However as the disclaimer says, feel free to
modify the script.

## Running

- Install Python 3 or higher - https://www.python.org/
- Install pyautogui `$ py -m pip install pyautogui` (This may vary depending on
  your OS. Just google "how to install python modules")
- Navigate your way to Dark Castle on easy difficulty
- Run the main script `$ py main.py`

You may have noticed that instead of leaving the game after completion, the game
will just restart. If you want to increase your diamond crate efficiency, do not
leave the game, so be patient.

For convenience, make sure you have a high level (I am 8 veteran levels at the
time of this writing) so you can keep it running overnight. I do not add checks
for level up screens.

## FAQ

### Why not use hotkeys?

Hotkeys used to work at some point, but Ninja Kiwi might have added some sort of
patch to disable automated key presses from pyautogui.

### Will this work on my mobile device?

No.

### Does this script work on Linux and macOS?

Not sure. I only tested Windows.
