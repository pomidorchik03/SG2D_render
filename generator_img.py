from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackQuery
from aiogram.fsm.context import FSMContext
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
import json
from states import Form
import factories
import zxingcpp
import sys
from PIL import Image

router = Router()
user_msg = {}


@router.message(Form.msg)
async def msg(message: Message, state: FSMContext):
    user_msg.update({message.from_user.id: message.text})
    await state.update_data(msg=message.text)
    await message.answer("Теперь выберите тип шифрования", reply_markup=factories.paginator())


@router.callback_query(factories.Pagination.filter(F.type.in_(["QR", "Datamatrix", "Maxicode", "PDF417", "Aztec"])))
@router.message(Form.finish)
async def encoding2D(call: CallbackQuery, state: FSMContext, bot: Bot):
    print(call.data[4:])
    print(call.from_user.id)
    msg = user_msg[call.from_user.id]
    print(user_msg)
    await state.update_data(finish=call)
    if call.data[4:] == "QR":
        photo = gen_QR(msg)
        with suppress(TelegramBadRequest):
            await bot.send_photo(call.from_user.id, photo=photo)
            await call.answer()

    if call.data[4:] == "Datamatrix":

        photo = gen_Datamatrix(msg)
        with suppress(TelegramBadRequest):
            await bot.send_photo(call.from_user.id, photo=photo)
        await call.answer()

    if call.data[4:] == "Maxicode":

        photo = gen_Maxicode(msg)
        with suppress(TelegramBadRequest):
            await bot.send_photo(call.from_user.id, photo=photo)
            await call.answer()

    if call.data[4:] == "PDF417":

        photo = gen_PDF417(msg)
        with suppress(TelegramBadRequest):
            await bot.send_photo(call.from_user.id, photo=photo)
            await call.answer()

    if call.data[4:] == "Aztec":

        photo = gen_Aztec(msg)
        with suppress(TelegramBadRequest):
            await bot.send_photo(call.from_user.id, photo=photo)
            await call.answer()


def gen_QR(msg):
    print(msg)
    if len(sys.argv) < 3:
        img = zxingcpp.write_barcode(
            zxingcpp.BarcodeFormat.QRCode, msg, quiet_zone=2, width=200, height=200)
    else:
        img = zxingcpp.write_barcode(zxingcpp.barcode_format_from_str(
            sys.argv[1]), sys.argv[2], width=200, height=200)
    png = Image.fromarray(img).save("image.png")
    return FSInputFile(path="image.png",
                       filename="image.png")


def gen_Datamatrix(msg):
    print(msg)
    if len(sys.argv) < 3:
        img = zxingcpp.write_barcode(
            zxingcpp.BarcodeFormat.DataMatrix, msg, quiet_zone=2, width=200, height=200)
    else:
        img = zxingcpp.write_barcode(zxingcpp.barcode_format_from_str(
            sys.argv[1]), sys.argv[2], width=200, height=200)
    png = Image.fromarray(img).save("image.png")
    return FSInputFile(path="image.png",
                       filename="image.png")


# def gen_Maxicode(msg):
#     print(msg)
#     if len(sys.argv) < 3:
#         img = zxingcpp.write_barcode(
#             zxingcpp.BarcodeFormat.MaxiCode, msg, width=200, height=200)
#     else:
#         img = zxingcpp.write_barcode(zxingcpp.barcode_format_from_str(
#             sys.argv[1]), sys.argv[2], width=200, height=200)
#     png = Image.fromarray(img).save("image.png")
#     return FSInputFile(path="D:\питхон\project\image.png",
#                        filename="image.png")


def gen_PDF417(msg):
    print(msg)
    if len(sys.argv) < 3:
        img = zxingcpp.write_barcode(
            zxingcpp.BarcodeFormat.PDF417, msg, quiet_zone=2, width=1000, height=200)
    else:
        img = zxingcpp.write_barcode(zxingcpp.barcode_format_from_str(
            sys.argv[1]), sys.argv[2], width=200, height=200)
    png = Image.fromarray(img).save("image.png")
    return FSInputFile(path="image.png",
                       filename="image.png")


def gen_Aztec(msg):
    print(msg)
    if len(sys.argv) < 3:
        img = zxingcpp.write_barcode(
            zxingcpp.BarcodeFormat.Aztec, msg, quiet_zone=2, width=200, height=200)
    else:
        img = zxingcpp.write_barcode(zxingcpp.barcode_format_from_str(
            sys.argv[1]), sys.argv[2], width=200, height=200)
    png = Image.fromarray(img).save("image.png")
    return FSInputFile(path="image.png",
                       filename="image.png")
