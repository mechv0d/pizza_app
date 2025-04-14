import eel
from app.data import main_data as data
from app.db import ConnectDb

from datetime import datetime as dt


def timenow_sql():
    return dt.now().strftime('"%Y-%m-%d %H:%M:%S"')


@eel.expose
def open_new_shift():
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        try:
            result = db.execute_query(f'''
                    INSERT INTO shift (start_time) 
                    VALUES ({timenow_sql()})
                    ''')
        except:
            return
        finally:
            add_take(data.a_id, 'Админ')


@eel.expose
def close_shift(other):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query(f'''
                UPDATE shift
                SET closed = 1, end_time = {timenow_sql()}
                WHERE shift_pk = {other} and closed = 0;
                ''')
        result = db.execute_query(f'''
                                UPDATE shift_employer_take
                                SET closed = 1, end_time = {timenow_sql()}
                                WHERE shift_pk = {other} and closed = 0;
                                ''')


@eel.expose
def add_take(uid, place):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        shift_res = db.execute_query(data.s_sql)
        shift_res = [s for s in shift_res if s['closed'] == 0]
        if len(shift_res) == 0:
            return

        shift_res = shift_res[0]
        result = db.execute_query(f"""
        INSERT INTO shift_employer_take (shift_pk, emp_id, start_time, place) 
        VALUES ({shift_res['shift_pk']}, {uid}, {timenow_sql()}, "{place}")
        """)


@eel.expose
def close_take(other):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query(f'''
                UPDATE shift_employer_take
                SET closed = 1, end_time = {timenow_sql()}
                WHERE take_pk = {other} and closed = 0;
                ''')
