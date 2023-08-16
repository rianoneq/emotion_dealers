from src.keyboards import keyboard

from aiogram.filters import Command
from aiogram import types
from aiogram import Router
from aiogram import Bot

route = Router()

bot = Bot(token='6477814839:AAH-oy1vB9toWF2r7CmvVdUV3yjxkUERigQ')

@route.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer('Тестируем WebApp!',
                           reply_markup=keyboard)

PRICE = {
    '1': [types.LabeledPrice(label='Item1', amount=100000)],
    '2': [types.LabeledPrice(label='Item2', amount=200000)],
    '3': [types.LabeledPrice(label='Item3', amount=300000)],
    '4': [types.LabeledPrice(label='Item4', amount=400000)],
    '5': [types.LabeledPrice(label='Item5', amount=500000)],
    '6': [types.LabeledPrice(label='Item6', amount=600000)]
}

@route.message(lambda msg: msg.web_app_data)
async def select_endpoints(web_app_message):
  
  if web_app_message.web_app_data.data:
    web_app_data: str = web_app_message.web_app_data.data
    print(web_app_data)    

# @route.message()
# async def buy_process(web_app_message):
#     await web_app_message.answer(web_app_message.chat.id,
#                            title='Laptop',
#                            description='Description',
#                            provider_token='pay_token',
#                            currency='rub',
#                            need_email=True,
#                            prices=PRICE[f'{web_app_message.web_app_data.data}'],
#                            start_parameter='example',
#                            payload='some_invoice')

# @route.pre_checkout_query(lambda query: True)
# async def pre_checkout_process(pre_checkout: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)

# @route.message(types.ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Платеж прошел успешно!')