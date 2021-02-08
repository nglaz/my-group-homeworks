import telebot


import requests
import string
import random


bot = telebot.TeleBot('1699048434:AAGgyh-TS-QLOYF56cH-IBsCf4-Lf2bM0Go')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Create mail', 'Help')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Create mail', 'Restart bot')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Check mail')

url = 'https://api.mail.tm/'

response_domain = requests.get(f'{url}domains').json()
data = {
        'address': f'{"".join(random.sample(string.ascii_lowercase + string.digits, 15))}'
                   f'@{response_domain["hydra:member"][0]["domain"]}',
        'password': f'{"".join(random.sample(string.ascii_letters + string.digits, 10))}'
}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to the FakeMailBot. Here you can create a temporary mail for all of '
                                      'your needs.', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'How it works - . Also you can restart the bot by pressing the button below.',
                     reply_markup=keyboard2)


@bot.message_handler(content_types=['text'])
def response(message):
    if message.text.lower() == 'help':
        help_message(message)
    elif message.text.lower() == 'create mail':
        requests.post(f'{url}accounts', json=data).json()
        bot.send_message(message.chat.id, text=data["address"])
        bot.send_message(message.chat.id, f'Here is your mail address. '
                                          f'To check for new messages press the button below.', reply_markup=keyboard3)
    elif message.text.lower() == 'check mail':
        response_token = requests.post(f'{url}authentication_token', json=data).json()
        response_msg = requests.get('https://api.mail.tm/messages',
                                    headers={'Authorization': f'Bearer {response_token["token"]}'}).json()
        if len(response_msg['hydra:member']) == 0:
            bot.send_message(message.chat.id, 'No mail yet.')
        else:
            response_msg_text = requests.get(f'https://api.mail.tm/messages/{response_msg["hydra:member"][0]["id"]}',
                                             headers={'Authorization': f'Bearer {response_token["token"]}'}).json()
            bot.send_message(
                message.chat.id,
                f'From: {response_msg_text["from"]["name"]}'
                f' ({response_msg_text["from"]["address"]})\n'
                f'Subject: {response_msg_text["subject"]}\n'
                f'  {response_msg_text["text"]}')
            patch = requests.patch(f'https://api.mail.tm/messages/{response_msg["hydra:member"][0]["id"]}',
                                   headers={'Authorization': f'Bearer {response_token["token"]}'}).json()
            print(patch)
    elif message.text.lower() == 'restart bot':
        start_message(message)


bot.polling(none_stop=True)
