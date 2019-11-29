## Dataset
data/dataset/csv/videostats.csv -> final output file (for machine learning model training)
data/dataset/json/response.json -> all search results
data/dataset/json/videostats.json -> all stats for videos (final json before conversion to csv)

## Scripts
data/scripts/get_channel_data.py -> fetch all search results into response.json
data/scripts/get_vid_stats.py -> fetch vid stats into videostats.json
data/scripts/vidsjson_to_csv.py -> convert videostats.json to videostats.csv 