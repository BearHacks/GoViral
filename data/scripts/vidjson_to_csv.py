import csv
import json
import requests
import datetime

API_TOKEN = ''
API_URL_BASE = 'https://www.googleapis.com/youtube/v3'

fr = open("data/dataset/json/videostats.json","r")
f = open("data/dataset/csv/videostats.csv","w+")

f.write("projectedViews,viewCount,likeCount,dislikeCount,favoriteCount,commentCount,upTime\n")

videoStatsRaw = fr.read()
videoStatistics = json.loads(videoStatsRaw)

# response = requests.get(API_URL_BASE + "/videos?part=snippet&id=" + "0Hdl5DIs8y4" + "&key=" + API_TOKEN) 
# python_response = json.loads(response.content)

# #publishedAt = python_response["items"]
# publishedAt = python_response["items"][0]["snippet"]["publishedAt"]
# print(publishedAt)

i = 0
while i < len(videoStatistics["videoStatistics"]):
    try:
        idstats = videoStatistics["videoStatistics"][i]["items"][0]["id"]
        print(idstats)
        viewCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["viewCount"]
        likeCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["likeCount"]
        dislikeCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["dislikeCount"]
        favoriteCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["viewCount"]
        commentCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["commentCount"]
        response = requests.get(API_URL_BASE + "/videos?part=snippet&id=" + idstats + "&key=" + API_TOKEN) 
        python_response = json.loads(response.content)
        publishedAt = python_response["items"][0]["snippet"]["publishedAt"]
        year = publishedAt[0:4]
        month = publishedAt[5:7]
        day = publishedAt[8:10]
        # year = 2010
        # month = 10
        # day = 20

        publishedTime  = datetime.datetime(int(year), int(month), int(day))
        timesince = datetime.datetime.today() - publishedTime
        minutessince = int(timesince.total_seconds() / 60)
        print(minutessince)
        f.write(str(float(viewCount)) + "," + "0.0" + "," + str(float(likeCount)) + "," +  str(float(dislikeCount)) + "," + str(float(favoriteCount)) + "," + str(float(commentCount)) + "," + str(float(minutessince)) + "\n")
    except:
        i = i
    i = i + 1
f.close()
#              python C:\Users\Armeet Singh Jatyani\Documents\Development\GitHub\GoViral\data\scripts\vidjson_to_csv.py