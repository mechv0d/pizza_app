from exposed.data_get import data_get
from exposed.auth import *
from exposed.load_shift import load_shift
from exposed.create_take import create_take
from exposed.index_msg import *
from exposed.create_archive_card import create_archive_card
from exposed.create_food_card import create_food_card
from exposed.shift_admin import close_shift, open_new_shift, add_take, close_take
from app.data import debug
import eel

if __name__ == '__main__':
    eel.init("")

    eel.start("index.html", size=(900, 900), app_mode=True)
