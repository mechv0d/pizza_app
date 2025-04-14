from datetime import datetime, timedelta
import eel
from app.data import main_data as data
from app.db import ConnectDb
from app.get_employer import get_employer


def time_until_ready(taken_time, minutes_to_cook):
    if not isinstance(taken_time, datetime) or not isinstance(minutes_to_cook, int) or minutes_to_cook < 0:
        print(type(taken_time))
        print('isinstance(taken_time, datetime)', isinstance(taken_time, datetime))
        print('isinstance(minutes_to_cook, int)', isinstance(minutes_to_cook, int))
        print('minutes_to_cook < 0', minutes_to_cook < 0)
        return ''

    ready_time = taken_time + timedelta(minutes=minutes_to_cook)
    time_difference = ready_time - datetime.now()
    minutes_left = time_difference.total_seconds() // 60

    return f"{int(minutes_left)} мин. ({ready_time.strftime('%H:%M')})"


@eel.expose
def create_food_card(fName, fNumb, fClient, fWeight, fCal, fPrice, fTips, fIngredients, fTakeTime, fTaker,
                     fReadyState, fReadyTime, fClientComment, fExtraInfo, fTimeToCook):
    with open('src/components/food-card.html', 'r', encoding='utf-8') as f:
        emp = get_employer(fTaker)
        r_state = 'Неизвестно'
        match fReadyState:
            case -3:
                r_state = 'Отменено (админ)'
            case -2:
                r_state = 'Отменено (система)'
            case -1:
                r_state = 'Отменено (клиент)'
            case 0:
                r_state = 'Взято'
            case 1:
                r_state = 'Готовится'
            case 2:
                r_state = 'Готово'
            case 3:
                r_state = 'Получено'
        if fReadyState < 2 and fReadyState >= 0:
            r_color = 'orange'
        elif fReadyState == 2:
            r_color = 'green'
        elif fReadyState < 0:
            r_color = 'red'
        elif fReadyState == 3:
            r_color = ''
        card = f.read()
        r_time = time_until_ready(fTakeTime, fTimeToCook) if fReadyState == 1 \
            else "{:02d}:{:02d}".format(fReadyTime.seconds // 3600, (fReadyTime.seconds % 3600) // 60)
        card = card.replace('%fName', fName) \
            .replace('%fNumb', f'{fNumb[0]}-{fNumb[1::]}') \
            .replace('%fClientName', fClient) \
            .replace('%fWeight', str(fWeight)) \
            .replace('%fCal', str(fCal)) \
            .replace('%fPrice', str(fPrice)) \
            .replace('%fTips', str(fTips)) \
            .replace('%fIngredients', fIngredients) \
            .replace('%fTakeTime', fTakeTime.strftime("%H:%M") if fTakeTime else '') \
            .replace('%fTaker', f'{emp["surname"]} {emp["name"]}' if fTakeTime else '') \
            .replace('%fReadyState', r_state) \
            .replace('%fReadyColor', r_color) \
            .replace('%fReadyTime', r_time) \
            .replace('%fClientComment', f'<br>Комментарий: {fClientComment}' if fClientComment else '') \
            .replace('%fExtraInfo', f'<br>Доп. информация: {fExtraInfo}' if fExtraInfo else '') \
            .replace('%fArchiveBtnDisplay', 'none') \
            .replace('%fReadyButtonDisplay', 'flex' if fReadyState == 1 else 'none') \
            .replace('%fTakeButtonDisplay', 'flex' if fReadyState == 0 else 'none') \
            .replace('%fMakeArchiveBtnDisplay', 'flex' if fReadyState == 3 or fReadyState < 0 else 'none')

        return card


@eel.expose
def load_food_cards():
    fp_list = []
    if not data.is_auth:
        return fp_list
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query('select * from food_position where archived = 0 order by ordered_time limit 501')
        for fp in result:
            fp_list.append(create_food_card(
                fp["name"],
                fp["number"],
                fp["client_name"],
                fp["weight"],
                fp["calories"],
                fp["price"],
                fp["tips"],
                fp["ingredients"],
                fp["taken_time"],
                fp["emp_id"],
                fp["ready_state"],
                fp["ready_time"],
                fp["client_comment"],
                fp["extra_info"],
                fp["minutes_to_cook"]
            ))

        db.close_connection()
        return fp_list

    print("Load Food Cards failed")  # Optional: Print for debugging
    eel.go_to('/index.html')
