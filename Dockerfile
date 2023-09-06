FROM python:latest

RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/Buenos_Aires /etc/localtime

WORKDIR /app

COPY ./app .

ENV PYTHONPATH=/app

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app","--host","0.0.0.0" ]
