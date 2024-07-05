import logging
import asyncio

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart,Command

BOT_TOKEN =  "ваш токен"

bot=Bot(token=BOT_TOKEN)
dp=Dispatcher()

@dp.message(CommandStart())
async def handle_start(message):
    await message.answer(text=f"Салем,{message.from_user.full_name}\nПривет,{message.from_user.full_name}!\nHello,{message.from_user.full_name}")

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "Привет это эхо бот!" \
           "Сәлем бұл эхо бот" \
           "Hello"
    await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Ожидание."
             "Күте тұрыныз."
             "Wait"
    )

    if message.text:
        await message.answer(
            text=message.text,
            entities=message.entities,
            parse_mode=None,
        )
    elif message.sticker:
        await message.reply_sticker(sticker=message.sticker.file_id)
    elif message.animation:
        await message.reply_animation(animation=message.animation.file_id )
    elif message.photo:
        # Choose the first photo if multiple are sent
        photo = message.photo[0]
        # Extract the file ID for the chosen photo
        photo_file_id = photo.file_id

        # Send the photo as a reply
        await message.reply_photo(photo=photo_file_id)
    else:
        await message.reply_animation(text='Подожди')


    #*await message.answer(text=message.text)
    #await message.reply(text=message.text)

    await message.reply(text=message.text)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
