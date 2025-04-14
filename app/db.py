import mysql.connector


class ConnectDb:
    def __init__(self, host="localhost", user="root", password="1983", database="rem"):
        try:
            self.mydb = mysql.connector.connect(
                host=host,
                port='3306',
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.mydb.cursor(buffered=True, dictionary=True)
        except mysql.connector.Error as err:
            print(f"Ошибка при подключении к базе данных: {err}")
            self.mydb = None
            self.cursor = None

    def execute_query(self, query, params=None):
        if self.mydb is None:
            return None  # Или поднять исключение

        try:

            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            self.mydb.commit()
            return self.cursor.fetchall()  # Возвращаем результаты запроса
        except mysql.connector.Error as err:
            self.mydb.rollback()  # Отмена транзакции в случае ошибки
            raise mysql.connector.Error(err.msg)

    def close_connection(self):
        if self.mydb:
            self.cursor.close()
            self.mydb.close()


# Пример использования:
db = ConnectDb()

# if db.mydb:
#     result = db.execute_query("select * from employer;")  # Замените your_table на имя вашей таблицы
#     if result:
#         for row in result:
#             print(row)
#     else:
#         print("Запрос не выполнен.")
#
#     # Пример с параметрами
#     result_params = db.execute_query("SELECT * FROM buy_check WHERE check_id = '%s'",
#                                      (0,))  # Замените your_table и 1 на нужные значения
#     if result_params:
#         for row in result_params:
#             print(row)
#     else:
#         print("Запрос с параметрами не выполнен.")
#
#     db.close_connection()
