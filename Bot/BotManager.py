from email import message
from pydoc import cli
import telebot
import BotSettings


def Test(msgs):
    for m in msgs:
        chatid = m.chat.id
        if m.content_type == "text":
            client.send_message(chat_id=chatid,text=m.text)
        
client = telebot.TeleBot(BotSettings.token)

client.set_update_listener(Test)

@client.message_handler(content_types=['text'])
def TestFunc(message):
    msg = message.text 
    if msg.lower() == "ping": 
        client.send_message(message.chat.id,"pong")
        client.send_location(message.chat.id,latitude=44,longitude=22)



client.polling(non_stop=True,interval=0)