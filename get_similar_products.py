
from google.cloud import vision
import pandas as pd
from pprint import pprint

df = pd.read_csv(r'/home/chantal/Downloads/vision_product_search_product_catalog_updated.csv')

# df_new = df.iloc[:, 0:2]
# df_new.columns = ['col1', 'col2']
# # df_new['col3'] = df_new[]
# # loop over results, getting all where the results.imagetag == dfnew['col1']
# # loop over df, select all from col1 where col2 equals list
# print(df_new)


def transformGS(gslink = 'gs://cloud-ai-vision-data/product-search-tutorial/images/468fc8f570ba11e8b821d20059124800.jpg'):
    newlink = f"https://storage.cloud.google.com/{gslink[5::]}"
    # print(newlink)
    return newlink

def get_similar_products_uri(
        project_id, location, product_set_id, product_category,
        image_uri, filter):
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        image_uri: Cloud Storage location of image to be searched.
        filter: Condition to be applied on the labels.
        Example for filter: (color = red OR color = blue) AND style = kids
        It will search on all products with the following labels:
        color:red AND style:kids
        color:blue AND style:kids
    """
    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    # Create annotate image request along with product search feature.
    image_source = vision.ImageSource(image_uri=image_uri)
    image = vision.Image(source=image_source)

    # product search specific parameters
    product_set_path = product_search_client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)
    product_search_params = vision.ProductSearchParams(
        product_set=product_set_path,
        product_categories=[product_category],
        filter=filter)
    image_context = vision.ImageContext(
        product_search_params=product_search_params)

    # Search products similar to the image.
    response = image_annotator_client.product_search(
        image, image_context=image_context)

    index_time = response.product_search_results.index_time
    print('Product set index time: ')
    # print(index_time)

    results = response.product_search_results.results
    # print(results)

    print('Search results:')
    for result in results:
        product = result.product
        # print(product)

    #     print('Score(Confidence): {}'.format(result.score))
    #     print('Image name: {}'.format(result.image))

    #     print('Product name: {}'.format(product.name))
    #     print('Product display name: {}'.format(
    #         product.display_name))
    #     print('Product description: {}\n'.format(product.description))
    #     print('Product labels: {}\n'.format(product.product_labels))
    
    # img_url = []
    # for a,b in df_new.itertuples(index=False):
    #     if result.image == df.iloc[2]:
    #         img_url = df.iloc[:,0]
    #     print(img_url)
     

    return results

# returns 'imageX' where X is a number
def getImageTag(imagePath):
    i = len(imagePath) - 1
    while (imagePath[i:i+1]).isnumeric():
        i -= 1
    x = imagePath[i+1::]
    X = int(x)
    # print(f"{imagePath} image{X}")
    return f"image{X}"

# returns image tags of all results as an array
def getAllImageTags(results):
    arr = [] # array of image tag strings 'image86'
    for result in results:
        arr.append((getImageTag(result.image), result.score))
    # print(arr)
    return arr

# def sortAndPrintImages(similar_products):
#     for result in similar_products:
#         print()


# x = get_similar_products_uri(project_id='hack-the-runway', location='asia-east1', product_set_id='product_set0', product_category="apparel-v2", image_uri="gs://cloud-ai-vision-data/product-search-tutorial/images/468f782e70ba11e8941fd20059124800.jpg", filter="style=womens OR style=women")
x = get_similar_products_uri(project_id='hack-the-runway', location='asia-east1', product_set_id='product_set0', product_category="apparel-v2", image_uri="gs://hack-the-runway.appspot.com/blue-plaid-pleated-jumper-2.jpg", filter="style=womens OR style=women") # 
# getImageTag('projects/hack-the-runway/locations/asia-east1/products/product_id4/referenceImages/image4')
# print(getAllImageTags(x))

df_new = df.iloc[:, 0:2]
df_new.columns = ['col1', 'col2']
# df_new['col3'] = df_new[]
# loop over results, getting all where the results.imagetag == dfnew['col1']
# loop over df, select all from col1 where col2 equals list
# print(df_new)

# return an array of links based on image tags
# twilurl  -> []
def getLinks(imageTags, df):
    arr = []
    for tag, score in imageTags:
        gslink = (df[df['col2'] == tag]['col1'].max())
        link = transformGS(gslink)
        arr.append((link, score, tag))
    # pprint(arr)
    return arr

# x = get_similar_products_uri(project_id='hack-the-runway', location='asia-east1', product_set_id='product_set0', product_category="apparel-v2", image_uri=twiliorl appspot.com/blue-plaid-pleated-jumper-2.jpg", filter="style=womens OR style=women") # 
getLinks(getAllImageTags(x), df_new)


'''
Search results:
name: "projects/hack-the-runway/locations/asia-east1/products/product_id22"
display_name: " "
product_category: "apparel-v2"
product_labels {
  key: "style"
  value: "women"
}
product_labels {
  key: "category"
  value: "dress"
}
product_labels {
  key: "kids"
  value: "true"


'''

'''
gs://cloud-ai-vision-data/product-search-tutorial/images/46a0cbcf70ba11e89399d20059124800.jpg,
image0,
product_set0,
product_id0,
apparel-v2,
6,
\"style=women,
category=shoe\"\r."
'''

'''
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @import_request.json \
https://vision.googleapis.com/v1/projects/$PROJECT_ID/locations/$LOCATION_ID/productSets:import
'''
'''
curl -X GET \
-H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
-H "Content-Type: application/json" \
https://vision.googleapis.com/v1/locations/$LOCATION_ID/operations/557bd0f4a139361d
'''

# url to image ->
# getsimilarproductsuri(...,url) returns [urls of similar images] ->
# use method that looks into search_table transform [urls of similar images] to [dictionaries with information of similar images]
    # [
    # {link: ..., price: ..., name: ...}, item1
    # {link: ..., price: ..., name: ...}, item2
    # {link: ..., price: ..., name: ...} item3
    # ]

# blue dress -> result=[{name:bluedress1, price:70}, {name:bluedress2, price:77}, {name:...,price:3}]
# one dict can only one unique key
# result[0].name
# result[1].price
# for product in result: print(product.name)

x = get_similar_products_uri(project_id='hack-the-runway', location='asia-east1', product_set_id='product_set0', product_category="apparel-v2", image_uri="gs://hack-the-runway.appspot.com/blue-plaid-pleated-jumper-2.jpg", filter="style=womens OR style=women")
print("here")
# pprint(getLinks(getAllImageTags(x), df_new))

from db import *
# return [dictionary] 
def get_similar_products_info(img_url):
    # get similar products to img url
    x = get_similar_products_uri(project_id='hack-the-runway', location='asia-east1', product_set_id='product_set0', product_category="apparel-v2", image_uri="gs://hack-the-runway.appspot.com/blue-plaid-pleated-jumper-2.jpg", filter="style=womens OR style=women")

    # [(link:str (.../.../),score: int (0.23),tag: str (image6))]
    similar_prod_info1 = getLinks(getAllImageTags(x), df_new)
    # for test
    # similar_prod_info1 = [('second url11',1,1),('second url1111',1,1),('second url',1,1)]

    # match with the database for each and every similar product
    # the database takes a link and maps it to its preset information
    results = []
    for (img_link, score, tag) in similar_prod_info1:
        # print(get_where_link_is(img_link))
        # (link, name, extern_link, price) = get_where_link_is(img_link)
        print('img link', img_link)
        data = get_where_link_is(img_link)
        print('data')
        if not data: continue
        print(data[0][0])
        # (link, name, extern_link, price) = data[0]
        doc = {
            'image_link': data[0][-1],
            'name': data[0][1],
            'extern_link': data[0][2],
            'price': data[0][3],
            'score': round(score * 100),
            'tag': tag
        }
        results.append(doc)
    return results
'''
[('real_img1',
  'Solea Dress',
  'https://www.etsy.com/au/listing/1097550887/solea-cartamodello-abito-bimba-tg-3a-10a',
  10,
  'https://storage.cloud.google.com/cloud-ai-vision-data/product-search-tutorial/images/469fe8d970ba11e8bc23d20059124800.jpg')]
'''
def return_similar_products():
    
    data = get_where_link_is('real_img1')
    
    pprint(data)
    dictionaries = []
    for singledataset in data:
        dict = {
            'img_link': singledataset[-1],
            'name': singledataset[1],
            'price': singledataset[3],
            'purchase_link': singledataset[2]
        }
        dictionaries.append(dict)

        pprint(dictionaries)


print('this')
pprint(get_similar_products_info('gs://hack-the-runway.appspot.com/blue-plaid-pleated-jumper-2.jpg'))






# searchtable contains all photo searchable image information 
# lookup searchtable where link = link (key) in table -> []