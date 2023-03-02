import json
from revChatGPT.V1 import Chatbot
import os
from dotenv import load_dotenv
from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")


load_dotenv()

accessToken = os.getenv('accessToken')

chatbot = Chatbot(config={
  "access_token": accessToken
})

@app.websocket("/feed")
async def chat_gpt(request,ws):
    recv = await ws.recv()
    jsonRecv = json.loads(recv)
    if jsonRecv['code'] == 209:
      return
    for data in chatbot.ask(jsonRecv['message']):
      data['isMe'] = 0
      await ws.send(json.dumps(data,ensure_ascii=False))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9395,auto_reload=True,debug=False)