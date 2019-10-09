import time
import telepot
from telepot.loop

TOKEN = '729092994:AAG9qWNZp9rJ2xWU_EyywRno2ZkezvFUTOU'
bot = telepot.Bot(TOKEN)


def handle(msg):
    userProfile = bot.getUserProfilePhotos(user_id=msg['from']['id'], offset=None, limit=2)
    print(msg)
    print()
    if msg['chat']['type'] == 'private':
        
        if msg['text']=='/start':
            bot.sendMessage(chat_id=msg['chat']['id'], text='Hi. Bot deployed by @thelurker. You can add this bot in your groups. It will delete messages from people who dont have either a profile picture or a username and it will give this same reason after deleting. You have to give deletion priveleges at least. Thats it.')
        else:
            bot.sendMessage(chat_id=msg['chat']['id'], text='Click /start for info')

    if msg['chat']['type'] == 'group' or msg['chat']['type']=='supergroup':
        if msg['text']=='/start@deleeteebot' or msg['text']=='/start':
            bot.sendMessage(chat_id=msg['chat']['id'], text='ib',reply_to_message_id=msg['message_id'])
        if userProfile['total_count'] < 1 or 'username' not in msg['from']:
            if msg['from']['first_name'] is None:
                if 'username' in msg['from']:
                    bot.sendMessage(chat_id=msg['chat']['id'], text='Message from @'+msg['from']['username']+' deleted. Reason: No profile picture or username present.',reply_to_message_id=msg['message_id'])
                else:
                    bot.sendMessage(chat_id=msg['chat']['id'], text='Message from a person without name deleted. Reason: No profile picture or username present.',reply_to_message_id=msg['message_id'])
            else:
                bot.sendMessage(chat_id=msg['chat']['id'], text='Message from '+str(msg['from']['first_name'])+' deleted. Reason: No profile picture or username present.',reply_to_message_id=msg['message_id'])

            bot.deleteMessage(telepot.message_identifier(msg))
            print('Message deleted')
            print()
            
            

telepot.loop.MessageLoop(bot, handle).run_as_thread()


# Keep the program running.
while 1:
    time.sleep(10)
