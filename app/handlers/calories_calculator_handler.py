from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router
from app.calories_calculator import calculate_calories
from app.users_calories import auth
router = Router()


class Calories_calculator(StatesGroup):
    age = State()
    sex = State()
    weight = State()
    height = State()
    activity = State()


@router.message(lambda message: message.text == 'Калькулятор калорий')
async def calories_calculator(message: Message, state: FSMContext):
    await state.set_state(Calories_calculator.age)
    await message.answer('Введите ваш возраст')


@router.message(Calories_calculator.age)
async def age(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await state.set_state(Calories_calculator.sex)
    await message.answer('Введите ваш пол')


@router.message(Calories_calculator.sex)
async def sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Calories_calculator.weight)
    await message.answer('Введите ваш вес')


@router.message(Calories_calculator.weight)
async def weight(message: Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    await state.set_state(Calories_calculator.height)
    await message.answer('Введите ваш рост')


@router.message(Calories_calculator.height)
async def height(message: Message, state: FSMContext):
    await state.update_data(height=int(message.text))
    await state.set_state(Calories_calculator.activity)
    await message.answer('Введите ваш уровень активности')


@router.message(Calories_calculator.activity)
async def activity(message: Message, state: FSMContext):
    await state.update_data(activity=message.text)
    data = await state.get_data()
    calories = calculate_calories(data["age"], data["weight"], data["height"], data["sex"],  data["activity"])
    await message.answer(f"{calories}")
    await state.clear()
    auth(calories)