from pyautogui import position, sleep

seconds = 6

print(f"Displaying position in {seconds} seconds")

sleep(seconds)

print(position())
