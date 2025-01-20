from aiogram.types import Message
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import sqlite3
import gpt_interface
from aiogram import Router

router = Router()


class Survey(StatesGroup):
    goal = State()
    preferences = State()
    allergy = State()
    ban_products = State()
    timeline = State()

@router.message(lambda message: message.text == "'Предпочтения'")
async def calories_calculator(message: Message, state: FSMContext):
    await state.set_state(Survey.goal)
    await message.answer('Выберите цель:', reply_markup=kb.goals)


@router.message(Survey.goal)
async def goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)
    await state.set_state(Survey.preferences)
    await message.answer('Напишите ваши самые любимые продукты через запятую:')


@router.message(Survey.preferences)
async def preferences(message: Message, state: FSMContext):
    await state.update_data(preferences=message.text)
    await state.set_state(Survey.allergy)
    await message.answer('Если у вас есть аллергии, то напишите их через запятую, '
                         'а если нет - нажмите на кнопку снизу.', reply_markup=kb.user_allergy)


@router.message(Survey.allergy)
async def preferences(message: Message, state: FSMContext):
    await state.update_data(allergy=message.text)
    await state.set_state(Survey.ban_products)
    await message.answer('Напишите ваши самые нелюбимые продукты через запятую:')


@router.message(Survey.ban_products)
async def ban_products(message: Message, state: FSMContext):
    await state.update_data(ban_products=message.text)
    data = await state.get_data()
    user_id = str(message.from_user.id)

    connection = sqlite3.connect('tablet.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM users WHERE id = ?', (user_id,))

    if cursor.fetchone():
        sql = '''
            UPDATE users 
            SET goal = ?, favorite_foods = ?,allergy = ?, ban_products = ?
            WHERE id = ?
        '''
        cursor.execute(sql, (data['goal'], data['preferences'],data['allergy'],data['ban_products'], user_id))
    else:
        sql = '''
        INSERT INTO users (id, goal, favorite_foods, allergy, ban_products) 
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(sql,(user_id,data["goal"],data["preferences"],data["allergy"],data["ban_products"]))

    connection.commit()
    await message.answer('Отлично! Если все параметры заполнены верно, то вы сможете получить свой План.',
                         reply_markup=kb.main_menu)
    await state.clear()


@router.message(lambda message: message.text == 'Получить план')
async def give_advice(message: Message, state: FSMContext):
    await message.answer('На сколько дней хотите получить план? (цифрой от 1 до 7)')
    await state.set_state(Survey.timeline)


@router.message(Survey.timeline)
async def give_advice(message: Message, state: FSMContext):
    await state.update_data(timeline=message.text)
    connection = sqlite3.connect('tablet.db')
    cursor = connection.cursor()
    data = await state.get_data()
    user_id = str(message.from_user.id)

    sql = '''
                UPDATE users 
                SET timeline = ?
                WHERE id = ?
            '''
    cursor.execute(sql, (data["timeline"], user_id))
    connection.commit()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    anydata = cursor.fetchone()

    calories = anydata[1]
    goal = anydata[2]
    preferences = anydata[3]
    allergy = anydata[4]
    ban_products = anydata[5]
    timeline = anydata[6]

    advice = gpt_interface.get_advice(goal, preferences, ban_products, allergy, calories, timeline)
    await message.answer(advice, reply_markup=kb.main_menu)
    await state.clear()