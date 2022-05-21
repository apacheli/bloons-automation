from pyautogui import position, sleep, moveTo

points = 797, 454

seconds = 5

print(f"Moving the position of your cursor to {points} in {seconds} seconds")

sleep(seconds)

moveTo(points[0], points[1])
