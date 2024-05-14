from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command, CommandObject, CommandStart
import sys
import zxingcpp
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from PIL import Image
import reply
import cv2
from aiogram.fsm.context import FSMContext
from states import Form
import generator_img
router = Router()

name = "SG2D"


@router.message(Command(commands=["help", "info"]))
async def echo(message: Message):
    msg = message.text.lower()
    if msg == "/help":
        await message.answer(f'Чтобы начать работу с {name}, вы можете использовать следующие команды:\n'
                             f'/start - запустить бота\n'
                             f'/help - получить список команд\n'
                             f'/gen - генерирует штрихкод по указанному сообщению\n'
                             f'Отправка фото - ищет штрихкод на фото и расшифровывает его\n'
                             f'/info - получить информацию о боте')
    elif msg == "/info":
        await message.answer(f'{name} - это Telegram бот, специализирующийся на генерации 2D штрихкодов. Этот бот может создавать различные виды штрихкодов, такие как QR, Datamatrix, PDF417, Aztec. Для использования {name}, вам нужно узнать его команды(/help).')
    else:
        await message.answer("неверная команда")


@router.message(Command(commands=["gen", "generation"]))
async def gen(message: Message, state: FSMContext):
    
    await state.set_state(Form.msg)
    await message.answer("Что хотите зашифровать?")


@router.message(F.photo)
async def dec(message: Message, bot: Bot):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    await bot.download_file(file_path, "ImgForEnc.png")
    img = cv2.imread("ImgForEnc.png")
    results = zxingcpp.read_barcodes(img)
    for result in results:
        print('Found barcode:'
              f'\n Text:    "{result.text}"'
              f'\n Format:   {result.format}'
              f'\n Content:  {result.content_type}'
              f'\n Position: {result.position}')
        with suppress(TelegramBadRequest):
            await message.answer(f"В коде зашифровано сообщение:{result.text}")
    if len(results) == 0:
        print("Не найдены данные в штрихкоде")
        await message.answer("Ой! Мы не можем расшифровать ваш штрихкод.")


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, дорогой пользователь! Тут ты можешь создать двумерный штрихкод.", reply_markup=reply.main)
