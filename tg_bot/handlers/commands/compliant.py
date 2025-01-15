from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from apps.models import Complaint
from . import router


class CompliantState(StatesGroup):
    name = State()
    phone_number = State()
    text = State()


@router.message(Command('compliant'))
async def get_compliant(msg: Message, state: FSMContext):
    buttons = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=msg.from_user.full_name)]], resize_keyboard=True)
    await msg.reply('Ismingizni kiriting', reply_markup=buttons)
    await state.set_state(CompliantState.name)


@router.message(CompliantState.name)
async def get_compliant_name(msg: Message, state: FSMContext):
    buttons = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Kontaktimni yuborish', request_contact=True)]],
        resize_keyboard=True)
    await msg.reply('Rahmat endi telefon raqamingizni kiriting', reply_markup=buttons)
    await state.update_data(name=msg.text)
    await state.set_state(CompliantState.phone_number)


@router.message(CompliantState.phone_number)
async def get_compliant_phone_number(msg: Message, state: FSMContext):
    if msg.contact:
        phone_number = msg.contact.phone_number
    else:
        phone_number = msg.text
    await msg.reply('Ajoyib endi shikoyatingizni yozing', reply_markup=ReplyKeyboardRemove())
    await state.update_data(phone_number=phone_number)
    await state.set_state(CompliantState.text)


@router.message(CompliantState.text)
async def get_compliant_text(msg: Message, state: FSMContext):
    await msg.reply('Shikoyakingiz muvaffaqqiyatli qabul qilindi. Tez orada sizga operatorlarimiz bog\'lanadi')
    data = await state.get_data()
    name = data.get('name')
    phone_number = data.get('phone_number')
    text = msg.text
    await Complaint.objects.acreate(name=name, phone_number=phone_number, text=text)
    await state.clear()
