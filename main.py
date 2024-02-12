from pyautogui import click, locateCenterOnScreen, sleep


def s(seconds):
    # print("taking a nap")
    return sleep(seconds)


def c(*args, **kwargs):
    return click(*args, **kwargs, interval=.5)


def rp():
    # reset position click random spot
    c(x=978, y=958)


def img(i):
    while True:
        try:
            return locateCenterOnScreen(f"images/{i}.png", confidence=.98)
        except:
            # print("image not found try again in 1 second")
            s(1)


def click_img(i):
    x, y = img(i)
    c(x=x, y=y)


instas = [834, 1092, 709, 963, 1218]


def check_if_collection_event_is_on_screen():
    try:
        x, y = locateCenterOnScreen(f"images/collect.png", confidence=.98)
        print("wow collect very cool")
        c(x=x, y=y)
        s(1)
        for p in instas:
            c(x=p, y=555, clicks=2)
        s(1)
        c(x=981, y=927)
        c(x=229, y=152)
    except:
        pass


def navigate_to_dark_castle():
    c(x=859, y=876)
    c(x=1270, y=908)
    c(x=1531, y=462)
    c(x=609, y=582)
    c(x=699, y=446)
    c(x=689, y=593)


def play_the_game():
    click_img("sauda")
    c(x=884, y=651)
    c(x=1692, y=944, clicks=2)

    click_img("dart_monkey")
    c(x=813, y=475)
    rp()

    img("round_8")
    c(x=813, y=475)
    c(x=1445, y=755, clicks=3)
    c(x=1445, y=632, clicks=2)
    rp()

    img("round_15")
    c(x=1680, y=409)
    c(x=762, y=659, clicks=2)
    c(x=1445, y=755, clicks=3)
    rp()

    img("round_17")
    c(x=762, y=659)
    c(x=1445, y=632, clicks=2)
    rp()

    img("round_23")
    c(x=813, y=475)
    c(x=1445, y=755)
    rp()

    img("round_37")
    c(x=1579, y=619)
    c(x=913, y=458, clicks=2)
    c(x=438, y=505, clicks=4)
    c(x=438, y=629)

    click_img("next")
    print("yay we won")
    c(x=761, y=805)


def main():
    print("starting in 15 seconds")
    print("click game window before the script starts")
    print("press ctrl+c to exit")
    try:
        s(12)
        while True:
            s(3)
            check_if_collection_event_is_on_screen()
            navigate_to_dark_castle()
            play_the_game()
    except KeyboardInterrupt:
        print("exiting...")


if __name__ == "__main__":
    main()
