from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort 

from random import randint

import psycopg2

med_count = 25 
workout_count = 50 
yoga_count = 50 




app = Flask(__name__)
api = Api(app)


class med(Resource):
    def get(self): 
        conn = psycopg2.connect(database="YoutubeVid", user="postgres", password="1229", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        num = randint(1, med_count)
        
        query = "select * from Meditation where id = %s"
        cur.execute(query, (num,))
        vid = cur.fetchone()
        cur.close()
        conn.close()
        return {"videoID" : vid[1]}, 200


class yoga(Resource):
    def get(self): 
        conn = psycopg2.connect(database="YoutubeVid", user="postgres", password="1229", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        num = randint(1, yoga_count)
      
        query = "select * from Yoga where id = %s"
        cur.execute(query, (num,))
        vid = cur.fetchone()
        cur.close()
        conn.close()
        return {"videoID" : vid[1]}, 200

class workout(Resource):
    def get(self): 
        conn = psycopg2.connect(database="YoutubeVid", user="postgres", password="1229", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        num = randint(1, workout_count)
      
        query = "select * from Workout where id = %s"
        cur.execute(query, (num,))
        vid = cur.fetchone()
        cur.close()
        conn.close()
        return {"videoID" : vid[1]}, 200

api.add_resource(med, "/api/med")
api.add_resource(yoga, "/api/yoga")
api.add_resource(workout, "/api/workout")


if __name__ == "__main__":
    app.run(debug=True)