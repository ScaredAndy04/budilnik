import telebot
import
bot=telebot.TeleBot('6501007470:AAGD04o-7-ak0R0DChiLYq0XyhTDhaToUkc')
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет,чтобы установть время клаций /set_alarm HH:MM")
@bot.message_handler(commands=["set_alarm"])
def set_alarm(message):
    try:
        alarm_time=message.text.split()[1]
        if ":" not in alarm_time:
            raise ValueError
        hour,minute=map(int,alarm_time.split(":"))
        if hour<0 or hour>23 or minute<0 or minute>59:
            raise ValueError
        current_time=time.localtime()
        if hour<current_time.tm_hour or (hour==current_time.tm_hour and minute <= current_time.tm_min):
            alarm_time=f'{hour:02d}:{minute:02d}'
            tomorrow =time.localtime(time.time()+24*60*60)
            alarm_date=f'{current_time.tm_year}-{tomorrow.tm_mon:02d}-{tomorrow.tm_mday:02d}'
        else:
            alarm_date=f"{current_time.tm_year}-{current_time.tm_mon:02d}"
        alarm_timestamp =time.mktime(time.strptime(alarm_date+alarm_time, "%Y-%m-%d %H:%M"))
        delay=alarm_timestamp-time.time()
        bot.reply_to(message,f'БУДИЛЬНИК УСТАНОВЛЕН НА {alarm_time}')
        time.sleep(delay)
        bot.send_message(message.chat.id,"Вставай!!!")
    except(IndexError, ValueError):
        bot.reply_to(message, 'отстань')
bot.polling()







