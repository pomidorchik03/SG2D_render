from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder, InlineKeyboardMarkup


class Pagination(CallbackData, prefix="pag"):
    type: str


def paginator():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="QR", callback_data=Pagination(type="QR").pack()),
        InlineKeyboardButton(
            text="Aztec", callback_data=Pagination(type="Aztec").pack()),
        InlineKeyboardButton(
            text="Datamatrix", callback_data=Pagination(type="Datamatrix").pack()),
        InlineKeyboardButton(
            text="PDF417", callback_data=Pagination(type="PDF417").pack())
    )
    return builder.as_markup()


# crpt = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="QR", callback_data="QR"),
#             InlineKeyboardButton(text="Aztec", callback_data="Aztec"),
#             InlineKeyboardButton(text="Maxicode", callback_data="Maxicode")
#         ],
#         [
#             InlineKeyboardButton(
#                 text="Datamatrix", callback_data="Datamatrix"),
#             InlineKeyboardButton(text="PDF417", callback_data="PDF417")
#         ]
#     ]
# )
