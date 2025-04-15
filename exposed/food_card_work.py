import eel
from app.data import main_data as data, timenow_sql
from app.db import ConnectDb
from app.hash import md5_hash
from random import uniform
from app.dialog import error_dialog


def taker_check() -> bool:
    if not data.is_auth:
        return False
    db = ConnectDb()
    shift_res = db.execute_query(data.s_sql)
    shift_res = [s for s in shift_res if s['closed'] == 0]
    if len(shift_res) == 0:
        error_dialog('Ошибка', 'Не найдено открытых смен!')
        return False

    shift_res = shift_res[0]
    target_take = db.execute_query(f"""
            select take_pk from shift_employer_take where emp_id = {data.a_id} and shift_pk = {shift_res['shift_pk']}
            and closed = 0;
            """)

    if len(target_take) == 0:
        error_dialog('Ошибка', 'Вы не найдены в смене! Может, администратору стоит добавить вас?')
        return False

    return True


@eel.expose
def fc_take(fc_id):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        is_taker = taker_check()
        if not is_taker:
            return

        result = db.execute_query(f"""
        UPDATE food_position
                SET emp_id = {data.a_id}, taken_time = {timenow_sql()}, ready_state = 1
                WHERE fp_pk = "{fc_id}" and ready_state = 0;
        """)


@eel.expose
def fc_ready(fc_id):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        is_taker = taker_check()
        if not is_taker:
            return

        emp_check = f'and emp_id = {data.a_id}' if data.a_status == 0 else ''
        result = db.execute_query(f"""
               UPDATE food_position
                    SET ready_time={timenow_sql()}, ready_state = 2
                    WHERE fp_pk = "{fc_id}" and ready_state = 1 {emp_check};
               """)


@eel.expose
def fc_close(fc_id):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        is_taker = taker_check()
        if not is_taker:
            return

        emp_check = f'and emp_id = {data.a_id}' if data.a_status == 0 else ''
        result = db.execute_query(f"""
               UPDATE food_position
                    SET archived_time={timenow_sql()}, ready_state = 3, archived = 1
                    WHERE fp_pk = "{fc_id}" and ready_state = 2 {emp_check};
               """)


@eel.expose
def fc_create(name, cl_name, w, cal, ingr, comm, extra, price, minutes):
    if not data.is_auth:
        return
    db = ConnectDb()
    if db.mydb:
        is_taker = taker_check()
        if not is_taker:
            return

        check_id = md5_hash('check_id', timenow_sql() + str(uniform(-99, 99)))
        pk = md5_hash(name + cl_name, timenow_sql() + str(uniform(-99, 99)))

        shift = db.execute_query(data.s_sql)
        shift = [s for s in shift if s['closed'] == 0]

        if len(shift) == 0:
            is_menu = 1
            shift_pk = 'NULL'
            check_id = 0
            c = db.execute_query(f"select fp_pk from food_position where is_menu = 1")
            numb = f'М{str(len(c) + 1).zfill(4)}'
        else:
            shift = shift[0]
            is_menu = 0
            shift_pk = shift['shift_pk']
            c = db.execute_query(f"select fp_pk from food_position where is_menu = 0 and shift_pk = {shift_pk}")
            numb = f'А{str(len(c) + 1).zfill(4)}'

        if len(shift) > 0:
            check = db.execute_query(f"""
            INSERT INTO buy_check (check_id, sum, type) 
            VALUES ("{check_id}", {price}, {0})
            """)

        result = db.execute_query(f"""
              INSERT INTO food_position (fp_pk, name, weight, calories, ingredients, client_comment, extra_info, price, minutes_to_cook, is_menu, shift_pk, check_id, number, ordered_time, client_name) 
                    VALUES ("{pk}", "{name}", {w}, {cal}, "{ingr}", "{comm}", "{extra}", {price}, {minutes}, {is_menu}, {shift_pk}, "{check_id}", "{numb}", {timenow_sql()}, "{cl_name}")
              """)
