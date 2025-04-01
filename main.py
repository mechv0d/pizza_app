from exposed.exp_add_count import *

debug = True

if __name__ == '__main__':
    eel.init("")

    eel.start("index.html", size=(900, 900), app_mode=not debug)
