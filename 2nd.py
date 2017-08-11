import telepot
from telepot.loop import MessageLoop

#from pprint import pprint
import time
import urllib3

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts


TOKEN="YOUR TOKEN HERE"

def on_chat_message(msg):
	print '\n\nmsg:', msg
	content_type, chat_type, chat_id = telepot.glance(msg)
	print '\n\ncontent_type, chat_type, chat_id:', content_type, chat_type, chat_id

	command = msg['text']
	if command =='/on PASSWORD':
	    bot.sendMessage(chat_id, 'Turn ON the pump')
	elif command =='/off PASSWORD':
	    bot.sendMessage(chat_id, 'Turn OFF the pump')
	else:
	    bot.sendMessage(chat_id, 'Wrong command or password')


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message}).run_as_thread()
print('Listening ...')

while 1:
	time.sleep(10)
