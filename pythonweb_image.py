from flask import Flask, request, abort

import requests # pip install requests
import urllib3

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage
)

app = Flask(__name__)

#Token
line_bot_api = LineBotApi('tgBlH/o6bTRXjdKuLC3QQ/42RefujzBGP/JPwagMHdpoh0+qQBcIoIJH+PvmRZmepqHG9UdSDvkWNLEWHcC5E5SfptTgPKsgcMgQzFj9nDOE5tT/ULtObrhqhc9WMe/HqeWN7GqzwfBfOhftArE0kgdB04t89/1O/w1cDnyilFU=')
#Channel secret
handler = WebhookHandler('85e93a3b16a648dafd2da84f1a9f9f3e')

APPID="BotChatLine"
KEY = "me37I8KsiCqpTWS"
SECRET = "ozPtNGTK6GPA1STe1PjIvvrwS"
Topic = "/LED_Control"

url = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic)
#curl -X PUT "https://api.netpie.io/topic/LineBotRpi/LED_Control" -d "ON" -u Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I 

urlRESTAPI = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic) + '?auth=' + str(KEY) + ':' + str(SECRET)
#https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I

image_menu = ImageSendMessage(original_content_url='https://www.img.in.th/images/25a44349ac26d45b53b0f4e306449b34.jpg ',preview_image_url='https://image.ibb.co/fx6ibU/hotpotgalaxy240.jpg')
#message = ImageSendMessage(original_content_url='https://telegram.org/img/t_logo.png',preview_image_url='https://telegram.org/img/t_logo.png')
#yesppp = TemplateSendMessage(alt_text='Confirm template',template=ConfirmTemplate(text='Are you sure?',actions=[PostbackTemplateAction(label='postback',text='postback text',data='action=buy&itemid=1'),MessageTemplateAction(label='message',text='message text')]))
#---------------------------------------------------
#@app.route("/")
#@app.route("/callback")
#def hello():
    #return "Hello World!"
    
#----------------------------------------------------
#@app.route("/callback", methods= ['GET','POST','DELETE'])
@app.route("/callback_TESR", methods= ['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if "menu" in str(event.message.text):
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text='On Menu'))
        line_bot_api.reply_message(event.reply_token,image_menu)

        #REST API NETPIE OFF LED
    	#r = requests.put(url, data = {'':'MENU'} , auth=(str(KEY),str(SECRET)))
	
    elif "yes_p" in str(event.message.text):
        #line_bot_api.reply_message(event.reply_token, message)
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='yes_pPP'))

    	#REST API NETPIE ON LED
    	#r = requests.put(url, data = {'':'ON'} , auth=(str(KEY),str(SECRET)))

    elif "on_p" in str(event.message.text):
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='ON LED2'))

    	#REST API NETPIE ON LED
    	r = requests.put(url, data = {'':'ON'} , auth=(str(KEY),str(SECRET)))
		
    elif "off_p" in str(event.message.text):
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='ON LED2'))
	
    	#REST API NETPIE OFF LED
    	r = requests.put(url, data = {'':'OFF'} , auth=(str(KEY),str(SECRET)))


    elif "temp?_p" in str(event.message.text):
    	#REST API NETPIE read sensor value
    	r = requests.put(url, data = {'':'temp?'} , auth=(str(KEY),str(SECRET)))
    	
    	http = urllib3.PoolManager()
    	response = http.request('GET',urlRESTAPI) # read data from publish retain

    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text=((str(response.data)).split('"')[7]) + " °C"))
        
        #r = requests.get(urlRESTAPI)
        #https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I
   
    else:
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

#------------------------------------------------
 
if __name__ == "__main__":
    app.run()

#-------------------------------------------------
