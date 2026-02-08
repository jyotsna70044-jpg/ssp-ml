FROM python:3.10-slim
RUN apt-get update && apt-get install -y git build-essential
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
WORKDIR /repo
ENTRYPOINT ["bash", "-c"]