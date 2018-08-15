from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import requests # pip install requests

import urllib3


app = Flask(__name__)

#Token
line_bot_api = LineBotApi('ItfoFj89IMTUAR2ERKN1yPxAPZk4UvEC4fperPkGrCg/L6GwTXKR/sOC1KEYyMJppqHG9UdSDvkWNLEWHcC5E5SfptTgPKsgcMgQzFj9nDNTaJlDhv/Xw+0ahLBCWC8nO8sMe6GSGd+dP6fmoFMPNwdB04t89/1O/w1cDnyilFU=')
#Channel secret
handler = WebhookHandler('85e93a3b16a648dafd2da84f1a9f9f3e')

APPID="BotChatLine"
KEY = "me37I8KsiCqpTWS"
SECRET = "ozPtNGTK6GPA1STe1PjIvvrwS"
Topic = "/LED_Control_TESR"

url = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic)
#curl -X PUT "https://api.netpie.io/topic/LineBotRpi/LED_Control" -d "ON" -u Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I 

urlRESTAPI = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic) + '?auth=' + str(KEY) + ':' + str(SECRET)
#https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I



@app.route("/callback_TESR", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	#global url , KEY , SECRET
    if "on" in str(event.message.text):
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='ON LED'))

    	#REST API NETPIE ON LED
    	r = requests.put(url, data = {'':'ON'} , auth=(str(KEY),str(SECRET)))
		
    elif "off" in str(event.message.text):
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='OFF LED'))

    	#REST API NETPIE OFF LED
    	r = requests.put(url, data = {'':'OFF'} , auth=(str(KEY),str(SECRET)))
	
    elif "menu" in str(event.message.text):
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Menu'))
	#image_message = ImageSendMessage(
    	#original_content_url='https://previews.123rf.com/images/seamartini/seamartini1708/seamartini170800547/84922979-japanese-cuisine-restaurant-menu-template-vector-lunch-offer-for-sweet-syrup-tangerine-tory-kenko-ya.jpg',
    	#preview_image_url='https://previews.123rf.com/images/seamartini/seamartini1708/seamartini170800547/84922979-japanese-cuisine-restaurant-menu-template-vector-lunch-offer-for-sweet-syrup-tangerine-tory-kenko-ya.jpg'
    	#)

    	#--REST API NETPIE OFF LED--
    	#r = requests.put(url, data = {'':'OFF'} , auth=(str(KEY),str(SECRET)))

    elif "temp?" in str(event.message.text):
    	#REST API NETPIE read sensor value
    	r = requests.put(url, data = {'':'temp?'} , auth=(str(KEY),str(SECRET)))
    	
    	http = urllib3.PoolManager()
    	response = http.request('GET',urlRESTAPI) # read data from publish retain

    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text=((str(response.data)).split('"')[7]) + " °C"))
        
        #r = requests.get(urlRESTAPI)
        #https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I
        
    else:
    	line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
