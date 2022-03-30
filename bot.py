#1 Bot twitter
#Publicar tweet

import tweepy

API_KEY = "" #Tu API KEY
API_SECRET = "" #Tu API KEY SECRET
ACCESS_TOKEN = "" #TU ACCESS TOKEN
ACCESS_SECRET = "" #TU ACCESS TOKEN SECRET
 
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)
 
 
def PubTweet(message):
    api.update_status(status=message)
 
PubTweet("  ") #Aqui va el texto que quieres publicar
