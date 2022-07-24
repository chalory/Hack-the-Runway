from Routes import Route
from twilio.twiml.messaging_response import MessagingResponse
from db import *

route = Route.help
lastImageUrl = ''
# print(route.value[0])

def respond(message):
    response = MessagingResponse()
    print("hello", message, "world")
    response.message(message)
    # print((f"you sent a response : \n\nhi"))
    return str(response)

def get_route1(from_phone_number):
    # todo: work it with different users using json
    return route

def set_route(from_phone_number, type):
    # todo: work it with different users using json
    global route
    route = type
    return route

def getLastImage(from_):
    return lastImageUrl

def setNewImage(imagelink, from_):
    # todo - make different for diff usrs
    global lastImageUrl
    lastImageUrl = str(imagelink)
    insert_img_wa(lastImageUrl)
    return lastImageUrl

def deleteLastImage(from_phone_number):
    # todo: work it with different users using json
    global lastImageUrl
    print('for this', lastImageUrl, 'one')
    if not lastImageUrl: return False
    
    # todo: add db functionality √√
    delete_img(get_conn(), img_url=lastImageUrl)
    lastImageUrl = ''
    return True
    
def updateImageDetails(img_url=lastImageUrl, name=None, description=None, category=None):
    print('you called this')
    global lastImageUrl
    img_url = lastImageUrl
    print(1, img_url, 2, lastImageUrl, name, description, category)
    print('method')
    insert_wa_tables(get_conn(), img_url=img_url, name=name, description=description, category=category)
    pass
    
