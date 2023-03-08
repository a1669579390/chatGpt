# api/__init__.py
from sanic import Blueprint
from .chatGPT import chatGPT


api = Blueprint.group(chatGPT, url_prefix='')
