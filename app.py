from flask import Flask, request
from full_bot import *
from img_bot_util import *


app = Flask(__name__)

# testing out receiving whatsapp images
@app.route('/receive_img', methods=['POST'])
def receive_img():
    return whatsapp_img_bot()
    
if __name__ == '__main__':
    app.run(port=4000)
