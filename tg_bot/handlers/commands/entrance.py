from aiogram.filters import CommandStart
from aiogram.types import Message

from . import router


@router.message(CommandStart())
async def start_entrance(message: Message):
    return message.reply(f'Assalomu aleykum {message.from_user.first_name}!\n\n'
                         f'Bo\'timizga hush kelibsiz shikoyatlarni yozish uchun /compliant komandasidan foydalaning')
