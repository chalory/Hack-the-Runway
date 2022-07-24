from flask import Flask, jsonify
from db import *
from pprint import pprint
app = Flask(__name__)
from get_similar_products import *
import flask



@app.route('/') 
def hello_world():
    response = jsonify('Hello world!')
    response.status_code = 200
    return response

# @app.route("/products/'<url>'",  methods=["GET", "POST"])
# def similar_products(url):
#     if flask.request.method == "POST":
#         img_url1 = flask.request.args.get('img_url')
#         img_url1.status_code = 200
  
@app.route("/products?id=WX3kDaN8alrv4PM0Ta8Xp32KpsvCtYzkuDmKyHZ9NEW")
def similar_products(img_url='https://api.twilio.com/2010-04-01/Accounts/AC25b264f295b2e06eff7efc77a3ff2132/Messages/MM5849a1fc9938bb660638e155fcf2153c/Media/ME5a450de3aba51f7efe69924b8a3ef78a'):
    return f"{get_similar_products_info(img_url)}"
        

#     return get_similar_products_info(url)

# real_img1 | Poppy Dress                                          | https://dannirosedesigns.com/products/copy-of-sadie-dress?pr_prod_strat=collection_fallback&pr_rec_id=aea24e325&pr_rec_pid=7133789913283&pr_ref_pid=7181513588931&pr_seq=uniform |   170 | https://storage.cloud.google.com/cloud-ai-vision-data/product-search-tutorial/images/469ac87870ba11e88fe4d20059124800.jpg  


# export GOOGLE_APPLICATION_CREDENTIALS="/Users/brayton/Downloads/hack-the-runway-3199276e8068.json"
import json
@app.route("/get_gallery")
def get_gallery():
    # phone is not used right now
    response = get_wa_table()
    response = flask.jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


#

return_similar_products()   




if __name__ == '__main__':
      app.run(port=5000)