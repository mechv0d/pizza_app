import eel


@eel.expose
def create_take(tid, uid, sname, name, lname, status, st_time, end_time, place, closed):
    with open('src/components/shifter.html', 'r', encoding='utf-8') as f:
        shifter = f.read()
        shifter = shifter.replace('%tid', str(tid)) \
            .replace('%uid', uid) \
            .replace('%name', f'{sname} {name} {lname}') \
            .replace('%status', 'admin' if status == 1 else '') \
            .replace('%place', place) \
            .replace('%stime', str(st_time)) \
            .replace('%etime', str(end_time))

        return shifter
