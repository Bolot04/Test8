import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_BUY)
    print("База данных подключена!")
    conn.commit()
    conn.close()

def add_list(list):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_LISTS, (list, ))
    conn.commit()
    list_id = cursor.lastrowid
    conn.close()
    return list_id

def get_list(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == "completed":
        cursor.execute(queries.SELECT_LISTS_COMPLETED)
    elif filter_type == "uncompleted":
        cursor.execute(queries.SELECT_LISTS_UNCOMPLETED)
    elif filter_type == "all":
        cursor.execute(queries.SELECT_LISTS)

    conn.commit()
    lists = cursor.fetchall()
    conn.close()
    return lists

def update_list(list_id, new_list=None, completed= None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if new_list is not None:
        cursor.execute(queries.UPDATE_LISTS, (new_list, list_id))
    elif completed is not None:
        cursor.execute("UPDATE lists SET completed = ? WHERE id = ?", (completed, list_id))
    conn.commit()
    conn.close()

def delete_list(list_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETED_LISTS, (list_id, ))
    conn.commit()
    conn.close()