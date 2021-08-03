FROM ubuntu:21.04
#21.04 has 10.3 gcc
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -y
RUN apt install build-essential -y
RUN apt install python3-pip -y
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY /html ./html
COPY DBconnection.py .
COPY app.py .
COPY pydantic_model.py .
COPY S3creds.py .
ENV aws_access_key_id=iam user access key
ENV aws_secret_access_key=secretkey
ENV password=password
CMD [ "uvicorn","app:app","--host","0.0.0.0" ]
