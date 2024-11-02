#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Получаем аргументы командной строки
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Подключаемся к базе данных
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Создаем курсор для выполнения SQL-запроса
    cursor = db.cursor()

    # Используем параметризованный запрос для защиты от SQL-инъекций
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Получаем все результаты из выполненного запроса
    rows = cursor.fetchall()

    # Выводим результаты
    for row in rows:
        print(row)

    # Закрываем курсор и соединение
    cursor.close()
    db.close()
