# в текущем каталоге должен быть размещен файл api.py, содержащий строку
# token = 'ваш_токен'.
import api
import telebot
import turtle

MAX_ARG = 50

helloMsg = f'''Привет. Это бот-черепашка. Используйте эти команды для рисования:
опустить хвост - оставлять след при перемещении
поднять хвост - не оставлять след
вперед х - переместиться вперед на х шагов
назад х - переместиться назад на х шагов
влево х - повернуть влево на х градусов
вправо х - повернуть вправо на х градусов.
Имейте в виду, что перемещение за одну команду ограничено {MAX_ARG} шагами'''

bot = telebot.TeleBot(api.token, threaded=False)
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, helloMsg)

@bot.message_handler(content_types=['text'])
def anyMessage(message):
    command = message.text.lower().strip()
    print(f'{message.from_user.first_name}: {command}')
    if command == 'reset' and message.from_user.id == 379884080:
        turtle.reset()
    elif command == 'поднять хвост':
        turtle.penup()
    elif command == 'опустить хвост':
        turtle.pendown()
    else:
        command = command.split()
        if len(command) != 2:
            bot.send_message(message.chat.id, 'Неизвестная команда')
            return
        cmd, arg = command[0].strip(), int(command[1])
        if cmd == 'вперед':
            turtle.forward(min(arg, MAX_ARG))
        elif cmd == 'назад':
            turtle.back(min(arg, MAX_ARG))
        elif cmd == 'влево':
            turtle.left(arg)
        elif cmd == 'вправо':
            turtle.right(arg)
    
bot.polling()

# turtle.mainloop()