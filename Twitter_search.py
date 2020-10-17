#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ライブラリ
import json,config
from requests_oauthlib import OAuth1Session

#API取得
ck = config.consumer_key
cs = config.consumer_secret
at = config.access_token
ats = config.access_token_secret

twitter = OAuth1Session(ck, cs, at,ats)#OAuth認証


API_URL = "https://api.twitter.com/1.1/search/tweets.json?q="
keyword = "猫　可愛い　-RT"
what_type_result_data = "resent"  # mixed, recent, popular
how = 10
url = API_URL + keyword + "&result_type=" + what_type_result_data + "&count=" + str(how)
response = twitter.get(url)#URLとして読み込ませる

response_data = json.loads(response.text) 
response_data #テキストの可視化


# In[2]:


#テキストを変数に代入
data = response_data['statuses'][0]
who = data['user']['name']
when = data['created_at'][:19]
what = data['text']
where = data['place']
retweet = data['retweet_count']
twitter_url = 'https://twitter.com/yjbtjn/status/' + str(data['id'])
description =  data['user']['description']

#送信したい内容
output=(what),(twitter_url)


# In[3]:


import requests
 
def LineNotify(message):
    line_notify_token = "*********************"
    line_notify_api = "https://notify-api.line.me/api/notify"
 
    payload = {"message":message}
    headers = {"Authorization":"Bearer " + line_notify_token}
    requests.post(line_notify_api, data = payload, headers = headers)
 
LineNotify(output)

