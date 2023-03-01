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

prompt = "Hello?"





@app.get("/")
async def hello_world(request):
    response = ""
    for data in chatbot.ask(prompt):
      response = data["message"]
    print(response)
    return text("Hello, world.")