from time import sleep
import telebot
from telebot import types
import config
import texts

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    services = types.KeyboardButton(texts.services)
    address = types.KeyboardButton(texts.address)
    contacts = types.KeyboardButton(texts.contacts)
    about = types.KeyboardButton(texts.about_me)
    markup.add(services, address, contacts, about)

    text = f'Привет, <b>{message.from_user.first_name}</b> ☺️\nЯ Чат-Бот Жибек 🤖!'
    bot.send_message(message.chat.id, text, parse_mode="html")
    sleep(0.5)
    photo = open("kitten3.jpg", "rb")
    bot.send_photo(message.chat.id, photo)
    sleep(0.5)
    bot.send_message(message.chat.id, "Чем я могу тебе помочь?", reply_markup=markup)
    #sleep(1)


@bot.message_handler()
def echo(message):
    if message.text == texts.back:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        services = types.KeyboardButton(texts.services)
        address = types.KeyboardButton(texts.address)
        contacts = types.KeyboardButton(texts.contacts)
        about = types.KeyboardButton(texts.about_me)
        markup.add(services, address, contacts, about)
        photo = open("kitten3.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        sleep(0.5)
        bot.send_message(message.chat.id, "Чем я могу тебе помочь?", reply_markup=markup)

    elif message.text == texts.services:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        lashes = types.KeyboardButton(texts.lashes)
        brows = types.KeyboardButton(texts.brows)
        markup.add(lashes, brows)
        bot.send_message(message.chat.id, f"Выберите вид услуг:", reply_markup=markup)

    elif message.text == texts.brows:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        bot.send_message(message.chat.id, f"Перманентный макияж бровей.\nВиды услуг:", reply_markup=markup)

    elif message.text == texts.lashes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, "Наращивание ресниц.\nВиды услуг:", reply_markup=markup)

    elif message.text == texts.contacts:
        markup = types.InlineKeyboardMarkup(row_width=1)
        instagram = types.InlineKeyboardButton("Мой Instagram 📸", "https://instagram.com/browbarmsk")
        whatsapp = types.InlineKeyboardButton("Мой WhatsApp", url="https://wa.me/79999788423")
        telegram = types.InlineKeyboardButton("Мой Telegram", url="https://t.me/dokbaeva")
        markup.add(instagram, whatsapp, telegram)
        bot.send_message(message.chat.id, texts.CONTACTS, reply_markup=markup)

    elif message.text == texts.address:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Маршрут 🗺", "https://go.2gis.com/08fgl"))
        bot.send_message(message.chat.id, texts.ADDRESS, reply_markup=markup)

    elif message.text == texts.about_me:
        bot.send_message(message.chat.id, texts.ABOUT_ME)

    elif message.text == texts.extra:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, "Дополнительные услуги:", reply_markup=markup)

    elif message.text == texts.pm_main:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.services)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        bot.send_message(message.chat.id, texts.PM_MAIN, reply_markup=markup)

    elif message.text == texts.pm_corr:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.services)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        bot.send_message(message.chat.id, texts.PM_CORR, reply_markup=markup)

    elif message.text == texts.remove_pm:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.services)
        notice = types.KeyboardButton(texts.notice)
        markup.add(main, corr, rem, notice)
        bot.send_message(message.chat.id, texts.REMOVE_PM, reply_markup=markup)

    elif message.text == texts.notice:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        main = types.KeyboardButton(texts.pm_main)
        corr = types.KeyboardButton(texts.pm_corr)
        rem = types.KeyboardButton(texts.remove_pm)
        notice = types.KeyboardButton(texts.services)
        markup.add(main, corr, rem, notice)
        bot.send_message(message.chat.id, texts.NOTICE, reply_markup=markup)

    elif message.text == texts.classic:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.services)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, texts.CLASSIC, reply_markup=markup)

    elif message.text == texts.one_five:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.services)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, texts.ONE_FIVE, reply_markup=markup)

    elif message.text == texts.two:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.services)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, texts.TWO, reply_markup=markup)

    elif message.text == texts.two_five:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.services)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, texts.TWO_FIVE, reply_markup=markup)

    elif message.text == texts.three:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.services)
        hollywood = types.KeyboardButton(texts.hollywood)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, texts.THREE, reply_markup=markup)

    elif message.text == texts.hollywood:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        classic = types.KeyboardButton(texts.classic)
        one_five = types.KeyboardButton(texts.one_five)
        two = types.KeyboardButton(texts.two)
        two_five = types.KeyboardButton(texts.two_five)
        three = types.KeyboardButton(texts.three)
        hollywood = types.KeyboardButton(texts.services)
        extra = types.KeyboardButton(texts.extra)
        markup.add(classic, one_five, two, two_five, three, hollywood, extra)
        bot.send_message(message.chat.id, texts.HOLLYWOOD, reply_markup=markup)

    elif message.text == texts.curve_l:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.back)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, texts.CURVE_L, reply_markup=markup)

    elif message.text == texts.curve_m:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.back)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, texts.CURVE_M, reply_markup=markup)

    elif message.text == texts.spec_wide:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.back)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, texts.SPEC_WIDE, reply_markup=markup)

    elif message.text == texts.fixer:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.back)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, texts.FIXER, reply_markup=markup)

    elif message.text == texts.kylie_effect:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.back)
        remove = types.KeyboardButton(texts.remove_lashes)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, texts.KYLIE_EFFECT, reply_markup=markup)

    elif message.text == texts.remove_lashes:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        curve_l = types.KeyboardButton(texts.curve_l)
        curve_m = types.KeyboardButton(texts.curve_m)
        spec_wide = types.KeyboardButton(texts.spec_wide)
        fixer = types.KeyboardButton(texts.fixer)
        effect = types.KeyboardButton(texts.kylie_effect)
        remove = types.KeyboardButton(texts.back)
        markup.add(curve_l, curve_m, spec_wide, fixer, effect, remove)
        bot.send_message(message.chat.id, texts.REMOVE_LASHES, reply_markup=markup)

    else:
        markup = types.InlineKeyboardMarkup(row_width=1)
        instagram = types.InlineKeyboardButton("Мой Instagram 📸", "https://instagram.com/browbarmsk")
        whatsapp = types.InlineKeyboardButton("Мой WhatsApp", url="https://wa.me/79999788423")
        telegram = types.InlineKeyboardButton("Мой Telegram", url="https://t.me/dokbaeva")
        markup.add(instagram, whatsapp, telegram)
        bot.send_message(message.chat.id, "Я не знаю что ты имеешь ввиду🥺\nНо ты можешь написать мне ⬇️", reply_markup=markup)


bot.polling(none_stop=True)