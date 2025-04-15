from datetime import datetime as dt

debug = True

def timenow_sql():
    return dt.now().strftime('"%Y-%m-%d %H:%M:%S"')

class Data:
    is_auth: bool = False
    a_id: str = None
    a_id_fancy: str = None
    a_passwd: str = None
    a_time: str = None
    a_name: str = None
    a_status: str = None
    a_status_raw: int = 0

    s_sql = "SELECT * FROM shift ORDER BY start_time DESC LIMIT 1;"
    s_id: str = None
    s_start_time_raw: dt = None
    s_end_time_raw: dt = None
    s_closed: bool = True
    s_passwd: str = None
    s_takes: list[dict] = []

    @property
    def s_start_time(self):
        return self.s_start_time_raw.strftime('%Y-%m-%d %H:%M:%S') if self.s_start_time_raw else False

    @property
    def s_end_time(self):
        return self.s_end_time_raw.strftime('%Y-%m-%d %H:%M:%S') if self.s_end_time_raw else False


main_data = Data()
