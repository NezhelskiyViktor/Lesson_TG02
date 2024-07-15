import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, KEY
import requests
from googletrans import Translator


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    translator = Translator()


    @dp.message(CommandStart())
    async def start(message: Message):
        await message.answer(f"Приветики , {message.from_user.first_name}, я бот!")

    @dp.message(Command('help'))
    async def help(message: Message):
        await message.answer("Этот бот умеет выполнять команды:\n"
                            + "1. Переводить на английский язык полученные сообщения.\n"
                            + "2. Сохранять в папку img присланные фотографии.\n"
                            +  "3. Отправлять голосовое сообщение по команде /voice\n"
                            +"А также выполнять команды /start (приветствие) и /help (что умеет)")

    @dp.message(Command('voice'))
    async def voice(message: Message):
        voice = FSInputFile("voice1.ogg")
        await message.answer_voice(voice)


    @dp.message(F.photo)
    async def photo(message: Message):
        await message.answer('Сохранил фото в папку img')
        await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')

    @dp.message()
    async def voice(message: Message):
        text = translator.translate(message.text, dest='en').text
        await message.answer(text)


    await dp.start_polling(bot)


    async def main():
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

