from pyautogui import click, locateOnScreen, moveTo, scroll, sleep
from time import time


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
    c(1581, 297, .1)
    c(1457, 696, .1)

    # place a boomerang monkey on round 3
    wait_for_image("3")
    c(1597, 399, .1)
    c(822, 657, .1)

    # place a tack shooter on round 4
    wait_for_image("4")
    c(1590, 503, .1)
    c(632, 504, .1)

    # place a sniper and a glue gunner on round 5
    wait_for_image("5")
    c(1681, 628, .1)
    c(1373, 513, .1)
    c(1593, 631, .1)
    c(1012, 661, .1)

    # place an engineer on round 6
    wait_for_image("6")
    c(1587, 879, .1, move=True)
    s(12, -1)
    c(seconds=.1)
    c(923, 472, .1)
    c(1587, 879, .1, move=True)
    s(12, 1)

    # place an ice monkey on round 8
    wait_for_image("8")
    c(1673, 477, .1)
    c(988, 476, .1)

    # place a ninja on round 9
    wait_for_image("9")
    c(1587, 879, .1, move=True)
    s(6, -1)
    c(seconds=.1)
    c(624, 615, .1)

    # place a super monkey on round 14
    wait_for_image("14")
    c(1680, 762, .1)
    c(797, 454, .1)

    # upgrade ninja
    wait_for_image("24")
    c(624, 615, .1)
    c(path_2_right[0], path_2_right[1], .1, 3)
    c(path_3_right[0], path_3_right[1], .1)

    random_click()

    # place a bomb shooter and upgrade to moab mauler
    wait_for_image("28")
    c(1684, 234, .1, move=True)
    s(2, 1)
    c(seconds=.1)
    c(599, 459, .1, 2)
    c(path_3_right[0], path_3_right[1], .1, 3)
    c(path_1_right[0], path_1_right[1], .1, 2)

    random_click()

    # sell the super monkey on round 28 (stealing too much xp)
    c(797, 454, .1)
    c(1449, 855, .1)

    random_click()

    # upgrade engineer
    c(923, 472, .1)
    c(path_1_left[0], path_1_left[1], .1, 2)
    c(path_2_left[0], path_2_left[1], .1, 3)

    random_click()

    # upgrade some towers on round 34
    wait_for_image("34")
    c(797, 454, .1)
    c(1449, 855, .1)

    random_click()

    def a():  # boomerang money
        c(822, 657, .1)
        c(path_1_right[0], path_1_right[1], .1, 3)
        c(path_3_right[0], path_3_right[1], .1, 2)
    a()

    random_click()

    def b():  # tack shooter
        c(632, 504, .1)
        c(path_2_right[0], path_2_right[1], .1, 3)
        c(path_1_right[0], path_1_right[1], .1)
        c(1582, 300, .1)
        c(754, 657, .1, 2)
        c(path_2_right[0], path_2_right[1], .1, 3)
        c(path_1_right[0], path_1_right[1], .1)
    b()

    random_click()

    def _c():  # dart monkey
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

    # upgrade more towers on round 36
    wait_for_image("36")

    def d():  # glue gunner
        c(1012, 661, .1)
        c(path_1_left[0], path_1_left[1], .1)
        c(path_2_left[0], path_2_left[1], .1, 2)
    d()

    random_click()

    def e():  # ice monkey
        c(988, 476, .1)
        c(path_1_left[0], path_1_left[1], .1, 3)
    e()

    random_click()

    # upgrade sniper on round 38
    wait_for_image("38")
    c(1373, 513, .1)
    c(path_1_left[0], path_1_left[1], .1, 2)
    c(path_2_left[0], path_2_left[1], .1, 2)

    random_click()

    # restart the map after completion because it is faster
    wait_for_image("victory")
    c(973, 861, .5)
    c(1182, 800, .5)
    c(952, 733, .5)
    c(1495, 133, .5)
    c(1057, 812, .5)
    c(1120, 706, .5)
    c(1598, 501, .5, move=True)
    s(2, 1)

    # caution sleep in case something goes wrong
    sleep(2)


if __name__ == "__main__":
    seconds = 5

    print(f"MAKE SURE THAT YOU ARE ON DARK CASTLE BEFORE STARTING")
    print(f"Starting in {seconds} seconds")
    print(f"use ctrl+c to exit")

    sleep(seconds)

    try:
        while True:
            play_game()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
