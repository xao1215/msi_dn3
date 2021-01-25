FROM python:3-alpine
RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask redis pymongo
RUN mkdir /app

#change to app2.py/app3.py
COPY app.py /app
WORKDIR /app

#change to app2.py/app3.py
CMD ["python", "app.py"]
EXPOSE 8080
