import csv
import json
fr = open("data/dataset/json/videostats.json","r")
f = open("data/dataset/csv/videostats.csv","w+")

f.write("viewCount,likeCount,dislikeCount,favoriteCount,commentCount\n")

videoStatsRaw = fr.read()
videoStatistics = json.loads(videoStatsRaw)

# print(videoStatistics["videoStatistics"][1000]["items"][0]["statistics"])

i = 0
while i < len(videoStatistics["videoStatistics"]):
    try:
        viewCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["viewCount"]
        likeCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["likeCount"]
        dislikeCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["dislikeCount"]
        favoriteCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["viewCount"]
        commentCount = videoStatistics["videoStatistics"][i]["items"][0]["statistics"]["commentCount"]
        f.write(viewCount + "," + likeCount + "," + dislikeCount + "," + favoriteCount + "," + commentCount + "\n")
    except:
        f.write("-1,-1,-1,-1,-1\n")        
    i = i + 1
f.close()