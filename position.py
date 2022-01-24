from pyautogui import position, sleep

seconds = 5

print(f"Displaying position in {seconds} seconds")

sleep(seconds)

print(position())
