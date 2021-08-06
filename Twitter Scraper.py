import tweepy
import csv
import pandas as pd

api_key = ""
api_secret_key = ""
access_token = ""
access_token_secret = ""
#insert your API Key and Secret and your Access Token Key and Secret

auth = tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
search_key = ""
#insert search key that you needed

csvFile = open(search_key+".csv","a+",newline="",encoding="utf-8")
csvWriter = csv.writer(csvFile)
c = []
u = []
l = []
t = []

for tweet in tweepy.Cursor(api.search,q=search_key,count=10000).items():
    print(tweet.created_at,tweet.user.screen_name,tweet.user.location,tweet.text)
    c.append(tweet.created_at)
    u.append(tweet.user.screen_name)
    l.append(tweet.user.location)
    t.append(tweet.text.encode("utf-8"))
    tweets = [tweet.created_at,tweet.user.screen_name,tweet.user.location,tweet.text.encode("utf-8")]
    csvWriter.writerow(tweets)

dictTweets = {"Waktu":c,"Pengguna":u,"Lokasi":l,"Tweet":t}
df = pd.DataFrame(dictTweets,columns=["Waktu","Pengguna","Lokasi","Tweet"])
