
import re
import sqlite3 
import telebot

token = "5499026409:AAGV3com_c4nmndYwErEyuJJXpCn-YfK0qQ"
 
class Spend:
    user = ""
    category = ""
    amount = ""


def InnitDataBase(message): 
    dbName = str( message.chat.id)
    con = sqlite3.connect(dbName+'.db')
    сur = con.cursor()
    сur.execute('''CREATE TABLE IF NOT EXISTS SPENDS
                (user text, category text,amount real,time text)''') 
    con.commit()
    return con

def InnitCursor(message):
    db = InnitDataBase(message)
    return db.cursor()
 

