from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.types import Message
import app.keyboards as kb
router = Router()


# Start handler
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!', reply_markup=kb.main_menu)

# Help handler


@router.message(lambda message: message.text == 'Помощь')
async def help(message: Message):
    await message.answer('Список команд:\nКалькулятор калорий\nПомощь\nМои данные')
