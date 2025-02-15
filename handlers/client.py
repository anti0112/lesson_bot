from aiogram import types
from aiogram.dispatcher import Dispatcher
from handlers.keyboards.kb_client import START, CHOOSE, FORMAT, GROUP, SINGLE, get_kb_days, get_kb_intervals
from core.create_bot import dp, bot
from core.implemented import week_schemas, interval_schemas, user_services
from handlers.utils import get_data_week, get_intervals


async def process_start_command(message: types.Message):
    await message.reply(f"Привет!\nЭтот бот поможет тебе записаться на урок!",
                        reply_markup=START)

@dp.message_handler(commands='add_user_data')
async def add_user(message: types.Message):

    contact = message.contact
    user = user_services.create(message, contact)

    if user:
        await message.answer('Вы успешно зарегестрировались!')
    else:
        await message.answer('Вы уже зарегестрированы!')

    await message.answer(message.from_user.id, "INFO", reply_markup=CHOOSE)

@dp.callback_query_handler(text='choose_lesson')
async def choose_lesson_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Уроки бывают следующих видов:", reply_markup=FORMAT)


@dp.callback_query_handler(text='single_lesson')
async def choose_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Description of single lesson", reply_markup=SINGLE)


@dp.callback_query_handler(text='group_lesson')
async def choose_group_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Description of group lesson", reply_markup=GROUP)


@dp.callback_query_handler(text='choosed_group_lesson')
async def choosed_group_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=get_kb_days(week_schemas.dump(get_data_week())))


@dp.callback_query_handler(text='choosed_single_lesson')
async def choosed_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Days for registration", reply_markup=get_kb_days(week_schemas.dump(get_data_week())))


@dp.callback_query_handler(text_endswith='choosed_day_for_lesson')
async def choosed_day_for_group_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Intervals", reply_markup=get_kb_intervals(interval_schemas.dump(get_intervals())))


@dp.callback_query_handler(text_endswith='choosed_day_for_lesson')
async def choosed_day_for_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Intervals", reply_markup=get_kb_intervals(interval_schemas.dump(get_intervals())))


@dp.callback_query_handler(text_endswith='choosed_interval_for_lesson')
async def choosed_interval_for_group_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы записаны!")


@dp.callback_query_handler(text_endswith='choosed_interval_for_lesson')
async def choosed_interval_for_single_command(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Вы записаны!")

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
