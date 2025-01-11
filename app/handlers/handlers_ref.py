from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from aiogram import Router

router = Router()


class Reg(StatesGroup):
    name = State()
    age = State()


# @router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer('Hello!', reply_markup=kb.main_menu)


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Enter your name')


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.age)
    await message.answer('Enter your age')


@router.message(Reg.age)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(f'Your name: {data["name"]}\nYour age: {data["age"]}')
    await state.clear()
