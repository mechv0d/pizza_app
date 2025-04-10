from datetime import datetime as dt

import eel
from app.data import main_data as data
from app.db import ConnectDb


@eel.expose
def send_msg(text: str):
    if not data.is_auth:
        print(f"Sending message failed. Reason: Bad Auth")
        return

    if text.replace(' ', '') == '':
        print(f"Sending message failed. Reason: Bad Text")
        return

    db = ConnectDb()
    if not db.mydb:
        print(f"Sending message failed. Reason: Bad Connection")
        return

    result = db.execute_query("SELECT shift_pk FROM shift WHERE closed = 0 ORDER BY start_time DESC LIMIT 1")
    if len(result) > 0:
        shift_pk = result[0]['shift_pk']
    else:
        print(f"Sending message failed. Reason: Bad Shift")
        db.close_connection()
        return

    now = dt.now().strftime('%Y-%m-%d %H:%M:%S')

    result_insert = db.execute_query(f'''
        INSERT INTO shift_message (time, text, visible, emp_id, shift_pk) 
        VALUES ("{now}", "{text}", {1}, {data.a_id}, {shift_pk})
        ''')

    print(f"Sending message successful. ID: {result_insert}")  # Optional: Print for debugging
    # eel.reload() HTML form already do this
    db.close_connection()
    return
