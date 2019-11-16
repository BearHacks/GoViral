import os
import json
import requests
import time

API_TOKEN = ''
API_URL_BASE = 'https://www.googleapis.com/youtube/v3'

TIME_SLEEP = 0;

def search_vids_keyword(search_keyword, starting_page_token, max_results):
    #full response will store json output
    full_response = ''
    #next page token
    next_page_token = starting_page_token

    #loop through all tokens
    while next_page_token != 'end':
        #make request
        response = requests.get(API_URL_BASE + "/search?part=id&prettyPrint=true&maxResults=" + max_results + "&q=" + search_keyword + "&key=" + API_TOKEN + "&pageToken=" + next_page_token + "&type=video")
        #load response to dictionary obj
        loaded_response = json.loads(response.content)

        #print content of response
        print(response.content)

        #try to go the next page
        try:
            next_page_token = loaded_response['nextPageToken']
        except:
            next_page_token = 'end' 
        print(next_page_token)

        #append to the full_response
        full_response = full_response + json.dumps(loaded_response) + ","
    return full_response;
    
f = open("data/dataset/json/response.json","w+")
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

i = 0
f.write("{\"videos\":[")
while i < len(arr):
    response = search_vids_keyword(arr[i], "", "50");
    f.write((response))
    i = i + 1;  
f.write("]}")
f.close();