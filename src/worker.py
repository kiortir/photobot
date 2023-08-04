import asyncio
from pathlib import Path
from entity import Message
from io import BytesIO
from typing import cast
import aiofiles
from PIL import Image

import bot
from settings import StaticSettings
from concurrent.futures import ProcessPoolExecutor

STATIC = Path("./static")
executor = ProcessPoolExecutor()

def apply_filter(file: BytesIO, mime: str, filters: list[str]) -> BytesIO:
    new = BytesIO()
    img = Image.open(file, formats=["PNG", "JPEG"])
    img = img.convert("L")
    img.save(new, format="PNG")
    return new
    
async def save_file(file: BytesIO, file_id: str, chat_id: int):
    fp = STATIC / f"{chat_id}+{file_id}"
    async with aiofiles.open(fp,"wb") as f:
        await f.write(file.getbuffer())
    return fp

async def enqueue_send(chat_id: int, fp: Path):
    async with aiofiles.open(fp,"rb") as f:
        with BytesIO() as i:
            i.write(await f.read())
            i.seek(0)
            await bot.bot.send_photo(chat_id, i)

async def process_file(message: Message):
    file = cast(BytesIO, await bot.bot.download_file_by_id(message.file_id))
    loop = asyncio.get_running_loop()
    file = await loop.run_in_executor(executor, apply_filter, file, message.mime, message.flags)
    # file = await apply_filter(file, message.mime, message.flags)
    fp = await save_file(file, message.file_id, message.chat_id)
    await enqueue_send(message.chat_id, fp)
