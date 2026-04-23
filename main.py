
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
buttons = [
        [InlineKeyboardButton(text="Да", callback_data="yes")]
    ]
kb = InlineKeyboardMarkup(inline_keyboard=buttons)

buttons2 = [
        [InlineKeyboardButton(text="Прокачка силы✊", callback_data="uppowers")],
        [InlineKeyboardButton(text="Прокачка ловкости🏃", callback_data="uplovkost")],
    ]
kb2 = InlineKeyboardMarkup(inline_keyboard=buttons2)

buttons3 = [
        [InlineKeyboardButton(text="Битвы с животными", callback_data="pvpanimals")],
        [InlineKeyboardButton(text="Тренировка на мишенях", callback_data="trenmish")]
    ]
kb3 = InlineKeyboardMarkup(inline_keyboard=buttons3)

buttons4 = [
        [InlineKeyboardButton(text="Уклонение от предмета", callback_data="yklonpredmet")]
         ]
kb4 = InlineKeyboardMarkup(inline_keyboard=buttons4)

buttons5 = [
        [InlineKeyboardButton(text="Битва с гоблином", callback_data="bgoblin")],
        [InlineKeyboardButton(text="Битва с темным рыцарем", callback_data="btemrizar")],
        [InlineKeyboardButton(text="Битва с светлым рыцарем", callback_data="bsvetrizar")],
        [InlineKeyboardButton(text="Битва с Ивентовым Боссом", callback_data="ivent_boss")],
         ]
kb5 = InlineKeyboardMarkup(inline_keyboard=buttons5)

buttons6 = [
        [InlineKeyboardButton(text="Лево", callback_data="left")],
        [InlineKeyboardButton(text="Центр", callback_data="center")],
        [InlineKeyboardButton(text="Право", callback_data="right")],
    ]
kb6 = InlineKeyboardMarkup(inline_keyboard=buttons6)

buttons7 = [
        [InlineKeyboardButton(text="Информация обо мне", callback_data="infome")],
        [InlineKeyboardButton(text="Прокачки", callback_data="proka")],
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")],
        [InlineKeyboardButton(text="Дуэли и битвы⚔️", callback_data="duelibitva")],
    ]
kb7 = InlineKeyboardMarkup(inline_keyboard=buttons7)


buttons9 = [
        [InlineKeyboardButton(text="Главное меню", callback_data="glavmenu")]
         ]
kb9 = InlineKeyboardMarkup(inline_keyboard=buttons9)
buttons11 = [
        [InlineKeyboardButton(text="Возродится", callback_data="vozr")],
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")]
    ]
kb11 = InlineKeyboardMarkup(inline_keyboard=buttons11)
buttons12 = [
        [InlineKeyboardButton(text="Магазин", callback_data="magaz")]
    ]
kb12 = InlineKeyboardMarkup(inline_keyboard=buttons12)
buttons13 = [
    [InlineKeyboardButton(text="Аптечка   [100 монет]", callback_data="apt")],
    [InlineKeyboardButton(text="Броня", callback_data="bron")]
    ]
kb13 = InlineKeyboardMarkup(inline_keyboard=buttons13)
buttons14 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="apt_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb14 = InlineKeyboardMarkup(inline_keyboard=buttons14)
buttons15 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="der_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb15 = InlineKeyboardMarkup(inline_keyboard=buttons15)
buttons17 = [
        [InlineKeyboardButton(text="Деревянная броня", callback_data="der_brona")],
        [InlineKeyboardButton(text="Кожанная броня", callback_data="koz_brona")],
        [InlineKeyboardButton(text="Железнная броня", callback_data="zel_brona")],
        [InlineKeyboardButton(text="Стальнная броня", callback_data="stal_brona")],
        [InlineKeyboardButton(text="Драконья броня", callback_data="drag_brona")],
        [InlineKeyboardButton(text="Карбонновая броня", callback_data="carb_brona")],
        [InlineKeyboardButton(text="Мифриловая броня [ИВЕНТ]", callback_data="mif_brona")],
        [InlineKeyboardButton(text="Обсидианновая броня [ИВЕНТ]", callback_data="obs_brona")],
        [InlineKeyboardButton(text="Адомантовая броня [ИВЕНТ]", callback_data="ado_brona")],
    ]
