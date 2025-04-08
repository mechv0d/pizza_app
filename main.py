from exposed.data_get import data_get
from exposed.proceed_auth import proceed_auth
from exposed.load_shift import load_shift
from exposed.create_take import create_take
import eel

debug = True

if __name__ == '__main__':
    eel.init("")

    eel.start("index.html", size=(900, 900), app_mode=not debug)
