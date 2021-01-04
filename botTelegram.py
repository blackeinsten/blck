import sys,signal,time
import telepot
from datetime import datetime


def handle(msg):

    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        text = "Selamat datang di Telegram Bot.\n"
        text += "Daftar perintah\n"
        text += "/start\t=> Start bot.\n"
        text += "/myid\t=> Melihat id chat.\n"
        text += "/sendPhoto\t=> Kirim foto dari server."
        bot.sendMessage(chat_id, text)

    elif command == '/myid':    
        text = "Nama\t: "+ msg['from']['first_name'] + " " + msg['from']['last_name'] + "\n"
        text += "Username\t: "+ msg['from']['username'] +"\n"
        text += "ChatID\t:"+ str(msg['chat']['id']) +"\n"
        bot.sendMessage(chat_id, text)

    elif command == "/sendPhoto":
        bot.sendPhoto(chat_id, "https://api.time.com/wp-content/uploads/2015/04/512137691.jpg?w=800&quality=85") #Sumber foto dari server

    else :
        text = "Maaf perintah tersebut tidak ada"
        bot.sendMessage(chat_id,text)

def signal_handling(signum,frame):
    sys.exit(0) #error handling saat menekan keyboard

signal.signal(signal.SIGINT, signal_handling)

print("["+ datetime.today().strftime("%d %B %Y %H:%M:%S") +"]") #Keterangan tanggal dan waktu
print('Start listening ...')

bot = telepot.Bot('883089148:AAG8UAMuiV9thmdCBDtVMCKwV54qC8nZWuk') #Bot Token dari BotFather
bot.message_loop(handle)

#Buat program selalu running
while 1:
    time.sleep(10) 