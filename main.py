from pyexpat.errors import messages

import config
import logging
import asyncio
import random
from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from base import SQL  # подключение класса SQL из файла base

db = SQL('db.db')  # соединение с БД

bot = Bot(token=config.TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

#inline клавиатура
buttons2 = [
        [InlineKeyboardButton(text="Да", callback_data="yes")],
        [InlineKeyboardButton(text="Нет", callback_data="no")]
    ]
kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Прокачка силы✊", callback_data="uppowers")],
        [InlineKeyboardButton(text="Прокачка ловкости🏃", callback_data="uplovkost")],
        [InlineKeyboardButton(text="Дуэли и битвы⚔️", callback_data="duelibitva")],
    ]
kb2 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Битвы с животными", callback_data="pvpanimals")],
        [InlineKeyboardButton(text="Тренировка на мишенях", callback_data="trenmish")]
    ]
kb3 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Уклонение от предмета", callback_data="yklonpredmet")]
         ]
kb4 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Битва с гоблином", callback_data="bgoblin")],
        [InlineKeyboardButton(text="Битва с темным рыцарем", callback_data="btemrizar")],
        [InlineKeyboardButton(text="Битва с светлым рыцарем", callback_data="bsvetrizar")],
         ]
kb5 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Лево", callback_data="pvpaleft")],
        [InlineKeyboardButton(text="Центр", callback_data="pvpacenter")],
        [InlineKeyboardButton(text="Право", callback_data="pvparight")],
    ]
kb6 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Информация обо мне", callback_data="infome")],
        [InlineKeyboardButton(text="Прокачки", callback_data="proka")],
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")],
    ]
kb7 = InlineKeyboardMarkup(inline_keyboard=buttons2)
buttons2 = [
        [InlineKeyboardButton(text="Лево", callback_data="left")],
        [InlineKeyboardButton(text="Центр", callback_data="center")],
        [InlineKeyboardButton(text="Право", callback_data="right")],
    ]
kb8 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons2 = [
        [InlineKeyboardButton(text="Главное меню", callback_data="glavmenu")]
         ]
kb9 = InlineKeyboardMarkup(inline_keyboard=buttons2)
buttons2 = [
        [InlineKeyboardButton(text="Лево", callback_data="dleft")],
        [InlineKeyboardButton(text="Центр", callback_data="dcenter")],
        [InlineKeyboardButton(text="Право", callback_data="dright")],
    ]
kb10 = InlineKeyboardMarkup(inline_keyboard=buttons2)
#когда пользователь написал сообщение
@dp.message()
async def start(message):
    id = message.from_user.id
    if not db.user_exist(id):  # если пользователя нет в бд
        db.add_user(id)  # добавляем
    status = db.get_field("users", id, "status")  # получаем статус пользователя
    if status == 0:
        await message.answer(
            "Привет👋 я главный лесник этого леса. Лес восстал! Магия древних деревьев пробудила животных, и теперь они яростно😡 защищают свои земли🏞. Тебе предстоит пробиваться⚔️ через суровый лес, сражаясь с огромными волками, взбешенными медведями. Используй оружие чтобы выжить и добраться до сердца леса, и заполучить спрятанные сокровища💰."
            "Ты готов оставить информацию о себе?",
            reply_markup=kb)

    #db.update_field("users", id, "status", 1) #изменяем статус пользователя
    #await message.answer("Выбери вариант!", reply_markup=kb2)#отправка сообщения с клавиатурой
    if status == 1:
        name = message.text
        db.update_field("users", id, "name", name)
        #name = db.get_field("users", id, "name")
        #hp = db.get_field("users", id, "hp")
        #power = db.get_field("users", id, "power")
        #lovkost = db.get_field("users", id, "lovkost")
        #yudacha = db.get_field("users", id, "yudacha")
        #brona = db.get_field("users", id, "brona")
        #await message.answer(f"Вот информация о тебе: \nИмя: {name}\nЗдоровье❤️: {hp}\nСила✊: {power}\nЛовкость🏃: {lovkost}\nУдача🤞: {yudacha}\nБроня🛡: {brona}")
        db.update_field("users", id, "status", 2)
        await message.answer("Главное меню:", reply_markup=kb7)
