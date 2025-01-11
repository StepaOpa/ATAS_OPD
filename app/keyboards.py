from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


settings = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Параметры тела"), KeyboardButton(text="'Предпочтения'")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие",
    one_time_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'Получить план')],
        [KeyboardButton(text="Параметры тела"), KeyboardButton(text="'Предпочтения'")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие",
    one_time_keyboard=True
)

goals = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Похудение"), KeyboardButton(
            text="Набор мышечной массы"), KeyboardButton(text="Поддержание веса")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите цель",
    one_time_keyboard=True
)

user_sex = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'Мужской'), KeyboardButton(text = 'Женский')]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пол",
    one_time_keyboard=True
)

user_activity = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'Не занимаюсь')],
        [KeyboardButton(text = '1 раз в неделю'),KeyboardButton(text = '3 раза в неделю')],
        [KeyboardButton(text = '5 раз в неделю'),KeyboardButton(text = 'Каждый день')]
    ],
    resize_keyboard=True,
    input_field_placeholder="Сколько раз?",
    one_time_keyboard=True
)

user_allergy = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = 'У меня нет аллергий')]
    ],
    one_time_keyboard=True
)