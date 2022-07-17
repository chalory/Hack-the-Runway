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

@app.route("/products",  methods=["GET", "POST"])
def similar_products():
    if flask.request.method == "POST":
        img_url1 = flask.request.args.get('img_url')
        img_url1.status_code = 200
        

    return get_similar_products_info(img_url)

# real_img1 | Poppy Dress                                          | https://dannirosedesigns.com/products/copy-of-sadie-dress?pr_prod_strat=collection_fallback&pr_rec_id=aea24e325&pr_rec_pid=7133789913283&pr_ref_pid=7181513588931&pr_seq=uniform |   170 | https://storage.cloud.google.com/cloud-ai-vision-data/product-search-tutorial/images/469ac87870ba11e88fe4d20059124800.jpg  



@app.route("/get_gallery/<user>")
def get_gallery(phone_number):
    # phone is not used right now
    return get_wa_table()


#

return_similar_products()   




if __name__ == '__main__':
      app.run(port=5000)