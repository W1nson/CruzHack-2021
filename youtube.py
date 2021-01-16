


import psycopg2
from apiclient.discovery import build
import json



# high-intensity workout
# meditation
# yoga
api_key = "AIzaSyAyXvlnRix4Dnd9OhK5J4IUUUGZvgHwMNU"
youtube = build('youtube', 'v3', developerKey=api_key)


def import_Yoga(cur):
    cur.execute('''CREATE TABLE Yoga
        (ID INT PRIMARY KEY     NOT NULL,
        VideoId           TEXT    NOT NULL,
        Title    TEXT    NOT NULL
        );''')

    res = youtube.search().list(part='snippet', eventType='completed',q='5 min yoga',type='video',videoDuration='short', relevanceLanguage='en',maxResults=50).execute() 
    count= 1
    for item in res['items']:
        print(item['snippet']['title'])
        print(item['id']['videoId'])
        cur.execute("INSERT INTO Yoga (ID, VideoId, Title) VALUES (%s, %s, %s)", (count, item['id']['videoId'], item['snippet']['title']))
        count += 1

def import_Meditation(cur):
    cur.execute('''CREATE TABLE Meditation
       (ID INT PRIMARY KEY     NOT NULL,
       VideoId           TEXT    NOT NULL,
       Title    TEXT    NOT NULL
       );''')

    res = youtube.search().list(part='snippet', relevanceLanguage='en', q='5 min guided meditation',type='video',videoDuration='short', maxResults=25).execute() 
    count= 1
    for item in res['items']:
        print(item['snippet']['title'])
        print(item['id']['videoId'])
        cur.execute("INSERT INTO Meditation (ID, VideoId, Title) VALUES (%s, %s, %s)", (count, item['id']['videoId'], item['snippet']['title']))
        count += 1 

def import_Workout(cur):

    cur.execute('''CREATE TABLE Workout
       (ID INT PRIMARY KEY     NOT NULL,
       VideoId           TEXT    NOT NULL,
       Title    TEXT    NOT NULL
       );''')

    res = youtube.search().list(part='snippet', eventType='completed', relevanceLanguage='en', q='5 min high intensity workout',type='video',videoDuration='short', maxResults=50).execute() 
    count= 1
    for item in res['items']:
        print(item['snippet']['title'])
        print(item['id']['videoId'])
        cur.execute("INSERT INTO Workout (ID, VideoId, Title) VALUES (%s, %s, %s)", (count, item['id']['videoId'], item['snippet']['title']))
        count += 1


def main():
    
    conn = psycopg2.connect(database="YoutubeVid", user="postgres", password="1229", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    #import_Yoga(cur)
    import_Meditation(cur)
    #import_Workout(cur)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
    