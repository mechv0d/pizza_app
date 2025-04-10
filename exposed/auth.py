import eel
from app.data import main_data as data
from app.db import ConnectDb
import datetime


@eel.expose
def exit_auth(force=False):
    if data.is_auth or force:
        data.is_auth = False
        data.a_id = None
        data.a_id_fancy = None
        data.a_passwd = None
        data.a_time = None
        data.a_name = None
        data.a_status = None
        eel.reload()

def get_datetime_string():
    now = datetime.datetime.now()
    return now.strftime("%H:%M, %d.%m.%Y")


@eel.expose
def proceed_auth(uid, passwd, pin):
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query(f"select * from employer where emp_id='{uid}' and pin='{pin}'")
        if len(result) > 0:
            data.is_auth = True
            data.a_id = uid
            data.a_id_fancy = "-".join(uid[i:i + 3] for i in range(0, 9, 3))
            data.a_passwd = passwd
            data.a_time = get_datetime_string()
            data.a_name = result[0]['surname'] + ' ' + result[0]['name']
            match result[0]['status']:
                case 0:
                    data.a_status = 'Работник'
                case 1:
                    data.a_status = 'Администратор'
                case _:
                    data.a_status = 'Неизвестно'

            print(f"Authentication successful. Data: {data}")  # Optional: Print for debugging
            eel.go_to('/index.html')
            db.close_connection()
            return

    print("Authentication failed")  # Optional: Print for debugging
    eel.go_to(
        '/src/pages/auth.html?bad_auth=1')
