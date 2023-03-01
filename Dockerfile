FROM python:3.9

WORKDIR /sanic

COPY . .

RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/

EXPOSE 9395

CMD ["python", "main"]