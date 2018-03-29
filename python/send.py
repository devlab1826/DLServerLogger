import sys
import telegram
chatToken = sys.argv[1]
chatId = sys.argv[2]
contents = sys.argv[3]
contents = unicode(contents,'euc-kr').encode('utf-8')
bot = telegram.Bot(token = chatToken)
print(contents)
bot.sendMessage(chat_id=chatId, text=contents)