kb17 = InlineKeyboardMarkup(inline_keyboard=buttons17)

buttons18 = [
    [InlineKeyboardButton(text="Деревянные штаны  [1000 монет]", callback_data="der_bron")],
    [InlineKeyboardButton(text="Деревяннные куртка [1000 монет]", callback_data="der_bron")],
    [InlineKeyboardButton(text="Деревяннные кроссовки [1000 монет]", callback_data="der_bron")],]
kb18 = InlineKeyboardMarkup(inline_keyboard=buttons18)
buttons19 = [
    [InlineKeyboardButton(text="Кожанные штаны  [2000 монет]", callback_data="koz_bron")],
    [InlineKeyboardButton(text="Кожанная куртка  [2000 монет]", callback_data="koz_bron")],
    [InlineKeyboardButton(text="Кожанные кроссовки [2000 монет]", callback_data="koz_bron")],
    ]
kb19 = InlineKeyboardMarkup(inline_keyboard=buttons19)
buttons20 = [
    [InlineKeyboardButton(text="Железнные штаны  [3000 монет]", callback_data="zel_bron")],
    [InlineKeyboardButton(text="Железнная кольчуга  [3000 монет]", callback_data="zel_bron")],
    [InlineKeyboardButton(text="Железнные сапоги [3000 монет]", callback_data="zel_bron")],
    ]
kb20 = InlineKeyboardMarkup(inline_keyboard=buttons20)
buttons21 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="koz_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb21 = InlineKeyboardMarkup(inline_keyboard=buttons21)
buttons22 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="zel_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb22 = InlineKeyboardMarkup(inline_keyboard=buttons22)
buttons23= [
    [InlineKeyboardButton(text="Стальнные штаны  [4000 монет]", callback_data="stal_bron")],
    [InlineKeyboardButton(text="Стальнная кольчуга  [4000 монет]", callback_data="stal_bron")],
    [InlineKeyboardButton(text="Стальнные сапоги [4000 монет]", callback_data="stal_bron")],
    ]
kb23 = InlineKeyboardMarkup(inline_keyboard=buttons23)
buttons24 = [
    [InlineKeyboardButton(text="Штаны из  дракогьей чещуи  [5000 монет]", callback_data="drag_bron")],
    [InlineKeyboardButton(text="Кольчуга из  дракогьей чещуи  [5000 монет]", callback_data="drag_bron")],
    [InlineKeyboardButton(text="Сапоги из  дракогьей чещуи [5000 монет]", callback_data="drag_bron")],
    ]
kb24 = InlineKeyboardMarkup(inline_keyboard=buttons24)
buttons25 = [
    [InlineKeyboardButton(text="Карбонновые штаны  [10000 монет]", callback_data="carb_bron")],
    [InlineKeyboardButton(text="Карбонновая кольчуга  [10000 монет]", callback_data="carb_bron")],
    [InlineKeyboardButton(text="Карбонновые сапоги [10000 монет]", callback_data="carb_bron")],
    ]
kb25 = InlineKeyboardMarkup(inline_keyboard=buttons25)
buttons26 = [
    [InlineKeyboardButton(text="Мифриловые штаны  [1000 ивент монет]", callback_data="mif_bron")],
    [InlineKeyboardButton(text="Мифриловые кольчуга  [1000 ивент монет]", callback_data="mif_bron")],
    [InlineKeyboardButton(text="Мифриловые сапоги [1000 ивент монет монет]", callback_data="mif_bron")],
    ]
