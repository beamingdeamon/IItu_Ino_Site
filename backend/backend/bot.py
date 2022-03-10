import telebot
import requests
import json
from telebot import types
API_TOKEN = '5190315685:AAGFDh46fvCN9vWt2eJUQ6dRMNj_KgrTLDU'
bot = telebot.TeleBot(API_TOKEN)
name = "admin"
password = "admin"
partner_name = ""

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.from_user.id, "Comands List:")
    bot.send_message(message.from_user.id, "/createpartner")
    bot.send_message(message.from_user.id, "/getpartners")
    bot.send_message(message.from_user.id, "/deletepartner")
    bot.send_message(message.from_user.id, "/updatepartner")

@bot.message_handler(commands=['getpartners'])
def firstGetMessage(message):
    response = requests.get('http://localhost:8000/api/getpartners/')
    data = response.text
    if len(data) > 4096:
        first = response[0:len(data)/2]
        last = response[len(data)/2:]
        bot.send_message(message.chat.id, first)
        bot.send_message(message.chat.id, last)
    else:
        bot.send_message(message.chat.id, data)

@bot.message_handler(commands=['deletepartner'])
def firstDeleteMessage(message):
    bot.send_message(message.chat.id, "Please Send Id of Partner")
    bot.register_next_step_handler(message, deletePartner)
def deletePartner(message):
    response = requests.delete('http://localhost:8000/api/deletepartner/'+ message.text+'/')
    bot.send_message(message.chat.id, response.status_code)
    if(response.status_code == 200):
        bot.send_message(message.chat.id, "Delete was succesfully")
    else:
        bot.send_message(message.chat.id, "Delete failed!!!!")


@bot.message_handler(commands=['createpartner'])
def firstCreateMessage(message):
    bot.send_message(message.from_user.id, "Please enter partner Name")
    bot.register_next_step_handler(message, getPartnerName)
def getPartnerName(message):
    partner_name = message.text
    bot.send_message(message.from_user.id, "Please send photo")

@bot.message_handler(content_types=['photo'])
def on_photo(message):
    img_source = lower(partner_name)
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
    with open('../../front/public/assets/'+img_source+'.png','wb') as f:
        f.write(file.content)
    response = requests.post('http://localhost:8000/api/createpartner/', json={"imgSource": img_source, "text": partner_name})
    bot.send_message(message.from_user.id, response.status_code)
    bot.send_message(message.from_user.id, "Partner was created succesfully")

    

    

bot.polling(none_stop=True, interval=0)