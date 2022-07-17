import requests # request img from web
import shutil # save img locally

def download_twilio_img(twilio_url='https://api.twilio.com/2010-04-01/Accounts/AC25b264f295b2e06eff7efc77a3ff2132/Messages/MM5849a1fc9938bb660638e155fcf2153c/Media/ME5a450de3aba51f7efe69924b8a3ef78a'):
    file_name = 'photo_to_search.jpeg'

    res = requests.get(twilio_url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

# download_twilio_img()