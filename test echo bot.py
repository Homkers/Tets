import aiogram
from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6211709932:AAFe6rsNqopUy8kc8CYNz86FgKTk7TPjEdk"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(massage: types.Message):
    await massage.answer(text=massage.text)

if __name__ == '__main__':
    executor.start_polling(dp)