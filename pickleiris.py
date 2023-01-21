import requests
import pickle
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# data = requests.get(url).text
# file = "mydata.pkl"
# fileobj = open(file, "wb")
# dataset = data.split("\n")
# pickle.dump(dataset, fileobj)
file = "mydata.pkl"
fileobj = open(file, 'rb')
mydata = pickle.load(fileobj)
print(mydata)
