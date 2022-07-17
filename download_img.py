import requests # request img from web
import shutil # save img locally

def download_twilio_img(twilio_url):
    file_name = 'photo_to_search.jpeg'

    res = requests.get(twilio_url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
