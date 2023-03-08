# api/pdf/__init__.py
from sanic import Blueprint

from .feed import feed
from .openai import openaiRoute

chatGPT = Blueprint.group(openaiRoute, feed, url_prefix="")
