import os
import sys
sys.path.append(os.path.join(os.getcwd(),'site-packages'))

import json
info = json.load(open('info.json', 'r'))


import tweepy

AK = info["TWITTER_API_TOKEN"][0]["API_KEY"]
AKS = info["TWITTER_API_TOKEN"][0]["API_KEY_SECRET"]
BT = info["TWITTER_API_TOKEN"][0]["BEARER_TOKEN"]
AT = info["TWITTER_API_TOKEN"][0]["ACCESS_TOKEN"]
ATS =  info["TWITTER_API_TOKEN"][0]["ACCESS_TOKEN_SECRET"]

client = tweepy.Client(bearer_token=BT,
                        consumer_key=AK,
                        consumer_secret=AKS,
                        access_token=AT,
                        access_token_secret=ATS)

# client.create_tweet(text="twitter api test\ntwitter api test")
# 自分のアカウントでツイート作成
# https://twitter.com/Kana26787048/status/1709387571019895011
# <blockquote class="twitter-tweet"><p lang="et" dir="ltr">twitter api test<br>twitter api test</p>&mdash; Kana🌻 (@Kana26787048) <a href="https://twitter.com/Kana26787048/status/1709387571019895011?ref_src=twsrc%5Etfw">October 4, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

def userIdGet(account):
    user = client.get_user(username=account)
    
    return user[0]['id']

accountid = userIdGet("Kana26787048")

print(accountid)

# https://twitter.com/i/oauth2/authorize?response_type=code&client_id=WnRncEhmSjBYMW5LR3BTenN1ZFg6MTpjaQ&redirect_uri=https://twitter.com/&scope=tweet.read%20tweet.write%20users.read&state=abc&code_challenge=aaa&code_challenge_method=s256

# https://confrage.jp/twitter-api-v2でoauth2-0認証でtweetするoauth-2-0-authorization-code-flow-with-pkce/
# https://zenn.dev/kg0r0/articles/8b1cfe654a1cee
# 加藤に聞く

# curl "https://api.twitter.com/2/tweets?ids=1261326399320715264,1278347468690915330" -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAJXoqAEAAAAA9YYAZhDwx2RIuAG0Z0dIrg1wFWw%3DYUrzZYKfQAT14omehMhAwFgfN7LrcYc4bZ3XKy4jKAkrr7KNB3"

# https://scr.marketing-wizard.biz/dev/tweepy-twitter-apiv2#413fc82cf3ed459ea750ea3fc4789343
# 参考にした

# docs: https://docs.tweepy.org/en/stable/examples.html