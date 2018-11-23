FROM python:3.7.1-alpine3.8

VOLUME /usr/src/sphinx
WORKDIR /usr/src/sphinx

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt \
    && echo "http://mirrors.aliyun.com/alpine/v3.8/main/" > /etc/apk/repositories \
    && apk add --no-cache make 

CMD [ "/usr/bin/make", "html" ]
