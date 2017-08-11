import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

#from pprint import pprint
import time
import datetime
import urllib3


# This part is for using a free PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts


TOKEN="YOUR TOKEN HERE"

def on_chat_message(msg):
  #pprint(msg) #display del messaggio che manda l'utente
	print '\n\nmsg:', msg
	content_type, chat_type, chat_id = telepot.glance(msg)
	print '\n\ncontent_type, chat_type, chat_id:', content_type, chat_type, chat_id

	keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='On', callback_data='on'),InlineKeyboardButton(text='Off', callback_data='off'),InlineKeyboardButton(text='Time', callback_data='time')],
                 ])
	bot.sendMessage(chat_id, 'You can use inline keyboard.\nOn: to turn on the pump;\nOff: to turn off the pump;\nTime: to view current time.', reply_markup=keyboard)


def on_callback_query(msg):
	query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('\n\nCallback Query:', query_id, chat_id, query_data)
	if query_data=='on':
		bot.sendMessage(chat_id, 'Turn on the pump')
	elif query_data=='off':
		bot.sendMessage(chat_id, 'Turn off the pump')
	elif query_data=='time':
		ts = time.time()
		bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
	time.sleep(10)
