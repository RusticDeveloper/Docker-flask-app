FROM alpine:3.14
RUN apk add --no-cache python3 py3-pip \
 && pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3","run.py" ]


