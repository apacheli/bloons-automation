from pyautogui import click, locateOnScreen, moveTo, scroll, sleep
from time import time

def c(x: int = None, y: int = None, seconds: int = None, clicks=1, move=False):
  if move:
    moveTo(x, y)
  else:
    click(x, y, clicks, seconds)
  sleep(seconds)


# remove the upgrade handle so it can reset
def random_click():
  c(1004, 156, .1)


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
  if not locateOnScreen(f"./assets/collect.png"):
    return False
  c(974, 670, 1)
  for l in insta_locations:
    c(l[0], l[1], .5, 2)
  c(969, 930, .5, 2)
  return True


path_1_left = [440, 510]
path_1_right = [1451, 505]

path_2_left = [440, 640]
path_2_right = [1456, 641]

path_3_left = [440, 770]
path_3_right = [1464, 754]


games_completed = 0
games_time_total = 0

def main(x: bool):
  if x:
    c(1676, 899, .25)
  else:
    wait_for_image("play")
    c(858, 874, .25)

  # navigate to dark castle
  c(1277, 907, .25)
  c(1532, 462, .25)
  c(967, 321, .25)
  c(688, 449, .25)
  c(694, 582, .25)

  # wait for the map to load, place a dart monkey, and then start the round
  wait_for_image("dark_castle_map")
  c(1683, 296, .1)
  c(898, 650, .1)
  c(1691, 945, .1, 2)

  # place down benjamin on round 2
  wait_for_image("2")
  c(1581, 297, .1)
  c(1457, 696, .1)

  # place down boomerang monkey on round 3
  wait_for_image("3")
  c(1597, 399, .1)
  c(822, 657, .1)

  # place down tack shooter on round 4
  wait_for_image("4")
  c(1590, 503, .1)
  c(632, 504, .1)

  # place down sniper and glue gunner on round 5
  wait_for_image("5")
  c(1681, 628, .1)
  c(1373, 513, .1)
  c(1593, 631, .1)
  c(1012, 661, .1)

  # place down engineer on round 6
  wait_for_image("6")
  c(1587, 879, .1, move=True)
  s(12, -1)
  c(seconds=.1)
  c(923, 472, .1)
  c(1587, 879, .1, move=True)
  s(12, 1)

  # place down ice monkey on round 8
  wait_for_image("8")
  c(1673, 477, .1)
  c(988, 476, .1)

  # place down ninja on round 9
  wait_for_image("9")
  c(1587, 879, .1, move=True)
  s(6, -1)
  c(seconds=.1)
  c(624, 615, .1)

  # place down super monkey on round 14
  wait_for_image("14")
  c(1680, 762, .1)
  c(797, 454, .1)

  # upgrade ninja
  wait_for_image("24")
  c(624, 615, .1)
  c(path_2_right[0], path_2_right[1], .1, 3)
  c(path_3_right[0], path_3_right[1], .1)

  random_click()

  # buy bomb shooter and upgrade to moab mauler
  wait_for_image("28")
  c(1684, 234, .1, move=True)
  s(2, 1)
  c(seconds=.1)
  c(599, 459, .1, 2)
  c(path_3_right[0], path_3_right[1], .1, 3)
  c(path_1_right[0], path_1_right[1], .1, 2)

  random_click()

  # sell super monkey on round 28
  c(797, 454, .1)
  c(1449, 855, .1)

  random_click()

  # upgrade engineer
  c(923, 472, .1)
  c(path_1_left[0], path_1_left[1], .1, 2)
  c(path_2_left[0], path_2_left[1], .1, 3)

  random_click()
  
  # upgrade some towers
  wait_for_image("34")
  c(797, 454, .1)
  c(1449, 855, .1)

  random_click()

  def a(): # boomerang money
    c(822, 657, .1)
    c(path_1_right[0], path_1_right[1], .1, 3)
    c(path_3_right[0], path_3_right[1], .1, 2)
  a()

  random_click()

  def b(): # tack shooter
    c(632, 504, .1)
    c(path_2_right[0], path_2_right[1], .1, 3)
    c(path_1_right[0], path_1_right[1], .1)
    c(1582, 300, .1)
    c(754, 657, .1, 2)
    c(path_2_right[0], path_2_right[1], .1, 3)
    c(path_1_right[0], path_1_right[1], .1)
  b()

  random_click()

  def _c(): # dart monkey
    c(898, 650, .1)
    c(path_2_left[0], path_2_left[1], .1, 3)
    c(path_3_left[0], path_3_left[1], .1, 2)
    c(1684, 234, .1, move=True)
    s(2, 1)
    c(seconds=.1)
    c(569, 713, .1, 2)
    c(path_2_right[0], path_2_right[1], .1, 3)
    c(path_3_right[0], path_3_right[1], .1, 2)
  _c()

  random_click()

  # upgrade more towers
  wait_for_image("36")
  def d(): # glue gunner
    c(1012, 661, .1)
    c(path_1_left[0], path_1_left[1], .1)
    c(path_2_left[0], path_2_left[1], .1, 2)
  d()

  random_click()

  def e(): # ice monkey
    c(988, 476, .1)
    c(path_1_left[0], path_1_left[1], .1, 3)
  e()

  random_click()

  # upgrade sniper
  wait_for_image("38")
  c(1373, 513, .1)
  c(path_1_left[0], path_1_left[1], .1, 2)
  c(path_2_left[0], path_2_left[1], .1, 2)

  random_click()

  # upgrade engineer
  # c(923, 472, .1)
  # c(path_1_left[0], path_1_left[1], .1, 2)
  # c(path_2_left[0], path_2_left[1], .1, 3)

  random_click()

  wait_for_image("victory")
  c(973, 861, .25)
  c(743, 813, .25)
  sleep(4)


if __name__ == "__main__":
  print(f"starting whenever the Bloons TD 6 menu is on screen")
  print(f"use ctrl+c to exit")
  try:
    while True:
      main(collection_event())
  except KeyboardInterrupt:
    print("exiting")
    exit()
