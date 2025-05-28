# Ответы на контрольные вопросы

### 1. Какой модуль используется для асинхронной работы с Telegram API?
Для асинхронной работы используется модуль `pyTelegramBotAPI` (асинхронная версия - `async_telebot`):
```python
from telebot.async_telebot import AsyncTeleBot
```

### 2. Чем отличается message_handler от callback_query_handler?
- `message_handler` - обрабатывает обычные текстовые сообщения и команды
- `callback_query_handler` - обрабатывает нажатия на inline-кнопки

### 3. Как создать inline-кнопку и обработать её нажатие?
Создание кнопки:
```python
markup = types.InlineKeyboardMarkup()
btn = types.InlineKeyboardButton("Текст", callback_data="action")
markup.add(btn)
```

Обработка нажатия:
```python
@bot.callback_query_handler(func=lambda call: call.data == "action")
async def handler(call):
    await bot.send_message(call.message.chat.id, "Кнопка нажата")
```

### 4. Как использовать asyncio совместно с ботом?
1. Все обработчики должны быть асинхронными (`async def`)
2. Запуск через `asyncio.run()`:
```python
async def main():
    await bot.polling(non_stop=True)

if __name__ == '__main__':
    asyncio.run(main())
```

### 5. В чём отличие обычной клавиатуры от inline-клавиатуры?
| Особенность      | Обычная клавиатура       | Inline-клавиатура      |
|------------------|-------------------------|-----------------------|
| Расположение     | Под полем ввода         | В сообщении           |
| Видимость        | Исчезает                | Остаётся              |
| Обработка        | Через message_handler   | Через callback_query_handler |
