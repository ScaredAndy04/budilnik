import telebot
import datetime
import time
bot=telebot.TeleBot('6501007470:AAGD04o-7-ak0R0DChiLYq0XyhTDhaToUkc')
def set_alarm(time):
    now=datetime.datetime.now()
    alarm_time =datetime.datetime.combine(now.date(), time)
    time_diff=(alarm_time-now).total_seconds()
    time.sleep(time_diff)
    bot.send_message('GEEEEET UP AND GO TO THE GYYYM')
@bot.message_handler(commands=['setalarm'])
def set_alarm_command(message):
    try:
        time_str=message.text.split(' ')[1]
        alarm_time=datetime.datetime.strptime(time_str, '%H:%M').time()
        set_alarm(alarm_time)
    except:
        bot.send_message('dmkdmvkd')
bot.polling()
