import json
import sys
from revChatGPT.V1 import Chatbot
import os
from dotenv import load_dotenv
from sanic import Sanic
import uuid
import time
import openai

app = Sanic("MyHelloWorldApp")
load_dotenv()

accessToken = os.getenv('accessToken')
apiKey = os.getenv('apiKey')

openai.api_key = apiKey

chatbot = Chatbot(config={
  "access_token": accessToken
})

# next(completion) 

@app.websocket("/openai")
async def open_ai(request,ws):
    while True:
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
        return
      try :
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
        await ws.send(json.dumps({
          'isMe':0,
          'message':'网络出错，请稍后再试',
          'parent_id':str( uuid.uuid1())
        },ensure_ascii=False))
       
@app.websocket("/feed")
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
        await ws.send(json.dumps({
          'isMe':0,
          'message':'网络出错，请稍后再试',
          'parent_id':str( uuid.uuid1())
        },ensure_ascii=False))
      

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9395,auto_reload=True,debug=False)