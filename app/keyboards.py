from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Калькулятор калорий")],
        [KeyboardButton(text="Помощь"), KeyboardButton(text="Контакты")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)
