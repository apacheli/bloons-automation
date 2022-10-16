# Bloons TD 6 Automation Script

## About

> **Warning** This is a personal project intended for educational purposes only.
> I am not responsible if anything goes wrong on your end. However, feel free to
> modify the script for your own use.

A Python script I wrote to help me grind collection events in Bloons TD 6.

## Requirements

- Have all monkeys and at least their tier 4 upgrades unlocked
- Have Benjamin unlocked
- Have all monkey knowledge unlocked and enabled
- Have Dark Castle unlocked
- Screen size set to 1600 x 900 (your screen must be 16:9 ratio too)

> **Note** This script will probably not work for you if you do not meet these
> requirements.

## Running

- Install Python 3 or higher: https://www.python.org/
- Install pyautogui - `$ py -m pip install pyautogui` (This may vary depending
  on your OS, but you can just google "how to install python modules")
- Open Bloons TD 6 and stay on the home screen
- Clone the repository with git:
  `$ git clone https://github.com/apacheli/bloons-automation`
- Run the script: `$ py main.py`

For convenience, make sure your level is high so you can keep it running
overnight. I did not add checks for level up screens. (I'm level 14 prestige not
to flex or anything)

## FAQ

### Q: Why not use hotkeys?

**A:** Hotkeys used to work at some point, but Ninja Kiwi might have added some
sort of patch to disable automated key presses from pyautogui.

### Q: Will this work on my mobile device?

**A:** No.

### Q: Does this script work on Linux and macOS?

**A:** Try it and see.

### Q: Why does it not work?

**A:** This usually happens after an update. You might have to update the
assets.

### Q: Why not restart after completion?

**A:** Ninja Kiwi must have patched this quirk. Unfortunately, you are unable to
save up for diamond crates.
