from logging import addLevelName
import os
from flask import request, Flask
from dotenv import load_dotenv
from img_bot_util import *
from Routes import Route

load_dotenv()

def whatsapp_img_bot():
    # get the message
    sender_phone_number = request.form.get('From')
    message_body = request.form.get('Body')
    img_url = request.form.get('MediaUrl0') 
    
    # print(f"{sender_phone_number} sent: \n{message_body}\n{img_url}\n")
    
    # get the current route for the current user
    route = get_route1(sender_phone_number)
    print(route)
    
    # if the user asks to help or cancel
    if 'help' in message_body or 'image' in message_body:
        set_route(sender_phone_number, Route.send_image)
        response = str(f'it seems like you asked for help! {Route.help.value[0]}')
        return respond(str(response))
    if 'cancel' in message_body or 'delete' in message_body:
        response = f"you asked to cancel or delete the previously added image.\n"
        set_route(sender_phone_number, help)
        deleted = deleteLastImage(sender_phone_number)
        if not deleted: 
            response = 'there is no previous image to delete.\n'
        return respond(response)
    
    # if the user sends an image
    if img_url:
        # I can assume that the user either already added description and categories for previous image
        # all that is left is to add the actual iamge to the database
        route = set_route(sender_phone_number, Route.add_name)
        setNewImage(img_url, sender_phone_number)
        print(getLastImage(sender_phone_number), 1)
        print(f"\nnAdd\n a name if you want to!")
        return respond(f"{Thanks for your image! We have saved it.}")
    
    # the user just sent an image, and now is sending a name -> set the name
    if route == Route.add_name:
        print(getLastImage(sender_phone_number), 2)
        route = set_route(sender_phone_number, Route.add_description)
        updateImageDetails(name=message_body)
        print(getLastImage(sender_phone_number), 3)
        response = f"You named your image '{message_body}'. \n{route.value[0]}"
        return respond(response)
    
    # description
    if route == Route.add_description:
        route = set_route(sender_phone_number, Route.add_category)
        updateImageDetails(description=message_body)
        response = f"Your image is description is '{message_body}'. \n{route.value[0]}"
        return respond(response)
    
    # category
    if route == Route.add_category:
        route = set_route(sender_phone_number, Route.add_category)
        updateImageDetails(category=message_body)
        response = f"Your image is description is '{message_body}'. \n{route.value[0]}"
        return respond(response)
    
    # default response
    return respond("Sorry. please try again.")

# cockroach sql --url "postgresql://chantal:hackrunway2022@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/defaultdb?options=--cluster%3Dhackrunway2022-2943&sslmode=verify-full&sslrootcert=%2FUsers%2Fbrayton%2F.postgresql%2Froot.crt"
# show tables;
# select * from wa_table;
#  real_img1 | Poppy Dress                                          | https://dannirosedesigns.com/products/copy-of-sadie-dress?pr_prod_strat=collection_fallback&pr_rec_id=aea24e325&pr_rec_pid=7133789913283&pr_ref_pid=7181513588931&pr_seq=uniform |   170 | https://storage.cloud.google.com/cloud-ai-vision-data/product-search-tutorial/images/469ac87870ba11e88fe4d20059124800.jpg  