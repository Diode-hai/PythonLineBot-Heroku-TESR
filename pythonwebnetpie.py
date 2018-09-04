import requests # pip install requests
import urllib3

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError,InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,ImageSendMessage
)

app = Flask(__name__)

#Token
line_bot_api = LineBotApi('tgBlH/o6bTRXjdKuLC3QQ/42RefujzBGP/JPwagMHdpoh0+qQBcIoIJH+PvmRZmepqHG9UdSDvkWNLEWHcC5E5SfptTgPKsgcMgQzFj9nDOE5tT/ULtObrhqhc9WMe/HqeWN7GqzwfBfOhftArE0kgdB04t89/1O/w1cDnyilFU=')
#Channel secret
handler = WebhookHandler('85e93a3b16a648dafd2da84f1a9f9f3e')

#--------------------------------Netpie-------------
APPID="BotChatLine"
KEY = "me37I8KsiCqpTWS"
SECRET = "ozPtNGTK6GPA1STe1PjIvvrwS"
Topic = "/LineChatbot"

url = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic)
#curl -X PUT "https://api.netpie.io/topic/LineBotRpi/LED_Control" -d "ON" -u Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I 

urlRESTAPI = 'https://api.netpie.io/topic/' + str(APPID) + str(Topic) + '?auth=' + str(KEY) + ':' + str(SECRET)
#https://api.netpie.io/topic/LineBotRpi/LED_Control?auth=Jk0ej35pLC7TVr1:edWzwTUkzizhlyRamWWq6nF9I
#---------------------------------------------------

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
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
    if text == 'profile':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='uid: ' + profile.user_id)
                    #TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
            r = requests.put(url, data = {'':profile.user_id} , auth=(str(KEY),str(SECRET)))
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile API without user ID"))
 #--------------------------------------------------------------------------------------
    #elif text == 'i':
       # line_bot_api = LineBotApi('tgBlH/o6bTRXjdKuLC3QQ/42RefujzBGP/JPwagMHdpoh0+qQBcIoIJH+PvmRZmepqHG9UdSDvkWNLEWHcC5E5SfptTgPKsgcMgQzFj9nDOE5tT/ULtObrhqhc9WMe/HqeWN7GqzwfBfOhftArE0kgdB04t89/1O/w1cDnyilFU=')
        #try:
            #line_bot_api.push_message('Ue0767b552bdffaa64add71ce93b016c5', TextSendMessage(text='Hello World!'))
        #except:
            #line_bot_api.reply_message(event.reply_token, 'error')
 #---------------------------------------------------------------------------------               
    elif text == 'bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
    elif text == '1':
        confirm_template = ConfirmTemplate(text='Stone Cake' + '\n' + 'Are you sure about the menu?', actions=[
            MessageAction(label='Yes', text='Yes!'),
            MessageAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
 #-------------------------------------------------------------------------------------       
    elif text == 'Hi':
        #Contact_image = ImageSendMessage(
           #original_content_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85',
            #preview_image_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85'
            #) 
       #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))

        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
        buttons_template = ButtonsTemplate(
            thumbnail_image_url='https://scontent.fbkk1-5.fna.fbcdn.net/v/t1.0-9/39397734_1001769493339424_8256724874488184832_n.jpg?_nc_fx=fbkk1-6&_nc_cat=0&oh=769224df555c6ece24fed770cdffe287&oe=5C0BD1C5',
            title='สวัสดีค่ะ คุณ ' + profile.display_name, text='ยินดีตอนรับเข้าสู่ร้านอาหารเวทมนต์ "TESR" กรุณากดเลือกเมนูด้านล่างนะ', actions=[
                #URIAction(label='Go to line.me', uri='https://line.me'),
                #PostbackAction(label='ping', data='ping'),
                #PostbackAction(label='ping with text', data='ping', text='ping'),
                #MessageAction(label='Translate Rice', text='米')
                MessageAction(label='เมนูอาหาร', text='menu'),
                URIAction(label='ติดต่อพนักงาน', uri='http://line.me/ti/p/~@ion1900z'),
                #URIAction(label='Contact', uri='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85'),
                MessageAction(label='ข้อมูลร้าน', text='contact')
            ])

        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)

        #if buttons_template =='ping':
            #Contact_image = ImageSendMessage(
                #original_content_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85',
                #preview_image_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85'
                #) 
        #line_bot_api.reply_message(event.reply_token, Contact_image)
 #------------------------------------------------------------------------------------- 
    elif text == 'contact':
    #elif PostbackAction.label =='ping':
        Contact_image = ImageSendMessage(
            original_content_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85',
            preview_image_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85'
        ) 
        line_bot_api.reply_message(event.reply_token, Contact_image)


    elif text == 'carousel':
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='hoge1', title='fuga1', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping')
            ]),
            CarouselColumn(text='hoge2', title='fuga2', actions=[
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ]),
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#------------------------------------------------------------------------------------
    #elif text == 'image_carousel':
    elif text == 'menu':
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/39258923_1001266590056381_2474212427365875712_n.jpg?_nc_cat=0&oh=ae7f3674e018cfdb527ed3687540ba02&oe=5BF3F3C6',
                                action=URIAction(
                                    label='Menu All',uri='https://line.me'
                                    )),
            ImageCarouselColumn(image_url='https://scontent.fbkk1-3.fna.fbcdn.net/v/t1.0-9/39454660_1001737283342645_6691743344214671360_n.jpg?_nc_fx=fbkk1-6&_nc_cat=0&oh=269858a5a47d917d437695e5782b8e64&oe=5C0886A1',
                                action=URIAction(
                                    label='Menu 1',uri='https://line.me'
                                    )),
            ImageCarouselColumn(image_url='https://scontent.fbkk1-6.fna.fbcdn.net/v/t1.0-9/39442752_1001738930009147_2170020964899749888_n.jpg?_nc_fx=fbkk1-6&_nc_cat=0&oh=d8ea897702d1d78eb921241afd90f62e&oe=5C119FA8',
                                action=URIAction(
                                    label='Menu 2',uri='https://line.me'
                                    )),
            ImageCarouselColumn(image_url='https://scontent.fbkk1-4.fna.fbcdn.net/v/t1.0-9/39221449_1001737313342642_6907313284718788608_n.jpg?_nc_fx=fbkk1-6&_nc_cat=0&oh=291709d75d28d0b2c35d28ad6ba249a4&oe=5C0783BB',
                                action=URIAction(
                                    label='Menu 3',uri='https://line.me'
                                    ))
        ])
        template_message = TemplateSendMessage(
            alt_text='ImageCarousel alt text', template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#------------------------------------------------------------------------------------
    elif text == 'imagemap':
        pass
    elif text == 'flex':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://example.com/cafe.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Brown Cafe', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Shinjuku, Tokyo',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='CALL', uri='tel:000000'),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='WEBSITE', uri="https://example.com")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'quick_reply':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='Quick reply',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="label1", data="data1")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="label2", text="text2")
                        ),
                        QuickReplyButton(
                            action=DatetimePickerAction(label="label3",
                                                        data="data3",
                                                        mode="date")
                        ),
                        QuickReplyButton(
                            action=CameraAction(label="label4")
                        ),
                        QuickReplyButton(
                            action=CameraRollAction(label="label5")
                        ),
                        QuickReplyButton(
                            action=LocationAction(label="label6")
                        ),
                    ])))
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title=event.message.title, address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )



