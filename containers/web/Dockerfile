FROM ubuntu:20.04

RUN apt update && apt install -y build-essential zlib1g-dev \
libncurses5-dev libgdbm-dev libnss3-dev \
libssl-dev libreadline-dev libffi-dev curl libbz2-dev liblzma-dev

COPY source/Python-3.9.0.tar.xz .
RUN tar -xf Python-3.9.0.tar.xz

RUN cd Python-3.* && ./configure && make -j8 && make install

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY django ./django
WORKDIR django
RUN python3 manage.py collectstatic
