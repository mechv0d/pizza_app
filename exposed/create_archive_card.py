import eel
from app.db import ConnectDb
from app.get_employer import get_employer
from app.data import main_data as data


@eel.expose
def create_archive_card(fName, fNumb, fClient, fWeight, fCal, fPrice, fTips, fIngredients, fTakeTime, fTaker,
                        fReadyState, fReadyTime, fArchiveTime, fClientComment, fExtraInfo):
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
        card = card.replace('%fName', fName) \
            .replace('%fNumb', f'{fNumb[0]}-{fNumb[1::]}') \
            .replace('%fClientName', fClient) \
            .replace('%fWeight', str(fWeight)) \
            .replace('%fCal', str(fCal)) \
            .replace('%fPrice', str(fPrice)) \
            .replace('%fTips', str(fTips)) \
            .replace('%fIngredients', fIngredients) \
            .replace('%fTakeTime', fTakeTime.strftime("%H:%M")) \
            .replace('%fTaker', f'{emp["surname"]} {emp["name"]}') \
            .replace('%fReadyState', r_state) \
            .replace('%fReadyColor', r_color) \
            .replace('%fReadyTime',
                     "{:02d}:{:02d}".format(fReadyTime.seconds // 3600, (fReadyTime.seconds % 3600) // 60)) \
            .replace('%fArchiveTime', fArchiveTime.strftime("%H:%M %d.%m.%Y")) \
            .replace('%fClientComment', f'<br>Комментарий: {fClientComment}' if fClientComment else '') \
            .replace('%fExtraInfo', f'<br>Доп. информация: {fExtraInfo}' if fExtraInfo else '') \
            .replace('%fArchiveBtnDisplay', 'flex') \
            .replace('%fMakeArchiveBtnDisplay', 'none') \
            .replace('%fReadyButtonDisplay', 'none')

        return card


@eel.expose
def load_archive_cards():
    fp_list = []
    if not data.is_auth:
        return fp_list
    db = ConnectDb()
    if db.mydb:
        result = db.execute_query('select * from food_position where archived = 1 order by archived_time desc limit 10')
        for fp in result:
            fp_list.append(create_archive_card(
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
                fp["archived_time"],
                fp["client_comment"],
                fp["extra_info"]
            ))

        db.close_connection()
        return fp_list

    print("Load Shift failed")  # Optional: Print for debugging
    eel.go_to('/index.html')
