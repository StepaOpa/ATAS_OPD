import sqlite3

from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router
from app.calories_calculator import calculate_calories
import app.keyboards as kb
router = Router()


class Calories_calculator(StatesGroup):
    age = State()
    sex = State()
    weight = State()
    height = State()
    activity = State()


@router.message(lambda message: message.text == 'Параметры тела')
async def calories_calculator(message: Message, state: FSMContext):
    await state.set_state(Calories_calculator.age)
    await message.answer('Введите ваш возраст (цифрой)')


@router.message(Calories_calculator.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await state.set_state(Calories_calculator.sex)
    await message.answer('Выберите ваш пол',reply_markup=kb.user_sex)


@router.message(Calories_calculator.sex)
async def sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Calories_calculator.weight)
    await message.answer('Введите ваш вес (в килограммах)')


@router.message(Calories_calculator.weight)
async def weight(message: Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    await state.set_state(Calories_calculator.height)
    await message.answer('Введите ваш рост (в сантиметрах)')


@router.message(Calories_calculator.height)
async def height(message: Message, state: FSMContext):
    await state.update_data(height=int(message.text))
    await state.set_state(Calories_calculator.activity)
    await message.answer('Сколько раз в неделю вы занимаетесь спортом?',reply_markup=kb.user_activity)


@router.message(Calories_calculator.activity)
async def activity(message: Message, state: FSMContext):
    await state.update_data(activity=message.text)
    data = await state.get_data()
    user_id = str(message.from_user.id)
    connection = sqlite3.connect('tablet.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM users WHERE id = ?',(user_id,))
    anydata = cursor.fetchone()
    calories = calculate_calories(data["age"], data["weight"], data["height"], data["sex"], data["activity"])

    if anydata:
        sql = '''
        UPDATE users 
        SET calories = ? 
        WHERE id = ?
        '''
        cursor.execute(sql,(calories,user_id))
        await message.answer(f"Ваша суточная норма калорий для поддержания веса - {calories}.\n"
                             "Теперь определите свои 'Предпочтения' и получите План питания.",
                             reply_markup=kb.main_menu)
    else:
        sql = '''
        INSERT INTO users (id, calories)
        VALUES (?, ?)
        '''
        cursor.execute(sql, (user_id,calories))
        await message.answer(f'Ваша суточная норма калорий для поддержания веса - {calories}\n'
                             "Если 'Предпочтения' уже определны, вы можете получить План питания.",reply_markup=kb.main_menu)
    await state.clear()
    connection.commit()
    cursor.close()
    connection.close()