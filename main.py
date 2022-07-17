from flask import Flask, jsonify
from db import *
from pprint import pprint
app = Flask(__name__)
from get_similar_products import *

@app.route("/similar_products/<img_url>")
def similar_products(img_url):
    return get_similar_products_info(img_url)

@app.route("/get_gallery/<user>")
def get_gallery(phone_number):
    # phone is not used right now
    return get_wa_table()



if __name__ == '__main__':
      app.run(port=5000)