import csv
import pandas as pd
import numpy as np
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import requests
import json

names = [ "projectedViews", "viewCount", "likeCount","dislikeCount", "favoriteCount", "commentCount", "upTime"]

dataset = pd.read_csv('data/dataset/csv/videostats.csv', names=names)
df = dataset.drop(dataset.index[0])


API_TOKEN = ""
# demo link : https://www.youtube.com/watch?v=G5JBZk-DiQU
#print(df)

X = df.iloc[:, 1:7].values
y = df.iloc[:, :1].values
print(len(X[0]))
print(len(y[0]))
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

print(x_train)

regressor = LinearRegression()  
regressor.fit(x_train, y_train) #training the algorithm

#To retrieve the intercept:
#print(regressor.intercept_)
#For retrieving the slope:
#print(regressor.coef_)

y_pred = regressor.predict(x_test)
print(y_pred)
df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print("enter link to youtube video: ")
userinput = input()
listuser = userinput.split('=')

print(listuser[1])

response = requests.get("https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" +listuser[1]+ "&key=" + API_TOKEN)
#load response to dictionary obj
loaded_response = json.loads(response.content)

#print content of response
print(response.content)

upTime = 1000;
finalID = loaded_response["items"][0]["statistics"]
viewCount = finalID["viewCount"]
likeCount = finalID["likeCount"]
dislikeCount = finalID["dislikeCount"]
favoriteCount = finalID["favoriteCount"]
commentCount = finalID["commentCount"]
print("viewCount: " + viewCount)
print("likeCOunt: " + likeCount)
print("dislikeCount: " + dislikeCount)
print("favoriteCount: " + favoriteCount)
print("commentCount: " + commentCount)
print("uptime: " + str(upTime))


hi = [float(viewCount), float(likeCount), float(dislikeCount), float(favoriteCount), float(commentCount), float(upTime)]
n = np.asarray(hi)

n = n.reshape(1, -1)

pred = regressor.predict(n)

print(float(pred.flatten()))