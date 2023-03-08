import uuid
import json

def response_format_200(data):
    return {
        'code': 200,
        'msg': 'success',
        'result': data
    }


def response_format_400(msg, url):
    return {
        'code': 400,
        'msg': msg,
        'url': url,
        'result': None
    }


def response_format_404(msg):
    return {
        'code': 404,
        'msg': msg,
        'result': None
    }


def response_format_500(msg):
    return {
        'code': 500,
        'msg': msg,
        'result': None
    }

def response_chat_Error():
    return json.dumps({
          'isMe':0,
          'message':'网络出错，请稍后再试',
          'parent_id':str(uuid.uuid1())
        },ensure_ascii=False)