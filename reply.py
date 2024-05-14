from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/gen')
        ],
        [

            KeyboardButton(text='/help'),
            KeyboardButton(text='/info')

        ]
    ],
    resize_keyboard=True
)


crpt_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="назад")
        ]
    ]
)
