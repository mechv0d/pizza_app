from datetime import datetime


class Data:
    is_auth: bool = False
    a_id: str = None
    a_id_fancy: str = None
    a_passwd: str = None
    a_time: str = None
    a_name: str = None
    a_status: str = None

    s_sql = "SELECT * FROM shift WHERE closed = 0 ORDER BY start_time DESC LIMIT 1;"
    s_id: str = None
    s_start_time: datetime = None
    s_end_time: datetime = None
    s_closed: bool = True
    s_passwd: str = None
    s_takes: list[dict] = []


main_data = Data()
