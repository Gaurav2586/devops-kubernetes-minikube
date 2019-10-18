FROM python:3.7-alpine

MAINTAINER "Gaurav Agnihotri"


COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 5000
EXPOSE 5001

CMD ["micro-1.py"]
