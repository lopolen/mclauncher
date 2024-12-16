import aiogram.types

main_kb = aiogram.types.ReplyKeyboardMarkup(keyboard=[
    [aiogram.types.KeyboardButton(text="Minecraft ON"), 
     aiogram.types.KeyboardButton(text="Minecraft OFF")]
], resize_keyboard=True)

on_prompt = "sudo setfacl -m u:illya:r-x /usr/bin/prismlauncher"
off_prompt = "sudo setfacl -m u:illya:r-- /usr/bin/prismlauncher"
