from pyautogui import position, sleep

seconds = 5

print(f"Displaying the position of your cursor in {seconds} seconds")

sleep(seconds)

print(position())
