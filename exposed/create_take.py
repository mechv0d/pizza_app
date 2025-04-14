import eel
from app.data import main_data as data


@eel.expose
def create_take(tid, uid, sname, name, lname, status, st_time, end_time, place, closed):
    with open('src/components/shifter.html', 'r', encoding='utf-8') as f:
        shifter = f.read()
        shifter = shifter.replace('%tid', str(tid)) \
            .replace('%uid', uid) \
            .replace('%name',
                     f'{sname} {name} {lname if lname else ""} {"(Вы)" if uid in [data.a_id_fancy, data.a_id] else ""}') \
            .replace('%status', 'admin' if status == 1 else '') \
            .replace('%place', place) \
            .replace('%stime', str(st_time)) \
            .replace('%etime', str(end_time)) \
            .replace('%disp', 'none' if closed in [1, True] or uid in [data.a_id_fancy, data.a_id] else 'flex')

        return shifter
