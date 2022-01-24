points = 797, 454

from pyautogui import position, sleep, moveTo

seconds = 3

print(f"Moving your position to {points} in {seconds} seconds")

sleep(seconds)

print(moveTo(points[0], points[1]))
