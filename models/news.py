from pymongo import MongoClient
from flask import jsonify
from bson.json_util import dumps


class News(object):
    """docstring for ."""
    def __init__(self):
        # set your host ip
        # self.client = MongoClient("mongodb://<host IP>:27017")
        self.client = MongoClient()
        self.db = self.client.kumparan

    def createNews(self,data):
        print("Function createNews invoked from Class News")

        # print(data['idKey'])
        # print(data['title'])
        # print(data['author'])
        # print(data['topics'])
        # print(data['time'])
        # print(data['status'])
        try:

            self.db.news.insert_one(data).inserted_id
            response = {
                "status" : True,
                "message" : "Data Inserted"
            }
            return jsonify(response)
        except Exception as e:
            response = {
                "status" : False,
                "message" : str(e)
            }
            return jsonify(response)

    def findList(self,data):
        listNews = None
        try:
            print(data)
            if 'all' in data:
                listNews = self.db.news.find()
            else:
                listNews = self.db.news.find(data)

            # for a in listNews:
            #     print(a)

            response = {
                "status" : True,
                "message" : "Data Find",
            }
            response['result'] = dumps(listNews)

            return response
        except Exception as e:
            response = {
                "status" : False,
                "message" : str(e)
            }
            return jsonify(response)

    def deleteOneByID(self,data):

        try:
            self.db.news.delete_one({"idKey": data})
            response = {
                "status" : True,
                "message" : "Data Deleted",
                "idKey" : data
            }

            return jsonify(response)
        except Exception as e:
            response = {
                "status" : False,
                "message" : str(e)
            }
            return jsonify(response)


    def deleteTopicFromNews(self,data):
        try:
            self.db.news.update( { "idKey": data['idKey'] }, { "$pull": { "topics": { "$in" : data['topics'] } } } )
            response = {
                "status" : True,
                "message" : "Topics Removed",
            }
            response['data'] = data

            return jsonify(response)
        except Exception as e:
            response = {
                "status" : False,
                "message" : str(e)
            }
            return jsonify(response)

    def addTopicsInNews(self,data):
        try:
            self.db.news.update( { "idKey": data['idKey'] }, { "$push": { "topics": {"$each" : data['topics'] } } } )
            response = {
                "status" : True,
                "message" : "Topics Added",
            }
            response['data'] = data

            return jsonify(response)
        except Exception as e:
            response = {
                "status" : False,
                "message" : str(e)
            }
            return jsonify(response)

    def updateNews(self,data):
        print("Function updateNews invoked from Class News")

        try:

            self.db.news.update_one({"idKey":data["idKey"]},{"$set": data })
            response = {
                "status" : True,
                "message" : "Data Updated"
            }
            return jsonify(response)
        except Exception as e:
            response = {
                "status" : False,
                "message" : str(e)
            }
            return jsonify(response)
