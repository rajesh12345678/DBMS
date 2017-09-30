from py2neo import Graph, Node, Relationship
import json
import os



def descriptionCompare(description1,description2):
	word_description1 = description1.split()
	word_description2 = description2.split()
	count = len(set(word_description2)&set(word_description1))
	return count

def tagsCompare(tags1,tags2):
	return len(set(tags1)&set(tags2))


graph = Graph(password="dipika")
print("yolo")

arrayjson = []
filelist = os.listdir("/home/paritosh/Desktop/Database Lab/POST_ASS2/test")
for i in range(len(filelist)):
	filelist[i]="/home/paritosh/Desktop/Database Lab/POST_ASS2/test/"+filelist[i]
	# print(filelist[i])
	page = open(filelist[i],"r")
	parsed = json.loads(page.read())
	arrayjson.append(parsed)

for i in range(len(arrayjson)):
	arraystring = arrayjson[i]['videoInfo']['statistics']
	a = Node("Youtube",name=arrayjson[i]['videoInfo']['id'],commentCount=arraystring['commentCount'],viewCount=arraystring['viewCount'],favoriteCount=arraystring['favoriteCount'],dislikeCount=arraystring['dislikeCount'],likeCount=int(arraystring['likeCount']))
	graph.create(a)
	print("yolo "+str(i))
	# print(arrayjson[i]['videoInfo']['id'])

for i in range(len(arrayjson)):
	element = arrayjson[i]
	for j in range(i-1,-1,-1):
		if arrayjson[j]['videoInfo']['snippet']['channelId'] != element['videoInfo']['snippet']['channelId']:
			a = graph.find_one("Youtube",property_key='name', property_value=element['videoInfo']['id'])
			b = graph.find_one("Youtube",property_key='name', property_value=arrayjson[j]['videoInfo']['id'])
			channelRelation = Relationship(a,"Same Channel",b)
			graph.create(channelRelation)
		Count=descriptionCompare(arrayjson[i]['videoInfo']['snippet']['description'],arrayjson[j]['videoInfo']['snippet']['description'])
		if Count !=0:
			a = graph.find_one("Youtube",property_key='name', property_value=element['videoInfo']['id'])
			b = graph.find_one("Youtube",property_key='name', property_value=arrayjson[j]['videoInfo']['id'])
			DescriptionRelation = Relationship(a,"Matching Description",b,weightage=Count)
			graph.create(DescriptionRelation)

		if 'tags' in arrayjson[i]['videoInfo']['snippet'] and 'tags' in arrayjson[j]['videoInfo']['snippet']:
			tagCount = tagsCompare(arrayjson[i]['videoInfo']['snippet']['tags'], arrayjson[j]['videoInfo']['snippet']['tags'])
			if tagCount !=0:
				a = graph.find_one("Youtube",property_key='name', property_value=element['videoInfo']['id'])
				b = graph.find_one("Youtube",property_key='name', property_value=arrayjson[j]['videoInfo']['id'])
				TagRelation = Relationship(a,"Matching Tags",b,weightage=tagCount)
				graph.create(TagRelation)
 
	print("yolo "+str(i))
print("finish")
