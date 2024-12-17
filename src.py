import aiogram.types
from config import *


def gen_prompts(status: bool) -> list:
    l = []
    for i in USER_LIST:
        if status:
            l.append(f"setfacl -m u:{i}:r-x /usr/bin/prismlauncher")
        else:
            l.append(f"setfacl -m u:{i}:r-- /usr/bin/prismlauncher")
    
    return l


main_kb = aiogram.types.ReplyKeyboardMarkup(keyboard=[
    [aiogram.types.KeyboardButton(text="Minecraft ON"), 
     aiogram.types.KeyboardButton(text="Minecraft OFF")]
], resize_keyboard=True)