kb26 = InlineKeyboardMarkup(inline_keyboard=buttons26)
buttons27 = [
    [InlineKeyboardButton(text="Обсидианновые штаны  [2000 ивент монет]", callback_data="obs_bron")],
    [InlineKeyboardButton(text="Обсидианновая кольчуга  [2000 ивент монет]", callback_data="obs_bron")],
    [InlineKeyboardButton(text="Обсидианновые сапоги [2000 ивент монет]", callback_data="obs_bron")],
    ]
kb27 = InlineKeyboardMarkup(inline_keyboard=buttons27)
buttons28 = [
    [InlineKeyboardButton(text="Адоманнтовые штаны  [3000 ивент монет]", callback_data="ado_bron")],
    [InlineKeyboardButton(text="Адоманнтовая кольчуга  [3000 ивент монет]", callback_data="ado_bron")],
    [InlineKeyboardButton(text="Адоманнтовые сапоги [3000 ивент монет]", callback_data="ado_bron")],
    ]
kb28 = InlineKeyboardMarkup(inline_keyboard=buttons28)
buttons29 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="stal_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb29 = InlineKeyboardMarkup(inline_keyboard=buttons29)
buttons30 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="drag_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb30 = InlineKeyboardMarkup(inline_keyboard=buttons30)
buttons31 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="carb_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb31 = InlineKeyboardMarkup(inline_keyboard=buttons31)
buttons32 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="mif_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb32 = InlineKeyboardMarkup(inline_keyboard=buttons32)
buttons33 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="obs_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb33 = InlineKeyboardMarkup(inline_keyboard=buttons33)
buttons34 = [
    [InlineKeyboardButton(text="Подтвердить", callback_data="ado_brona_yes")],
    [InlineKeyboardButton(text="Отмена", callback_data="no")]
    ]