@handler.add(FollowEvent)
def handle_follow(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Got follow event'))


@handler.add(UnfollowEvent)
def handle_unfollow():
    app.logger.info("Got Unfollow event")


@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Joined this ' + event.source.type))


@handler.add(LeaveEvent)
def handle_leave():
    app.logger.info("Got leave event")

@handler.add(BeaconEvent)
def handle_beacon(event):
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
    buttons_template = ButtonsTemplate(
        thumbnail_image_url='https://scontent.fbkk1-5.fna.fbcdn.net/v/t1.0-9/39397734_1001769493339424_8256724874488184832_n.jpg?_nc_fx=fbkk1-6&_nc_cat=0&oh=769224df555c6ece24fed770cdffe287&oe=5C0BD1C5',
        title='สวัสดีค่ะ คุณ ' + profile.display_name, text='ยินดีตอนรับเข้าสู่ร้านอาหารเวทมนต์ "TESR" กรุณากดเลือกเมนูด้านล่างนะ', actions=[
                #URIAction(label='Go to line.me', uri='https://line.me'),
                #PostbackAction(label='ping', data='ping'),
                #PostbackAction(label='ping with text', data='ping', text='ping'),
                #MessageAction(label='Translate Rice', text='米')
            MessageAction(label='เมนูอาหาร', text='menu'),
            URIAction(label='ติดต่อพนักงาน', uri='http://line.me/ti/p/~@ion1900z'),
                #URIAction(label='Contact', uri='https://scontent.fbkk10-1.fna.fbcdn.net/v/t1.0-9/25348376_10209405901979171_4715413657210557947_n.jpg?_nc_cat=0&oh=782afc517da25d80cf014aedf1a59b9b&oe=5C0DDB85'),
            MessageAction(label='ข้อมูลร้าน', text='contact')
        ])
    template_message = TemplateSendMessage(
        alt_text='Buttons alt text', template=buttons_template)
    line_bot_api.reply_message(event.reply_token, template_message)
    
    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(
            #text='Got beacon event. hwid={}, device_message(hex string)={}'.format(
                #event.beacon.hwid, event.beacon.dm)))


if __name__ == "__main__":
    app.run()
