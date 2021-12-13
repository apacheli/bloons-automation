from pyautogui import click, locateOnScreen, moveTo, scroll, sleep
from time import time

def c(x: int = None, y: int = None, seconds: int = None, clicks=1, move=False):
  if move:
    moveTo(x, y)
  else:
    click(x, y, clicks, seconds)
  sleep(seconds)


def s(times: int, direction: int):
  for _ in range(times):
    scroll(direction)


def wait_for_image(image: str):
  while not locateOnScreen(f"./assets/{image}.png"):
    pass


insta_locations = [
  # Double instas
  [834, 549],
  [1092, 556],

  # Triple instas
  [709, 558],
  [963, 551],
  [1218, 555],
]

def collection_event():
  if not locateOnScreen(f"./assets/9.png"):
    return False
  c(974, 670, .94)
  for l in insta_locations:
    c(l[0], l[1], .44, 2)
  c(969, 930, .44)
  return True


path_1 = [440, 510]
path_2 = [440, 640]
path_3 = [440, 770]


games_completed = 0
games_time_total = 0

def main(x: bool):
  if x:
    c(1676, 899, .24)
  else:
    wait_for_image("0")
    c(858, 874, .24)

  c(1277, 907, .24)
  c(1532, 462, .24)
  c(967, 321, .24)
  c(688, 449, .24)
  c(694, 582, .24)

  wait_for_image("1")
  game_time_start = time()
  c(1683, 296, .1)
  c(898, 650, .1)
  c(1691, 945, .1, 2)

  wait_for_image("2")
  c(1581, 297, .1)
  c(1457, 696, .1)

  wait_for_image("3")
  c(1578, 877, .1, move=True)
  s(8, -1)
  c(seconds=.1)
  c(907, 469, .1, 2)
  c(path_1[0], path_1[1], .1)

  wait_for_image("4")
  c(seconds=.1)

  wait_for_image("5")
  c(path_2[0], path_2[1], .1, 3)
  c(1685, 556, .1)
  c(1374, 549, .1, 2)
  c(458, 413, .1)
  c(path_1[0], path_1[1], .1, 2)
  c(path_2[0], path_2[1], .1, 2)

  wait_for_image("6")
  c(1600, 544, .1)
  c(906, 860, .1, 2)
  c(path_2[0], path_2[1], .1, 2)
  c(path_3[0], path_3[1], .1, 3)
  c(906, 860, .5)
  c(317, 212, .24)
  c(540, 257, .24)

  wait_for_image("7")
  c(1374, 549, .1)
  c(path_1[0], path_1[1], .1)

  wait_for_image("8")
  game_time_end = time() - game_time_start
  global games_completed
  games_completed += 1
  global games_time_total
  games_time_total += game_time_end
  average = games_time_total / games_completed / 60
  print(f"Completed {games_completed} games | Average: {average} minutes")

  c(973, 861, .24)
  c(743, 813, .24)
  sleep(3.8)


if __name__ == "__main__":
  print(f"starting whenever the Bloons TD 6 menu is on screen")
  print(f"use ctrl+c to exit")
  try:
    while True:
      main(collection_event())
  except KeyboardInterrupt:
    print("Exiting!")
    exit()
