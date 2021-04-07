# в текущем каталоге должен быть размещен файл api.py, содержащий строку
# token = 'ваш_токен'.
import api
import telebot
import turtle

MAX_ARG = 50

bot = telebot.TeleBot(api.token, threaded=False)

@bot.message_handler(content_types=['text'])
def anyMessage(message):
    command = message.text.lower().strip()
    print(command)
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