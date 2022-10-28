# Pull official base image
# amazon-linux2 버전용
FROM python:3.9-slim-buster

# set work directory
WORKDIR /usr/src/app

# set envirement variable
# .pyc 파일 no 생성
ENV PYTHONDONTWRITEBYTECODE 1

# buffering 하지 않음
ENV PYTHONUNBUFFERED 1

# 도커에 작업 내용 복사
COPY . /usr/src/app/

# install dependencies
RUN python -m pip install --upgrade pip

# 가상환경에서 작성한 모듈들 설치
RUN pip install -r requirements.txt

