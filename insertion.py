from glob import iglob
import os.path
import pymongo
import json
from pymongo import MongoClient
from pprint import pprint

connection = MongoClient()
db = connection.test
videos = db.videos

#result1 = db.videos.create_index([("videoInfo.snippet.tags","text")])
search_string = "Modi"
#for video in videos.find({"$text": {"$search": search_string}}):
#	print(video)
result = db.videos.find({"$text": {"$search": search_string}})
#pprint(result[0])
fname = "results.txt"
file_handle = open(fname,"w")
for item in result:
	print(item['videoInfo']['id'])
	file_handle.write(item['videoInfo']['id'])
	file_handle.write("\n")
