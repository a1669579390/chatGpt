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

prompt = "写一个递归"





@app.get("/")
async def hello_world(request):
    response = ""
    for data in chatbot.ask(prompt):
      response = data["message"]
    print(response)
    return text(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9395)