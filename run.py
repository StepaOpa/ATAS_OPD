import asyncio
import logging
import sqlite3


from aiogram import Bot, Dispatcher
from config import TOKENlesha as TOKEN
from app.handlers.calories_calculator_handler import router as calories_router
from app.handlers.utility_handlers import router as utility_router
from app.handlers.survey_handler import router as survey_router

bot = Bot(token=TOKEN) 
dp = Dispatcher()


async def main():
    connection = sqlite3.connect('tablet.sql')
    cursor = connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, ides varchar(50), calories varchar(50))'
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    
    dp.include_router(calories_router)
    dp.include_router(utility_router)
    dp.include_router(survey_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')
