# -*- coding: utf-8 -*-

from pydoc import cli
import telebot
import BotSettings
import pyautogui
import os
from datetime import datetime
import sqlite3



spends = []
client = telebot.TeleBot(BotSettings.token)

def InsertValues(message,cat,amount): 
    chat_id = str(message.chat.id)
    db = BotSettings.InnitDataBase(message)
    cur = db.cursor()
    cur.execute('''INSERT INTO SPENDS VALUES (?, ?, ?,?)''',(chat_id,cat,amount,datetime.now())) 
    db.commit() 
    db.close()
    client.send_message(message.chat.id,"Ваш расход добавлен в таблицу...")  

        

@client.message_handler(commands=['start'])
def StartApp(message): 
    db = BotSettings.InnitDataBase(message)
 

@client.message_handler(commands=['getall'])
def GetAll(message):  
    db = BotSettings.InnitDataBase(message)
    cur = db.cursor()
    data = cur.execute('''SELECT * FROM SPENDS''')    
    client.send_message(message.chat.id,"Список ваших трат:")  
    for line in list(data): 
        print(line)
        data =  str(line[1])+ " - " + str(line[2]) + " время : " + str(line[3])
        client.send_message(message.chat.id,data) 
    if(len(list(data)) == 0): 
     client.send_message(message.chat.id,"пусто.")  

    
    db.close()

@client.message_handler(commands=['clear'])
def GetAll(message):  
    db = BotSettings.InnitDataBase(message)
    cur = db.cursor()
    cur.execute('''DELETE FROM SPENDS''')  
    db.commit()
    client.send_message(message.chat.id,"Данные удалены...")   
    db.close()


@client.message_handler(func=lambda message: True, content_types=['text'])
def EachMsgFunc(message):
    msg = message.text   
    
    if msg.find('/') > -1:
        return
 
    print(msg) 
    try:
        cat = msg.split(" ")[0] 
        amo = msg.split(" ")[1] 
        InsertValues(message,cat,amo)  
    except:
        client.send_message(message.chat.id,"Введите данные в коректном формате [категория деньги] ")  


 
client.polling(non_stop=True,interval=1) 