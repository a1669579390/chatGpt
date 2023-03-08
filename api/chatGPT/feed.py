# api/pdf/test.py
import json
from revChatGPT.V1 import Chatbot
import os
from dotenv import load_dotenv

from sanic import Blueprint

from config.res_code import response_chat_Error

feed = Blueprint("feed", url_prefix="")

load_dotenv()


accessToken = os.getenv('accessToken')

chatbot = Chatbot(config={
  "access_token": accessToken
})
       
@feed.websocket("/feed")
async def chat_gpt(request,ws):
    while True:
      recv = await ws.recv()
      jsonRecv = json.loads(recv)
      if jsonRecv['code'] == 209:
        return
      try :
        for data in chatbot.ask(jsonRecv['message']):
          data['isMe'] = 0
          await ws.send(json.dumps(data,ensure_ascii=False))
      except Exception as e :
        print(e)
        await ws.send(response_chat_Error())
   