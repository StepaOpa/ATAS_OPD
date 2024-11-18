from aiogram.filters import Command
from aiogram.types import Message
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import gpt_interface
import sqlite3

from aiogram import Router

router = Router()


class Survey(StatesGroup):
    goal = State()
    preferences = State()
    ban_products = State()


@router.message(lambda message: message.text == 'Начать опрос')
async def calories_calculator(message: Message, state: FSMContext):
    await state.set_state(Survey.goal)
    await message.answer('Выберите цель:', reply_markup=kb.goals)


@router.message(Survey.goal)
async def goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    await state.set_state(Survey.preferences)
    await message.answer('Напишите Ваши предпочтения в еде через запятую:')


@router.message(Survey.preferences)
async def preferences(message: Message, state: FSMContext):
    await state.update_data(preferences=message.text)
    await state.set_state(Survey.ban_products)
    await message.answer('Напишите Ваши нелюбимые продукты через запятую:')


@router.message(Survey.ban_products)
async def ban_products(message: Message, state: FSMContext):
    await state.update_data(ban_products=message.text)
    data = await state.get_data()
    number_of_calories = generating()[str(message.from_user.id)]
    advice = gpt_interface.get_advice(
        data['goal'], data['ban_products'], number_of_calories)
    await message.answer(advice)
    await state.clear()


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


def idict(a,b):
    c = {}
    for i,j in zip(b,a):
        c[i[0]] = j[0]

    return c