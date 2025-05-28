from pyrogram import filters
from pyrogram.types import Message

from ZOYA_MUSIC import app
from ZOYA_MUSIC.core.call import ZOYA

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await ZOYA.stop_stream_force(message.chat.id)
