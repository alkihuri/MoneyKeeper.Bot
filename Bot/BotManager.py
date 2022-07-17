from email import message
from pydoc import cli
import telebot
import BotSettings
import pyautogui
import os
from datetime import datetime


spends = []

def UpdateDB(chat_id,cat,amount): 
    path = os.getcwd()
    dbPath = path+"/"+str(chat_id)+"_db.csv" 

    try:
        data = open(dbPath,"r+") 
    except:
        data = open(dbPath,"w+") 
        
    db = data.readlines()
    
    total = 0
    try:
        for x in db:
            if x.find(cat) > -1:
                try:
                    total += int( x.split(";")[2])
                except:
                    total += 0
    
        total += int(amount)
        total =str(total)

    except:
        total = amount
    
    data.close()
    newSpend = BotSettings.Spend()
    newSpend.user = chat_id
    newSpend.category = cat
    newSpend.amount = amount  
    spends.clear()
    info = "\n" + str( chat_id) + ";" +  str(newSpend.category) + ";" + str(newSpend.amount) + ";" + str(datetime.now())
    data = open(dbPath,"a")
    data.write(info)
    data.close()
    client.send_message(chat_id,"бот записал ваш расход...")  
    client.send_message(chat_id,"вы уже потратили в этой категории..." + total)

def MakeSceenShot():
    myScreenshot = pyautogui.screenshot() 
    return myScreenshot

       
client = telebot.TeleBot(BotSettings.token)
 

@client.message_handler(content_types=['text'])
def TestFunc(message):
    msg = message.text  
    
    try:
        cat = msg.split(" ")[0] 
        amo = msg.split(" ")[1]
        UpdateDB(message.chat.id,cat,amo)  
    except: 
        client.send_message(message.chat.id,"Введите данные в коректном формате [категория деньги] ")  


@client.message_handler(commands=['clear'])
def Clear(message): 
    path = os.getcwd()
    dbPath = path+"/"+str(message.chat.id)+"_db.csv"   
    data = open(dbPath,"w+") 
    data.close()
    client.send_message(message.chat.id,"Данные удалены...")


 
client.polling(non_stop=True,interval=1)