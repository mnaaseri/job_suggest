FROM python:3.8
WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install --timeout 1000 -r requirements.txt

EXPOSE 8080

CMD uvicorn --host ${HOST:-"0.0.0.0"} --port ${PORT:-"8080"} app.main:app --reload
