from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio

TOKEN = "8776241574:AAEInesfyjcu_ljNcfS61PaVKfoAyNIBufE"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💰 Расчетный счет", callback_data="account")],
            [InlineKeyboardButton(text="📲 Эквайринг", callback_data="acquiring")],
            [InlineKeyboardButton(text="📱 Зарплатный проект", callback_data="payroll")],
            [InlineKeyboardButton(text="💳 Бизнес-карта", callback_data="bcard")],
            [InlineKeyboardButton(text="💳 Кредитная бизнес-карта", callback_data="creditcard")],
            [InlineKeyboardButton(text="🏦 Кредиты", callback_data="credits")],
            [InlineKeyboardButton(text="💵 Депозиты", callback_data="deposits")],
            [InlineKeyboardButton(text="🛡️ Банковская гарантия", callback_data="guarantee")],
            [InlineKeyboardButton(text="📜 Все инструкции по продуктам", url="https://www.sberbank.com/help/business/sbbol")]
        ]
    )


def account_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://www.sberbank.ru/ru/s_m_business/open-accounts")],
            [InlineKeyboardButton(text="📄 Тарифы", url="https://www.sberbank.ru/ru/s_m_business/bankingservice/rko")],
            [InlineKeyboardButton(text="📋 Документы для открытия счета", url="https://www.sberbank.com/help/business/docs_rko")],
            [InlineKeyboardButton(text="🧾 Спец. счета", url="https://www.sberbank.ru/ru/legal/bankingservice/spec-scheta")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def acquiring_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте и расчет ставки", url="https://www.sberbank.ru/ru/s_m_business/bankingservice/acquiring_total")],
            [InlineKeyboardButton(text="💳 Как подключить эквайринг?", url="https://www.sberbank.com/help/business/sbbol/100292")],
            [InlineKeyboardButton(text="💳 Как подключить оплаты по СБП QR?", url="https://www.sberbank.com/help/business/sbbol/100836")],
            [InlineKeyboardButton(text="💳 Как подключить оплаты по SberPay QR?", url="https://www.sberbank.com/help/business/sbbol/100013")],
            [InlineKeyboardButton(text="💳 Как подключить приложение «Мобильный кассир»?", url="https://www.sberbank.com/help/business/sbbol/100986")],
            [InlineKeyboardButton(text="💳 Информация об интернет-эквайринге ЮKassa", url="https://www.sberbank.ru/ru/s_m_business/bankingservice/yookassa")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def payroll_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://example.com/payroll1")],
            [InlineKeyboardButton(text="📄 Как подключить зарплатный проект?", url="https://www.sberbank.com/help/business/sbbol/100048")],
            [InlineKeyboardButton(text="📑 Как создать зарплатный реестр?", url="https://www.sberbank.com/help/business/sbbol/100067")],
            [InlineKeyboardButton(text="👤 Как создать реестр на выплату самозанятым?", url="https://www.sberbank.com/help/business/sbbol/100460")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def bcard_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://www.sberbank.ru/ru/s_m_business/bankingservice/cards/corporatecards")],
            [InlineKeyboardButton(text="📄 Как выпустить обычную или кредитную бизнес-карту?", url="https://www.sberbank.com/help/business/sbbol/100047")],
            [InlineKeyboardButton(text="📄 Как закрыть бизнес-карту?", url="https://www.sberbank.com/help/business/sbbol/100176")],
            [InlineKeyboardButton(text="📄 Как заказать пластиковую бизнес-карту для цифровой?", url="https://www.sberbank.com/help/business/sbbol/100940")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def creditcard_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://www.sberbank.ru/ru/s_m_business/bankingservice/cards/credit-businesscards")],
            [InlineKeyboardButton(text="📄 Как посмотреть льготный период по кредитной бизнес-карте?", url="https://www.sberbank.com/help/business/sbbol/100954")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def credits_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://www.sberbank.ru/ru/s_m_business/onlinecredit")],
            [InlineKeyboardButton(text="📄 Как подать заявку на кредит без посещения банка?", url="https://www.sberbank.com/help/business/sbbol/100112")],
            [InlineKeyboardButton(text="📄 Как рассчитать кредитный потенциал?", url="https://www.sberbank.com/help/business/sbbol/100871")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def deposits_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://www.sberbank.ru/ru/s_m_business/deposits")],
            [InlineKeyboardButton(text="📄 Как разместить депозит на публичных условиях?", url="https://www.sberbank.com/help/business/sbbol/100119")],
            [InlineKeyboardButton(text="📄 Как разместить депозит на индивидуальных условиях?", url="https://www.sberbank.com/help/business/sbbol/100120")],
            [InlineKeyboardButton(text="📄 Как разместить денежные средства в виде неснижаемого остатка?", url="https://www.sberbank.com/help/business/sbbol/101010")],
            [InlineKeyboardButton(text="📄 Как отозвать депозит?", url="https://www.sberbank.com/help/business/sbbol/100262")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )


def guarantee_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📘 Информация о продукте", url="https://www.sberbank.ru/ru/s_m_business/credits/warranty")],
            [InlineKeyboardButton(text="📄 Как посмотреть условия по выданной гарантии?", url="https://www.sberbank.com/help/business/sbbol/101050")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back_main")]
        ]
    )



@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Я внутренний помощник для новых сотрудников.\n\n"
        "Здесь ты можешь быстро изучить банковские продукты и инструкции по работе.\n\n"
        "📌 Как пользоваться ботом:\n"
        "— Выбери интересующий продукт из меню\n"
        "— Открой инструкции или материалы\n"
        "— Используй кнопку «Назад» для навигации\n\n"
        "💡 Совет: начни с «Расчетного счета» — это базовый продукт для работы.\n\n"
        "Удачного обучения 🚀",
        reply_markup=main_menu()
    )


@dp.callback_query(F.data == "account")
async def account_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по расчетному счету:",
        reply_markup=account_menu()
    )


@dp.callback_query(F.data == "acquiring")
async def acquiring_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по эквайрингу:",
        reply_markup=acquiring_menu()
    )


@dp.callback_query(F.data == "payroll")
async def payroll_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по зарплатному проекту:",
        reply_markup=payroll_menu()
    )


@dp.callback_query(F.data == "bcard")
async def bcard_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по бизнес-картам:",
        reply_markup=bcard_menu()
    )


@dp.callback_query(F.data == "creditcard")
async def creditcard_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по кредитной бизнес-карте:",
        reply_markup=creditcard_menu()
    )


@dp.callback_query(F.data == "credits")
async def credits_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по кредитам:",
        reply_markup=credits_menu()
    )


@dp.callback_query(F.data == "deposits")
async def deposits_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по депозитам:",
        reply_markup=deposits_menu()
    )


@dp.callback_query(F.data == "guarantee")
async def guarantee_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Материалы по банковским гарантиям:",
        reply_markup=guarantee_menu()
    )



@dp.callback_query(F.data == "back_main")
async def back_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите продукт для изучения:",
        reply_markup=main_menu()
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())