#когда пользователь нажал на inline кнопку
@dp.callback_query()
async def start_call(call):
    id = call.from_user.id
    if not db.user_exist(id):#если пользователя нет в бд
        db.add_user(id)#добавляем
    if call.data == "yes":
        await call.answer("Введите свое имя!")
        db.update_field("users", id, "status", 1)
    if call.data == "uppowers":
        await call.message.answer("Хороший выбор! Давай приступим!", reply_markup=kb3)
        db.update_field("users", id, "status", 2)
    if call.data == "uplovkost":
        await call.message.answer("Хороший выбор! Давай приступим!", reply_markup=kb4)
        db.update_field("users", id, "status", 3)
    if call.data == "duelibitva":
        await call.message.answer("Хороший выбор! Давай приступим!", reply_markup=kb5)
        db.update_field("users", id, "status", 4)
    if call.data == "trenmish":
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Мишень стоит тебе надо попасть по ней! Куда будем стрелять?", reply_markup=kb6)
    if call.data == "pvpaleft":
        r = db.get_field("users",id, "random")
        if r == 1:
            await call.message.answer("Ты попал! Враг был с лево")
            pr = db.get_field("users", id, "power")
            pr += 1
            db.update_field("users", id, "power", pr)
            power = db.get_field("users", id, "power")
            await call.message.answer(f"Твоя сила улучшена! Твоя сила: {power}", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "pvpacenter":
        r = db.get_field("users",id, "random")
        if r == 1:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты попал! Враг был по центру!")
            pr = db.get_field("users", id, "power")
            pr += 1
            db.update_field("users", id, "power", pr)
            power = db.get_field("users", id, "power")
            await call.message.answer(f"Твоя сила улучшена! Твоя сила: {power}", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "pvparight":
        r = db.get_field("users",id, "random")
        if r == 1:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты попал! Враг был с право!")
            pr = db.get_field("users", id, "power")
            pr += 1
            db.update_field("users", id, "power", pr)
            power = db.get_field("users", id, "power")
            await call.message.answer(f"Твоя сила улучшена! Твоя сила: {power}", reply_markup=kb9)
            return
    if call.data == "pvpanimals":
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! животное стоит тебе надо попасть по нему! Куда будем стрелять?", reply_markup=kb6)
    if call.data == "pvpaleft":
        r = db.get_field("users",id, "random")
        if r == 1:
            await call.message.answer("Ты попал! Враг был с лево")
            pr = db.get_field("users", id, "power")
            pr += 1
            db.update_field("users", id, "power", pr)
            power = db.get_field("users", id, "power")
            await call.message.answer(f"Твоя сила улучшена! Твоя сила: {power}", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "pvpacenter":
        r = db.get_field("users",id, "random")
        if r == 1:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты попал! Враг был по центру!")
            pr = db.get_field("users",id, "power")
            pr+=1
            db.update_field("users",id, "power", pr)
            power = db.get_field("users", id, "power")
            await call.message.answer(f"Твоя сила улучшена! Твоя сила: {power}", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
    if call.data == "pvparight":
        r = db.get_field("users",id, "random")
        if r == 1:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты попал! Враг был с право!")
            pr = db.get_field("users", id, "power")
            pr += 1
            db.update_field("users", id, "power", pr)
            power = db.get_field("users", id, "power")
            await call.message.answer(f"Твоя сила улучшена! Твоя сила: {power}", reply_markup=kb9)
            return
    if call.data == "yklonpredmet":
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Противник кинул в тебя булыжник! Куда будешь уклоняться",reply_markup=kb8)
    if call.data == "left":
        r = db.get_field("users", id, "random")
        if r == 1:
            await call.message.answer("Ты не увернулся от булыжника")
            pr = db.get_field("users", id, "lovkost")
            pr -= 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr += 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr += 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
    if call.data == "center":
        r = db.get_field("users", id, "random")
        if r == 1:
            await call.message.answer("Ты увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr += 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты не увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr -= 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr += 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
    if call.data == "right":
        r = db.get_field("users", id, "random")
        if r == 1:
            await call.message.answer("Ты увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr += 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        elif r == 2:
            await call.message.answer("Ты увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr += 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        elif r == 3:
            await call.message.answer("Ты не увернулся от булыжника!")
            pr = db.get_field("users", id, "lovkost")
            pr -= 1
            db.update_field("users", id, "lovkost", pr)
            lovkost = db.get_field("users", id, "lovkost")
            await call.message.answer(f"Твоя сила улучшена! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
    if call.data == "bgoblin":
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb10)
        if call.data == "dleft":
            r = db.get_field("users", id, "random")
            if r == 1:
                await call.message.answer("Ты попал!")
                pr = db.get_field("users", id, "money")
                pr += 10
                db.update_field("users", id, "money", pr)
                money = db.get_field("users", id, "money")
                await call.message.answer(f"Твой баланс пополнен! Твоя твой баланс: {money}", reply_markup=kb9)
                return
            elif r == 2:
                await call.message.answer("Ты промазал!", reply_markup=kb9)
                pr = db.get_field("users", id, "power")
                pr -= 1
                db.update_field("users", id, "power", pr)
                power = db.get_field("users", id, "power")
                await call.message.answer(f"Твоя сила была уменьшена! Твоя сила: {power}", reply_markup=kb9)
                return
            elif r == 3:
                await call.message.answer("Ты промазал!", reply_markup=kb9)
                pr = db.get_field("users", id, "power")
                pr -= 1
                db.update_field("users", id, "power", pr)
                power = db.get_field("users", id, "power")
                await call.message.answer(f"Твоя сила была уменьшена! Твоя сила: {power}", reply_markup=kb9)
                return
        if call.data == "dcenter":
            r = db.get_field("users", id, "random")
            if r == 1:
                await call.message.answer("Ты промазал!", reply_markup=kb9)
                pr = db.get_field("users", id, "power")
                pr -= 1
                db.update_field("users", id, "power", pr)
                power = db.get_field("users", id, "power")
                await call.message.answer(f"Твоя сила была уменьшена! Твоя сила: {power}", reply_markup=kb9)
                return
            elif r == 2:
                await call.message.answer("Ты попал!")
                pr = db.get_field("users", id, "money")
                pr += 10
                db.update_field("users", id, "money", pr)
                money = db.get_field("users", id, "money")
                await call.message.answer(f"Твой баланс пополнен! Твоя твой баланс: {money}", reply_markup=kb9)
                return
            elif r == 3:
                await call.message.answer("Ты промазал!", reply_markup=kb9)
                pr = db.get_field("users", id, "power")
                pr -= 1
                db.update_field("users", id, "power", pr)
                power = db.get_field("users", id, "power")
                await call.message.answer(f"Твоя сила была уменьшена! Твоя сила: {power}", reply_markup=kb9)
                return
        if call.data == "dright":
            r = db.get_field("users", id, "random")
            if r == 1:
                await call.message.answer("Ты промазал!", reply_markup=kb9)
                pr = db.get_field("users", id, "power")
                pr -= 1
                db.update_field("users", id, "power", pr)
                power = db.get_field("users", id, "power")
                await call.message.answer(f"Твоя сила была уменьшена! Твоя сила: {power}", reply_markup=kb9)
                return
            elif r == 2:
                await call.message.answer("Ты промазал!", reply_markup=kb9)
                pr = db.get_field("users", id, "power")
                pr -= 1
                db.update_field("users", id, "power", pr)
                power = db.get_field("users", id, "power")
                await call.message.answer(f"Твоя сила была уменьшена! Твоя сила: {power}", reply_markup=kb9)
                return
            elif r == 3:
                await call.message.answer("Ты попал! Враг был с право!")
                pr = db.get_field("users", id, "money")
                pr += 10
                db.update_field("users", id, "money", pr)
                money = db.get_field("users", id, "money")
                await call.message.answer(f"Твой баланс пополнен! Твоя твой баланс: {money}", reply_markup=kb9)
                return
    if call.data == "infome":
        name = db.get_field("users", id, "name")
        hp = db.get_field("users", id, "hp")
        power = db.get_field("users", id, "power")
        lovkost = db.get_field("users", id, "lovkost")
        yudacha = db.get_field("users", id, "yudacha")
        brona = db.get_field("users", id, "brona")
        money = db.get_field("users", id, "money")
        await call.message.answer(f"Вот информация о тебе: \nИмя: {name}\nЗдоровье❤️: {hp}\nСила✊: {power}\nЛовкость🏃: {lovkost}\nУдача🤞: {yudacha}\nБроня🛡: {brona}\nБаланс: {money}")
    if call.data == "proka":
        await call.message.answer("Давай приступим", reply_markup=kb2)
    if call.data == "glavmenu":
        await call.message.answer("Главное меню", reply_markup=kb7)















    #if call.data == "yes": проверка нажатия на кнопку
    #await call.answer("Оповещение сверху")
    #await call.message.answer("Отправка сообщения")
    #await call.message.edit_text("Редактирование сообщения")
    #await call.message.delete()#удаление сообщения
    await bot.answer_callback_query(call.id)#ответ на запрос, чтобы бот не зависал

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
