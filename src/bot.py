from aiogram import Bot, Dispatcher, types, executor
from settings import BotSettings
from entity import Message
import worker
import asyncio
bot_settings = BotSettings() # type: ignore

bot = Bot(bot_settings.token.get_secret_value())
dp = Dispatcher(bot)

# TODO: Изучить возможность обрабатывать изображения "пачками"
# Обрабатывать их асинхронно
# Добавить фильтры на выбор, на основании текста сообщения
@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def get_image(message: types.Message) -> None:
    m = Message(chat_id=message.chat.id, file_id=message.document.file_id, flags=[], mime=message.document.mime_subtype)
    loop = asyncio.get_running_loop()
    loop.create_task(worker.process_file(m))
        

        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)