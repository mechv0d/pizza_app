from datetime import datetime as dt

import eel

from app.data import main_data as data
from app.db import ConnectDb


@eel.expose
def load_shift():
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query(f"select * from shift_view")
        data.s_takes = result
        for take in data.s_takes:
            take['start_time'] = take['start_time'].strftime("%H:%M, %d.%m") if take['start_time'] else ''
            take['end_time'] = take['end_time'].strftime("%H:%M, %d.%m") if take['end_time'] else ''
        db.close_connection()
        return

    print("Load Shift failed")  # Optional: Print for debugging
    eel.go_to('/index.html')