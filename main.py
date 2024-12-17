import asyncio
import logging 
import sys
import os

import aiogram
import aiogram.filters
import aiogram.types
import aiogram.client.default
import aiogram.enums

from config import *
import src


dp = aiogram.Dispatcher()


@dp.message(aiogram.filters.CommandStart())
async def command_start_handler(message: aiogram.types.Message) -> None:
    if message.from_user.id in OP_LIST:
        await message.answer("Authorization succeed", reply_markup=src.main_kb)
    else:
        await message.answer(f"Hello, {message.from_user.id}!")


@dp.message()
async def echo_handler(message: aiogram.types.Message) -> None:
    if message.from_user.id in OP_LIST:
        if message.text == "Minecraft ON":
            for prompt in src.gen_prompts(True):
                c = os.system(prompt)
                if c:
                    await message.answer("Unknown error...")
                else:
                    await message.answer("Done!")

        elif message.text == "Minecraft OFF":
            for prompt in src.gen_prompts(False):
                c = os.system(prompt)
                if c:
                    await message.answer("Unknown error...")
                else:
                    await message.answer("Done!")

        else:
            await message.answer('Unknown command!')


async def main() -> None:
    bot = aiogram.Bot(token=TOKEN, 
          default=aiogram.client.default.DefaultBotProperties(parse_mode=
          aiogram.enums.ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
