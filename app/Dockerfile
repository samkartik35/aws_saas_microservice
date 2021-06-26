FROM python:3.8.5-alpine
MAINTAINER Arvind Kumar

WORKDIR /app
ADD . /app

RUN pip3 install -r requirement.txt

CMD ["python", "run_operation_main.py"]
