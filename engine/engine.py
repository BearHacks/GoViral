import csv
import pandas as pd
import numpy as np

names = [ "projectedViews", "viewCount", "likeCount","dislikeCount", "favoriteCount", "commentCount", "upTime"]

dataset = pd.read_csv('data/dataset/csv/videostats.csv', names=names)
df = dataset.drop(dataset.index[0])

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

print("enter views: ")
viewCount = input()
print("enter likeCount: ")
likeCount = input()
print("enter dislikeCount: ")
dislikeCount = input()
print("enter favoriteCount: ")
favoriteCount = input()
print("enter commentCount: ")
commentCount = input()
print("enter uptime(minutes): ")
upTime = input()

hi = [viewCount, likeCount, dislikeCount, favoriteCount, commentCount, upTime]
n = np.asarray(hi)

n = n.reshape(1, -1)
print(n)

pred = regressor.predict(n)

print(pred.flatten())