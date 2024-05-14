from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

crpt = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="QR", callback_data="QR"),
            InlineKeyboardButton(text="Aztec", callback_data="Aztec")
        ],
        [
            InlineKeyboardButton(
                text="Datamatrix", callback_data="Datamatrix"),
            InlineKeyboardButton(text="PDF417", callback_data="PDF417")
        ]
    ]
)
