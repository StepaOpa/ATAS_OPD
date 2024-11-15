import sqlite3
from aiogram import types, Dispatcher

dp = Dispatcher()


@dp.message_handler()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    return user_id


def creating_tablet():
    connection = sqlite3.connect('tablet.sql')
    cursor = connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, ides varchar(50), calories varchar(50))'
    cursor.execute(query)
    connection.commit()


def generating():
    connection = sqlite3.connect('tablet.sql')
    cursor = connection.cursor()

    passes = 'SELECT calories FROM users'
    cursor.execute(passes)
    rows1 = cursor.fetchall()

    ids = 'SELECT ides FROM users'
    cursor.execute(ids)
    rows2 = cursor.fetchall()

    id_calories = idict(rows1,rows2)

    return id_calories


async def auth(calories):
    message = types.Message()
    user_id = await handle_message(message)

    connection = sqlite3.connect('tablet.sql')
    cursor = connection.cursor()

    last_dict = generating()
    if user_id not in last_dict.keys():
        sql = f'INSERT INTO users (ides, calories) VALUES ("{user_id}","{calories}")'
        cursor.execute(sql)
        connection.commit()

    cursor.close()
    connection.close()


def idict(a,b):
    c = {}
    for i,j in zip(b,a):
        c[i[0]] = j[0]

    return c
