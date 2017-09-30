from glob import iglob
import os.path
import pymongo
import json
from pymongo import MongoClient
from pprint import pprint
#file_handle = openn("results.txt","r")
connection = MongoClient()
db = connection.test
videos = db.videos
with open("results.txt") as file_handle:
	for line in file_handle:
		line = line.strip('\n')
		video_id = line
		result = db.videos.find({"videoInfo.id":video_id})
		result = result[0]
		print(result['videoInfo']['snippet']['title'])
