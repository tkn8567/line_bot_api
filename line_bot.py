import os
import sys
sys.path.append(os.path.join(os.getcwd(),'site-packages'))

import json
info = json.load(open('info.json', 'r'))

from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info["LINE_API_TOKEN"][0]["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info["LINE_API_TOKEN"][0]['USER_ID']
    messages = TextSendMessage(text='Hello \n World')
    line_bot_api.push_message(USER_ID, messages = messages)
if __name__ == "__main__":
    main()