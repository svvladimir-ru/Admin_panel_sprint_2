FROM python:3.9.7-buster
WORKDIR /sites
COPY requirements.txt /sites
RUN pip install -r /sites/requirements.txt
COPY movies_admin/ /sites