from app.db import ConnectDb


def get_employer(id: str):
    db = ConnectDb()
    if db.mydb and id:
        result = db.execute_query(f'select * from employer where emp_id = {id} limit 1')[0]
        if len(result) > 0:
            return result
    return None
