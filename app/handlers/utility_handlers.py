from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n'
                         'Если хочешь получить персональный план питания, тогда выполни небольшую настройку,'
                          ' нажимая кнопки "Предпочтения" и "Параметры тела".', reply_markup=kb.settings)


# Help handler
@router.message(lambda message: message.text == 'Помощь')
async def help(message: Message):
    await message.answer('Список команд:\nКалькулятор калорий\nПомощь\nМои данные')
