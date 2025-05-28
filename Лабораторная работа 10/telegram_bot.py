import os
import random
import datetime
import asyncio
import aiohttp
from telebot.async_telebot import AsyncTeleBot
from telebot import types

TOKEN = '7123597470:AAHb1CWkCbtkmPHCwDA9RkPmsT4g8s4thcY'
bot = AsyncTeleBot(TOKEN)

IMAGE_LINKS = [
    'https://httpbin.org/image/jpeg',
    'https://httpbin.org/image/png',
]

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📅 Текущая дата", callback_data='date'),
        types.InlineKeyboardButton("🎲 Случайное число", callback_data='random')
    )
    markup.row(
        types.InlineKeyboardButton("🖼️ Получить изображение", callback_data='meme')
    )
    
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.add("ℹ️ О боте", "🆘 Помощь")
    
    await bot.send_message(
        message.chat.id,
        "👋 Привет! Я демонстрационный бот. Выбери действие:",
        reply_markup=reply_markup
    )
    await bot.send_message(
        message.chat.id,
        "Или используй кнопки ниже:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
async def callback_inline(call):
    try:
        if call.data == 'date':
            now = datetime.datetime.now()
            await bot.send_message(call.message.chat.id, f"📅 Текущая дата и время:\n{now.strftime('%d.%m.%Y %H:%M:%S')}")
        elif call.data == 'random':
            num = random.randint(1, 100)
            await bot.send_message(call.message.chat.id, f"🎲 Случайное число: {num}")
        elif call.data == 'meme':
            url = random.choice(IMAGE_LINKS)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        await bot.send_photo(call.message.chat.id, photo=url)
                    else:
                        await bot.send_message(call.message.chat.id, "⚠️ Изображение временно недоступно")
    except Exception as e:
        error_msg = f"❌ Произошла ошибка:\n{str(e)}"
        print(error_msg)
        await bot.send_message(call.message.chat.id, error_msg)
    finally:
        await bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda message: message.text in ["ℹ️ О боте", "О боте"])
async def about(message):
    await bot.send_message(message.chat.id, "🤖 Я учебный Telegram-бот 🤖\nСоздан для демонстрации возможностей Python")

@bot.message_handler(func=lambda message: message.text in ["🆘 Помощь", "Помощь"])
async def help(message):
    help_text = """
🆘 Справка по боту:
/start - перезапустить бота
ℹ️ О боте - информация
🖼️ Получить изображение - случайная картинка
📅 Текущая дата - показывает дату и время
🎲 Случайное число - генерирует число от 1 до 100
"""
    await bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda message: True)
async def handle_unknown(message):
    await bot.send_message(message.chat.id, "❌ Неизвестная команда. Нажмите /start")

async def main():
    print("Бот запущен и готов к работе!")
    await bot.polling(non_stop=True)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
    except Exception as e:
        print(f"Ошибка: {e}")