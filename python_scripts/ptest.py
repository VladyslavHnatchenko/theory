import time


def fast():
    print("I'm fast function")


def slow():
    time.sleep(3)
    print("I'm very slow function")


def medium():
    time.sleep(0.5)
    print("I'm an average function ...")


def main():
    fast()
    slow()
    medium()


if __name__ == '__main__':
    main()
