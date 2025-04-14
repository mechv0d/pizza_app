from datetime import datetime as dt

import eel

from app.data import main_data as data
from app.db import ConnectDb


@eel.expose
def load_shift():
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query(f"select * from shift_view")
        data.s_takes = result
        for take in data.s_takes:
            take['emp_id'] = "-".join(take['emp_id'][i:i + 3] for i in range(0, 9, 3))
            take['start_time'] = take['start_time'].strftime("%H:%M, %d.%m") if take['start_time'] else ''
            take['end_time'] = take['end_time'].strftime("%H:%M, %d.%m") if take['end_time'] else ''

        result = db.execute_query(data.s_sql)
        if len(result) > 0:
            result = result[0]
            data.s_id = result['shift_pk']
            data.s_start_time_raw = result['start_time']
            data.s_end_time_raw = result['end_time']
            data.s_closed = result['closed']
            data.s_passwd = result['password']

        db.close_connection()
        return

    print("Load Shift failed")  # Optional: Print for debugging
    eel.go_to('/index.html')
