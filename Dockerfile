FROM python:3.9.6

WORKDIR /sanic

COPY . .

# RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple/
RUN pip install -r requirements.txt

EXPOSE 9395

CMD ["python", "main.py"]