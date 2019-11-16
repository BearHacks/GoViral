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
    
f = open("data/dataset/json/video_stats.json","w+")
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

i = 0
f.write("{\"videoStatistics\":[")
while i < len(arr):
    response = get_vid_stats_id("lLp8ybJER_Q")
    f.write((response))
    i = i + 1;  
f.write("]}")
f.close();