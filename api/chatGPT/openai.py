# api/pdf/test.py
from sanic import Blueprint, json
import json
from dotenv import load_dotenv
import os
import openai

from config.res_code import response_chat_Error

openaiRoute = Blueprint("openai", url_prefix="")

load_dotenv()

apiKey = os.getenv('apiKey')

openai.api_key = apiKey



@openaiRoute.websocket("/openai")
async def open_ai(request,ws):
    while True:
      try :
        recv = await ws.recv()
        jsonRecv = json.loads(recv)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            stream=True,
            messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": recv}
            ])
        
        if jsonRecv['code'] == 209:
          await ws.send(json.dumps({'code':209,'type':'ping'}))
        else :
          message1 = ''
          for n in completion:
            res = n['choices'][0]['delta']
            if n['choices'][0]['finish_reason']!='stop':
              result = {
                'isMe':0,
                'parent_id':n['id'],
                'message': '',
              }
              if ('content' in res):
                message1 += res['content']
                result['message'] = message1
              await ws.send(json.dumps(result,ensure_ascii=False))
      except Exception as e :
        print(e)
        await ws.send(response_chat_Error())
   
