from google.cloud import vision

def get_similar_products_file(
        project_id,
        location,
        product_set_id,
        product_category,
        file_path,
        filter,
        max_results
):
    """Search similar products to image.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_set_id: Id of the product set.
        product_category: Category of the product.
        file_path: Local file path of the image to be searched.
        filter: Condition to be applied on the labels.
                Example for filter: (color = red OR color = blue) AND style = kids
                It will search on all products with the following labels:
                color:red AND style:kids
                color:blue AND style:kids
        max_results: The maximum number of results (matches) to return. If omitted, all results are returned.
    """
    # product_search_client is needed only for its helper methods.
    product_search_client = vision.ProductSearchClient()
    image_annotator_client = vision.ImageAnnotatorClient()

    # Read the image as a stream of bytes.
    with open(file_path, 'rb') as image_file:
        content = image_file.read()

    # Create annotate image request along with product search feature.
    image = vision.Image(content=content)

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
        image,
        image_context=image_context,
        max_results=max_results
    )

    index_time = response.product_search_results.index_time
    print('Product set index time: ')
    print(index_time)

    results = response.product_search_results.results
    return results

    # print('Search results:')
    # for result in results:
    #     product = result.product

    #     print('Score(Confidence): {}'.format(result.score))
    #     print('Image name: {}'.format(result.image))

    #     print('Product name: {}'.format(product.name))
    #     print('Product display name: {}'.format(
    #         product.display_name))
    #     print('Product description: {}\n'.format(product.description))
    #     print('Product labels: {}\n'.format(product.product_labels))
        
# get_similar_products_uri(project_id='hack-the-runway', location='asia-east1', product_set_id='product_set0', product_category="apparel-v2", image_uri=twiliorl appspot.com/blue-plaid-pleated-jumper-2.jpg", filter="style=womens OR style=women")

x = get_similar_products_file(
        project_id='hack-the-runway',
        location='asia-east1',
        product_set_id='product_set0',
        product_category='apparel-v2',
        file_path='photo_to_search.jpeg',
        filter='style=womens OR style=women',
        max_results=100
)
# print(x)

from download_img import *
def get_similar_products_from_twilio_img(twilio_img_link='https://api.twilio.com/2010-04-01/Accounts/AC25b264f295b2e06eff7efc77a3ff2132/Messages/MM5849a1fc9938bb660638e155fcf2153c/Media/ME5a450de3aba51f7efe69924b8a3ef78a'):
    # first download the file as a local file
    download_twilio_img(twilio_img_link)
    
    # the img will be stored in a file called 'photo_to_search.jpeg'
    filepath = "photo_to_search.jpeg"
    
    # similar products with its raw data
    x = get_similar_products_file(
        project_id='hack-the-runway',
        location='asia-east1',
        product_set_id='product_set0',
        product_category='apparel-v2',
        file_path=filepath,
        filter='style=womens OR style=women',
        max_results=100
    )
    
    # return it
    return x

    
print(get_similar_products_from_twilio_img('https://api.twilio.com/2010-04-01/Accounts/AC25b264f295b2e06eff7efc77a3ff2132/Messages/MM5849a1fc9938bb660638e155fcf2153c/Media/ME5a450de3aba51f7efe69924b8a3ef78a'))
