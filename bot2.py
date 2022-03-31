#2 Bot twitter
#Publicar tweet con una imagen\video\Gif

import tweepy

API_KEY = "" #Tu API KEY
API_SECRET = "" #Tu API KEY SECRET
ACCESS_TOKEN = "" #TU ACCESS TOKEN
ACCESS_SECRET = "" #TU ACCESS TOKEN SECRET
 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)
 
def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])
upload_media('Aqui va el texto','Aqui va el nombre del archivo')


