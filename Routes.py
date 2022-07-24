from enum import Enum

class Route(Enum):
    help =  f"\n Welcome to *WhatsThatFashionware*!\n" \
            'This bot helps to get the !\n' \
            '*Please follow the steps to use the bot:*\n' \
            "\n'cancel' or 'delete' - delete previously added image" \
            "To repeat this message, ask me to 'help' or 'repeat'!n",

    # help = f"\n Hi \n there \ns"
    
    cancel = f'You canceled! We deleted your image 😉',
    
    send_image = f"We received your image!",
    
    add_name = "\nnAdd\n a name if you want to!",
    
    add_description = 'Add a description if you want to!',
    
    add_category = 'Add the image to a category if you want to!'
    
    
    