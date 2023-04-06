from pyautogui import click, locateOnScreen, moveTo, scroll, sleep
from time import time


insta_locations = [
  # Double instas
  [834, 549],
  [1092, 556],

  # Triple instas
  [709, 558],
  [963, 551],
  [1218, 555],
]


def c(x: int = None, y: int = None, seconds: int = None, clicks=1, move=False):
    if move:
        moveTo(x, y)
    else:
        click(x, y, clicks, seconds)

    sleep(seconds)


# clicks a random spot to make the upgrade menu go away
def random_click():
    c(1004, 156, .1)


# down = -1, up = +1
def s(times: int, direction: int):
    for _ in range(times):
        scroll(direction)


def wait_for_image(image: str):
    while not locateOnScreen(f"./assets/{image}.png"):
        pass


def collection_event():
    sleep(3)
    if not locateOnScreen("./assets/collect.png"):
        return
    c(974, 670, 1)
    for l in insta_locations:
        c(l[0], l[1], .4, clicks=2)
    c(231, 155, .4)


def go_to_dark_castle():
    c(866, 876, .25) # play
    c(1277, 907, .25) # expert
    c(1532, 462, .25) # expert arrow right
    c(1380, 332, .25) # dark castle
    c(688, 449, .25) # easy
    c(694, 582, .25) # standard


path_1_left = [440, 510]
path_1_right = [1451, 505]

path_2_left = [440, 640]
path_2_right = [1456, 641]

path_3_left = [440, 770]
path_3_right = [1464, 754]


def play_game():
    # place a dart monkey and start the game
    c(1683, 296, .1)
    c(898, 650, .1)
    c(1691, 945, .2, 2)

    # place benjamin on round 2
    wait_for_image("2")
    c(1581, 297, .15)
    c(1457, 696, .15)

    # buy monkey ace
    wait_for_image("4")
    c(1576, 852, .15)
    c(985, 716, .15)

    # buy heli pilot
    wait_for_image("8")
    c(1687, 802, .15)
    c(768, 401, .15)
    c(876, 562, .15, move=True)

    # upgrade heli pilot to 2xx
    wait_for_image("14")
    c(768, 401, .15)
    c(path_1_right[0], path_1_right[1], .1, 2)
    random_click()

    # upgrade heli pilot and monkey ace
    # heli
    wait_for_image("24")
    c(768, 401, .15)
    c(path_1_right[0], path_1_right[1], .1, 1)
    c(path_2_right[0], path_2_right[1], .1, 2)
    random_click()
    # ace
    c(985, 716, .15)
    c(path_1_left[0], path_1_left[1], .1, 2)
    c(path_2_left[0], path_2_left[1], .1, 3)
    random_click()

    # buy another ace
    wait_for_image("34")
    c(1576, 852, .15)
    c(949, 447, .2, clicks=2)
    c(path_1_left[0], path_1_left[1], .1, clicks=4)
    c(path_2_left[0], path_2_left[1], .1, clicks=2)
    random_click()

    wait_for_image("next")
    c(973, 861, .5)
    c(747, 805, .5)

    # caution sleep in case something goes wrong
    sleep(1.5)


if __name__ == "__main__":
    seconds = 3

    print(f"MAKE SURE THAT YOU ARE ON DARK CASTLE BEFORE STARTING")
    print(f"Starting in {seconds} seconds")
    print(f"use ctrl+c to exit")

    sleep(seconds)

    try:
        while True:
            collection_event()
            go_to_dark_castle()
            wait_for_image("castle")
            play_game()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
