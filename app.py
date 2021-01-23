from flask import Flask, render_template
from redis import Redis
from pymongo import MongoClient
import socket
import time

hostname = socket.gethostname()
app = Flask(__name__)


client = MongoClient("mongodb://mongo:27017") 
db = client.containers_list

hostname = socket.gethostname()
redis = Redis(host="redis.default.svc.cluster.local") # port=6379


def insert():

    hostname = socket.gethostname()
    y = True
    for x in db.containers.find():
        if x["id"] == str(hostname):
            y = False
            break
    
    if y == True:
        cont = {"id":hostname}
        db.containers.insert_one(cont)

def give_containers():
    uf = db.containers.find();
    return uf


@app.route('/')
def hello():
    time.sleep()
    insert()
    redis.incr("counter")
    counter = redis.get("counter").decode("utf8")
    lel = give_containers()

    return """
    <body style="background-color:#0c0c0d; color:#ffffff; width:100%; height:100%;">

    <h1 style='text-align: center; color: white;'>   Currently being served by <label style="color:#fca532">{}<label> (V1) </h1>
    <p style="text-align: center;"> Total visits: <label style="color:#97fc32">{}<label> </p>
    <p style="text-align: center;"> Some previous containers: <label style="color:#32affc">{} {} {}<label> </p>
    </body>
    """.format(hostname,counter,lel[1]["id"],lel[2]["id"],lel[3]["id"])


if __name__ == '__main__':
    # time.sleep(5)

    app.run(host='0.0.0.0', port=8080)