FROM python:3-alpine

RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask redis pymongo
# copy application files
RUN mkdir /app
COPY app.py /app

WORKDIR /app


CMD ["python", "app.py"]

EXPOSE 8080
