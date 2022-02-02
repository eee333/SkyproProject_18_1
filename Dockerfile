FROM python:3.10-slim
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
CMD flask run -h 0.0.0.0 -p 80