kb34 = InlineKeyboardMarkup(inline_keyboard=buttons34)
#когда пользователь написал сообщениеs
@dp.message()
async def start(message):
    id = message.from_user.id
    if not db.user_exist(id):  # если пользователя нет в бд
        db.add_user(id)  # добавляем
    status = db.get_field("users", id, "status")  # получаем статус пользователя
    if status == 0:
        await message.answer(
            "Привет👋 я главный лесник этого леса. Лес восстал! Магия древних деревьев пробудила животных, и теперь они яростно😡 защищают свои земли🏞. Тебе предстоит пробиваться⚔️ через суровый лес, сражаясь с огромными волками, взбешенными медведями. Используй оружие чтобы выжить и добраться до сердца леса, и заполучить спрятанные сокровища💰."
            "Ты готов оставить информацию о себе?",reply_markup=kb)
    status = db.get_field("users", id, "status")
    if status >=2:
         await message.answer("Главное меню:", reply_markup=kb7)
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
    status = db.get_field("users", id, "status")  # получаем статус пользователя
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
        db.update_field("users", id, "status", 2)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Мишень стоит тебе надо попасть по ней! Куда будем стрелять?", reply_markup=kb6)
    if call.data in ["left", "center", "right"] and status == 2:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            power = db.get_field("users", id, "power")
            power -= 1
            db.update_field("users", id, "lovkost", power)
            await call.message.answer(f"Ты попал по мишени!+1 сила! Твоя сила: {power}", reply_markup=kb9)
            return
        else:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "pvpanimals":
        db.update_field("users", id, "status", 2)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! животное стоит тебе надо попасть по нему! Куда будем стрелять?", reply_markup=kb9)
        return
    if call.data in ["pvpaleft", "pvpacenter", "pvparight"] and status == 2:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            power = db.get_field("users", id, "power")
            power -= 1
            db.update_field("users", id, "lovkost", power)
            await call.message.answer(f"Ты попал по животному!+1 сила! Твоя сила: {power}", reply_markup=kb9)
            return
        else:
            await call.message.answer("Ты промазал!", reply_markup=kb9)
            return
    if call.data == "yklonpredmet":
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Противник кинул в тебя булыжник! Куда будешь уклоняться",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status==3:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            lovkost = db.get_field("users", id, "lovkost")
            lovkost -= 1
            db.update_field("users", id, "lovkost", lovkost)
            await call.message.answer(f"Ты не уклонился от булыжника!-1 ловкость! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
        else:
            lovkost = db.get_field("users", id, "lovkost")
            lovkost += 1
            db.update_field("users", id, "lovkost", lovkost)
            await call.message.answer(f"Ты уклонился от булыжника!+1 ловкость! Твоя ловкость: {lovkost}", reply_markup=kb9)
            return
    if call.data == "bgoblin":
        db.update_field("users", id, "status", 5)
        db.update_field("users", id, "hp_goblin", 50)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==5:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 6)
            d = 10 + random.randint(5,15)
            hp_goblin = db.get_field("users", id, "hp_goblin")
            yron = hp_goblin - d
            await call.message.answer(f"Вы снесли гоблину {d}хп")
            db.update_field("users", id, "hp_goblin", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки гоблина! Куда будем уклонятся?",reply_markup=kb6)
            db.update_field("users", id, "status", 6)
        hp_goblin = db.get_field("users", id, "hp_goblin")
        if hp_goblin <= 0:
            await call.message.answer("Гоблин был повержен! Ты получаешь +20 к силе, +30 к ловкости, +5 к удаче, +1000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=20
            lovkost +=30
            yudacha +=5
            money +=1000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 6)
            await call.message.answer("Теперь твоя задача уклонится от атаки гоблина! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 6:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 10 + random.randint(-5, 5)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки гоблина! -{d}")
            brona = db.get_field("users", id, "brona")
            if d > brona:
                ostatok = brona - d
                yron = hp - ostatok
                db.update_field("users", id, "hp", yron)
                db.update_field("users", id, "brona", 0)
            if d <= brona:
                yron = brona - d
                db.update_field("users", id, "brona", yron)
            if brona <= 0:
                yron = hp - d
                db.update_field("users", id, "hp", yron)
            db.update_field("users", id, "status", 5)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки гоблина!")
            db.update_field("users", id, "status", 5)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return

    if call.data == "btemrizar":
        hp = db.get_field("users", id, "hp")
        if hp < 100:
            await call.message.answer("Вам может не хватить хп для битвы нужно выличиться в магазине", reply_markup=kb12)
            return
        power = db.get_field("users", id, "power")
        if power < 50:
            await call.message.answer("Твоя сила мала минимально 50 силы для запуска!", reply_markup=kb9)
            return
        lovkost = db.get_field("users", id, "lovkost")
        if lovkost < 50:
            await call.message.answer("Твоя ловкость мала минимально 50 ловкости для запуска!", reply_markup=kb9)
        db.update_field("users", id, "status", 7)
        db.update_field("users", id, "hp_temric", 75)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==7:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 8)
            d = 10 + random.randint(10,15)
            hp_temric = db.get_field("users", id, "hp_temric")
            yron = hp_temric - d
            await call.message.answer(f"Вы снесли рыцарю {d}хп")
            db.update_field("users", id, "hp_temric", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        hp_temric = db.get_field("users", id, "hp_temric")
        if hp_temric <= 0:
            await call.message.answer("Рыцарь был повержен! Ты получаешь +50 к силе, +50 к ловкости, +15 к удаче, +3000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=50
            lovkost +=50
            yudacha +=15
            money +=3000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 8)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 8:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 10 + random.randint(-2, 5)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки рыцаря! -{d}")
            brona = db.get_field("users", id, "brona")
            if d > brona:
                ostatok = brona - d
                yron = hp - ostatok
                db.update_field("users", id, "hp", yron)
                db.update_field("users", id, "brona", 0)
            if d <= brona:
                yron = brona - d
                db.update_field("users", id, "brona", yron)
            if brona <= 0:
                yron = hp - d
                db.update_field("users", id, "hp", yron)
            db.update_field("users", id, "status", 7)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки рыцаря!")
            db.update_field("users", id, "status", 7)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return




    if call.data == "bsvetrizar":
        hp = db.get_field("users", id, "hp")
        if hp < 100:
            await call.message.answer("Вам может не хватить хп для битвы нужно выличиться в магазине", reply_markup=kb12)
            return
        power = db.get_field("users", id, "power")
        if power < 80:
            await call.message.answer("Твоя сила мала минимально 80 силы для запуска!", reply_markup=kb9)
            return
        lovkost = db.get_field("users", id, "lovkost")
        if lovkost < 80:
            await call.message.answer("Твоя ловкость мала минимально 80 ловкости для запуска!", reply_markup=kb9)
        db.update_field("users", id, "status", 9)
        db.update_field("users", id, "hp_swetric", 75)
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==9:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 10)
            d = 10 + random.randint(10,20)
            hp_swetric = db.get_field("users", id, "hp_swetric")
            yron = hp_swetric - d
            await call.message.answer(f"Вы снесли рыцарю {d}хп")
            db.update_field("users", id, "hp_swetric", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        hp_swetric = db.get_field("users", id, "hp_swetric")
        if hp_swetric <= 0:
            await call.message.answer("Рыцарь был повержен! Ты получаешь +75 к силе, +75 к ловкости, +25 к удаче, +5000 к балансу!", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            power +=75
            lovkost +=75
            yudacha +=25
            money +=5000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 10)
            await call.message.answer("Теперь твоя задача уклонится от атаки рыцаря! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 10:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 10 + random.randint(-2, 5)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки рыцаря! -{d}")
            brona = db.get_field("users", id, "brona")
            if d > brona:
                ostatok = brona - d
                yron = hp - ostatok
                db.update_field("users", id, "hp", yron)
                db.update_field("users", id, "brona", 0)
            if d <= brona:
                yron = brona - d
                db.update_field("users", id, "brona", yron)
            if brona <= 0:
                yron = hp - d
                db.update_field("users", id, "hp", yron)
            db.update_field("users", id, "status", 9)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки рыцаря!")
            db.update_field("users", id, "status", 9)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return
    if call.data == "ivent_boss":
        hp_do = db.get_field("users", id, "hp")
        db.update_field("users", id, "hp_do", hp_do)
        db.update_field("users", id, "hp", 1000)
        db.update_field("users", id, "hp_boss_ivent", 1000)
        db.update_field("users", id, "status", 11)
        await call.message.answer("Отлично! В этом режиме у тебя 1000 хп, а у Босса 1000 в целом как и у тебя. Твой урон варируется от 50 до 300, а его атака варируется от 75 до 150! При победе данного босса ты получишь, ивент монеты и многое другое!")
        random_number = random.randint(1, 3)
        db.update_field("users", id, "random", random_number)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
    if call.data in ["left","center","right"] and status==11:
        r = db.get_field("users", id, "random")
        if r == random.randint(1,3):
            await call.message.answer("Ты попал!")
            db.update_field("users", id, "status", 12)
            d = 50 + random.randint(0,150)
            hp_boss = db.get_field("users", id, "hp_boss_ivent")
            yron = hp_boss - d
            await call.message.answer(f"Вы снесли Боссу {d}хп")
            db.update_field("users", id, "hp_boss_ivent", yron)
            await call.message.answer("Теперь твоя задача уклонится от атаки Босса! Куда будем уклонятся?",reply_markup=kb6)
        hp_boss_ivent = db.get_field("users", id, "hp_boss_ivent")
        if hp_boss_ivent <= 0:
            await call.message.answer(r"Босс был повержен! Ты получаешь +100 к силе, +100 к ловкости, +20 к удаче, +1000 к балансу, +1000 ивент монет!\n ||Твои хп были возращены в прежний вид(как было до битвы)!||", reply_markup=kb9)
            power = db.get_field("users", id, "power")
            lovkost = db.get_field("users", id, "lovkost")
            yudacha = db.get_field("users", id, "yudacha")
            money = db.get_field("users", id, "money")
            ivent_money = db.get_field("users", id, "ivent_money")
            hp_do = db.get_field("users", id, "hp_do")
            ivent_money +=1000
            power +=100
            lovkost +=100
            yudacha +=20
            money +=1000
            db.update_field("users", id, "power", power)
            db.update_field("users", id, "lovkost", lovkost)
            db.update_field("users", id, "yudacha", yudacha)
            db.update_field("users", id, "money", money)
            db.update_field("users", id, "ivent_money", ivent_money)
            db.update_field("users", id, "hp", hp_do)
        else:
            await call.message.answer("Ты промазал!")
            db.update_field("users", id, "status", 12)
            await call.message.answer("Теперь твоя задача уклонится от атаки Босса! Куда будем уклонятся?",reply_markup=kb6)
        return
    if call.data in ["left","center","right"] and status == 12:
        r = db.get_field("users", id, "random")
        if r == random.randint(1, 3):
            d = 75 + random.randint(0, 75)
            hp = db.get_field("users", id, "hp")
            await call.message.answer(f"Вы не уклонились от атаки Босса! -{d}")
            brona = db.get_field("users", id, "brona")
            if d > brona:
                ostatok = brona - d
                yron = hp - ostatok
                db.update_field("users", id, "hp", yron)
                db.update_field("users", id, "brona", 0)
            if d <= brona:
                yron = brona - d
                db.update_field("users", id, "brona", yron)
            if brona <= 0:
                yron = hp -  d
                db.update_field("users", id, "hp", yron)
            db.update_field("users", id, "status", 11)
        await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        hp = db.get_field("users", id, "hp")
        if hp <= 0:
            await call.message.answer("Вы мертв! Вы можете возродится, но при возрождении все ваши ресурсы и навыки будут потеряны, или можете купить зелье излечения в магазине!", reply_markup=kb11)
        else:
            await call.message.answer("Вы уклонились от атаки Босса!")
            db.update_field("users", id, "status", 11)
            await call.message.answer("Отлично! Твоя задача кидать в противника! Куда будем кидать?", reply_markup=kb6)
        return




    if call.data == "infome":
        name = db.get_field("users", id, "name")
        hp = db.get_field("users", id, "hp")
        power = db.get_field("users", id, "power")
        lovkost = db.get_field("users", id, "lovkost")
        yudacha = db.get_field("users", id, "yudacha")
        brona = db.get_field("users", id, "brona")
        money = db.get_field("users", id, "money")
        ivent_money = db.get_field("users", id, "ivent_money")
        await call.message.answer(f"Вот информация о тебе: \nИмя: {name}\nЗдоровье❤️: {hp}\nСила✊: {power}\n Ловкость🏃: {lovkost}\nУдача🤞: {yudacha}\nБроня🛡: {brona}\nБаланс💰: {money}\nИвент монеты: {ivent_money}")
    if call.data == "proka":
        await call.message.answer("Давай приступим", reply_markup=kb2)
    if call.data == "glavmenu":
        await call.message.answer("Главное меню", reply_markup=kb7)
    if call.data =="vozr":
       db.del_user(id)
       await call.message.answer(
           "Привет👋 я главный лесник этого леса. Лес восстал! Магия древних деревьев пробудила животных, и теперь они яростно😡 защищают свои земли🏞. Тебе предстоит пробиваться⚔️ через суровый лес, сражаясь с огромными волками, взбешенными медведями. Используй оружие чтобы выжить и добраться до сердца леса, и заполучить спрятанные сокровища💰."
           "Ты готов оставить информацию о себе???", reply_markup=kb)
    if call.data == "magaz":
        await call.message.answer("Вот товары имеющиеся в магазине:", reply_markup=kb13)
    if call.data == "apt":
        await call.message.answer(f"Аптечка прибовляет 10хп \n Подтвердить покупку???", reply_markup=kb14)
    if call.data == "apt_yes":
        await call.message.answer("Успешно", reply_markup=kb12)
        db.update_field("users", id, "hp", (db.get_field("users", id, "hp"))+10)
        db.update_field("users", id, "money", (db.get_field("users", id, "money")-100))
    if call.data == "bron":
        await call.message.answer("Есть такие виды брони:", reply_markup=kb17)
    if call.data == "der_brona":
        await call.message.answer("Деревянная броня:", reply_markup=kb18)
    if call.data == "der_bron":
        await call.message.answer("Деревянная броня дает +100 ку броне \n Подтвердить покупку???", reply_markup=kb15)
    if call.data == "der_brona_yes":
        der_bron = db.get_field("users", id, "der_bron")
        if der_bron != 3:
            money = db.get_field("users", id, "money")
            if money >= 1000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+100)
                db.update_field("users", id, "money", (db.get_field("users", id, "money")-1000))
                db.update_field("users", id, "der_bron", (db.get_field("users", id, "der_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Деревянной брони!")
    if call.data == "koz_brona":
        await call.message.answer("Кожанная броня:", reply_markup=kb19)
    if call.data == "koz_bron":
        await call.message.answer("Кожанная броня дает +250 к броне \n Подтвердить покупку???", reply_markup=kb21)
    if call.data == "koz_brona_yes":
        koz_bron = db.get_field("users", id, "koz_bron")
        if koz_bron != 3:
            money = db.get_field("users", id, "money")
            if money >= 2000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+250)
                db.update_field("users", id, "money", (db.get_field("users", id, "money")-2000))
                db.update_field("users", id, "koz_bron", (db.get_field("users", id, "koz_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Кожанной брони!")
    if call.data == "zel_brona":
        await call.message.answer("Железнная броня:", reply_markup=kb20)
    if call.data == "zel_bron":
        await call.message.answer("Железнная броня дает +500 к броне \n Подтвердить покупку???", reply_markup=kb22)
    if call.data == "zel_brona_yes":
        zel_bron = db.get_field("users", id, "zel_bron")
        if zel_bron != 3:
            money = db.get_field("users", id, "money")
            if money >= 3000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+500)
                db.update_field("users", id, "money", (db.get_field("users", id, "money")-3000))
                db.update_field("users", id, "zel_bron", (db.get_field("users", id, "zel_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Железнной брони!")
    if call.data == "stal_brona":
        await call.message.answer("Стальнная броня:", reply_markup=kb23)
    if call.data == "stal_bron":
        await call.message.answer("Стальнная броня дает +1000 к броне \n Подтвердить покупку???", reply_markup=kb29)
    if call.data == "stal_brona_yes":
        stal_bron = db.get_field("users", id, "stal_bron")
        if stal_bron != 3:
            money = db.get_field("users", id, "money")
            if money >= 4000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+1000)
                db.update_field("users", id, "money", (db.get_field("users", id, "money")-4000))
                db.update_field("users", id, "stal_bron", (db.get_field("users", id, "stal_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Стальнной брони!")
    if call.data == "drag_brona":
        await call.message.answer("Драконья броня:", reply_markup=kb24)
    if call.data == "drag_bron":
        await call.message.answer("Стальнная броня дает +1200 к броне \n Подтвердить покупку???", reply_markup=kb30)
    if call.data == "drag_brona_yes":
        drag_bron = db.get_field("users", id, "drag_bron")
        if drag_bron != 3:
            money = db.get_field("users", id, "money")
            if money >= 5000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+1200)
                db.update_field("users", id, "money", (db.get_field("users", id, "money")-5000))
                db.update_field("users", id, "drag_bron", (db.get_field("users", id, "drag_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Драконьей брони!")
    if call.data == "carb_brona":
        await call.message.answer("Карбонновая броня:", reply_markup=kb25)
    if call.data == "carb_bron":
        await call.message.answer("Карбонноваянная броня дает +1500 к броне \n Подтвердить покупку???", reply_markup=kb31)
    if call.data == "carb_brona_yes":
        carb_bron = db.get_field("users", id, "carb_bron")
        if carb_bron != 3:
            money = db.get_field("users", id, "money")
            if money >= 6000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+1500)
                db.update_field("users", id, "money", (db.get_field("users", id, "money")-6000))
                db.update_field("users", id, "carb_bron", (db.get_field("users", id, "carb_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Карбонновой брони!")
    if call.data == "mif_brona":
        await call.message.answer("Мифриловая броня:", reply_markup=kb26)
    if call.data == "mif_bron":
        await call.message.answer("Мифриловая броня дает +3000 к броне \n Подтвердить покупку???", reply_markup=kb32)
    if call.data == "mif_brona_yes":
        mif_bron = db.get_field("users", id, "mif_bron")
        if mif_bron != 3:
            ivent_money = db.get_field("users", id, "ivent_money")
            if ivent_money >= 1000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+3000)
                db.update_field("users", id, "ivent_money", (db.get_field("users", id, "ivent_money")-1000))
                db.update_field("users", id, "mif_bron", (db.get_field("users", id, "mif_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно ивент монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Мифриловой брони!")
    if call.data == "obs_brona":
        await call.message.answer("Обсидианновая броня:", reply_markup=kb27)
    if call.data == "obs_bron":
        await call.message.answer("Обсидианновая броня дает +4000 к броне \n Подтвердить покупку???", reply_markup=kb33)
    if call.data == "obs_brona_yes":
        obs_bron = db.get_field("users", id, "obs_bron")
        if obs_bron != 3:
            ivent_money = db.get_field("users", id, "ivent_money")
            if ivent_money >= 2000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+4000)
                db.update_field("users", id, "ivent_money", (db.get_field("users", id, "ivent_money")-2000))
                db.update_field("users", id, "obs_bron", (db.get_field("users", id, "obs_bron") + 1))
            else:
                await call.answer("Ошибка! Не достаточно ивент монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Обсидианновой брони!")
    if call.data == "ado_brona":
        await call.message.answer("Адомантовая броня:", reply_markup=kb28)
    if call.data == "ado_bron":
        await call.message.answer("Адомантовая броня дает +5000 к броне \n Подтвердить покупку???", reply_markup=kb34)
    if call.data == "ado_brona_yes":
        ado_bron = db.get_field("users", id, "ado_bron")
        if ado_bron !=3:
            ivent_money = db.get_field("users", id, "ivent_money")
            if ivent_money >= 3000:
                await call.message.answer("Успешно", reply_markup=kb12)
                db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+5000)
                db.update_field("users", id, "ivent_money", (db.get_field("users", id, "ivent_money")-3000))
                db.update_field("users", id, "ado_bron", (db.get_field("users", id, "ado_bron")+1))
            else:
                await call.answer("Ошибка! Не достаточно ивент монет!")
        else:
            await call.answer("Ошибка! У вас уже есть 3 Адоманнтовой брони!")





    #if call.data == "bron_yes":
        #money = db.get_field("users", id, "money")
        #if money <= 100:
            #await call.message.answer("Успешно", reply_markup=kb12)
            #db.update_field("users", id, "brona", (db.get_field("users", id, "brona"))+10)
            #db.update_field("users", id, "money", (db.get_field("users", id, "money")-100))
        #else:
            #await call.message("Ошибка! Не достаточно монет!")
    if call.data == "no":
        await call.message.answer("Успешно отклонено!", reply_markup=kb9)







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
