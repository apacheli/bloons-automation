# Bloons TD 6 Automation Script

> **Note** Confirmed to be working as of 2023-04-10 version 36.1.

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
- Screen size set to 1600x900 (16:9 ratio)

> **Note** This script will probably not work for you if you do not meet these
> requirements.

## Running

- Install Python 3 or higher: https://www.python.org/
- Install pyautogui - `$ py -m pip install pyautogui` This may vary depending on
  your OS, but you can just google "how to install python modules"
- Upgrade pillow because pyautogui needs it
  `$ py -m pip install pillow --upgrade` Again, this may vary depending on your
  OS
- Open Bloons TD 6 and stay on the home screen
- Clone the repository with git:
  `$ git clone https://github.com/apacheli/bloons-automation`
- Go to the cloned directory: `$ cd bloons-automation`
- Run the script: `$ py main.py`

For convenience, make sure your level is high so you can keep it running
overnight. I did not add checks for level up screens.

## FAQ

### Q: Why not use hotkeys?

**A:** Ninja Kiwi probably patched this.

### Q: Will this work on my mobile device?

**A:** Try it and see.

### Q: Does this script work on Linux and macOS?

**A:** Try it and see.

### Q: Why does it not work?

**A:** This usually happens after an update. You might have to update the
assets.

### Q: Why not restart after completing?

**A:** Ninja Kiwi probably patched this.
