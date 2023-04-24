FROM python:3.11-alpine

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "logify.main:app", "--host", "0.0.0.0", "--port", "80"]

