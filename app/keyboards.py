from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Калькулятор калорий")],
        [KeyboardButton(text="Помощь"), KeyboardButton(text="Начать опрос")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)

goals = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Похудение"), KeyboardButton(
            text="Набор массы"), KeyboardButton(text="Поддержание здорового питания")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите цель"
)
