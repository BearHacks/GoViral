import os
import json
import requests
import time

API_TOKEN = ''
API_URL_BASE = 'https://www.googleapis.com/youtube/v3'

TIME_SLEEP = 0;

def get_vid_stats_id(vid_id):
    #full response will store json output
    full_response = ''

    response = requests.get(API_URL_BASE + "/videos?part=statistics&id=" + vid_id + "&key=" + API_TOKEN)
    #load response to dictionary obj
    loaded_response = json.loads(response.content)

    #print content of response
    print(response.content)

    #append to the full_response
    full_response = full_response + json.dumps(loaded_response) + ","
    return full_response;
    
f = open("data/dataset/json/videostats.json","w+")
jsonfile = open("data/dataset/json/response.json","r")
videos = json.loads(jsonfile.read())

i = 0
j = 0

f.write("{\"videoStatistics\":[")

while(i < len(videos["videos"])):
    while(j < len(videos["videos"][i]["items"])):
        print("i: " + str(i))
        print("j: " + str(j))
        try:
            id = videos["videos"][i]["items"][j]["id"]["videoId"]
            response = get_vid_stats_id(str(id))
            f.write(response)
        except:
            break;
        j = j + 1
    i = i + 1
    j = 0
f.write("]}")
f.close()