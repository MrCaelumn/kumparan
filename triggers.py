#!/usr/bin/env python

from flask import Flask, jsonify, request
from models import news
import time

app = Flask(__name__)

instanceNews = news.News()

# LIST FOR ALL,Topics, Status
@app.route('/list/news', methods=['GET'])
def getListNews():
    print("FUNCTION getListNews invoked")
    data = {}
    if request.args.get('topics'):
        data['topics'] = request.args.get('topics')
    elif request.args.get('status'):
        data['status'] = request.args.get('status')
    else:
        data['all'] = True

    res = instanceNews.findList(data)

    return jsonify(res)


@app.route('/remove/news/<idKey>', methods=['POST'])
def deleteNewsById(idKey):
    print(idKey)
    print("FUNCTION deleteNewsByStatus invoked")


    res = instanceNews.deleteOneByID(idKey)

    return res


@app.route('/remove/topics/<idKey>/<topics>', methods=['POST'])
def removeTopicsFromNews(idKey,topics):
    print(idKey)
    print(topics)
    print("FUNCTION removeTopicsFromNews invoked")

    arr = []
    if ',' in topics:
        topics = topics.split(',')
    else:
        arr.append(topics)
        topics = arr

    msg = {
        "idKey" : idKey,
        "topics" : topics,
    }
    res = instanceNews.deleteTopicFromNews(msg)
    return res


@app.route('/add/news', methods=['POST'])
def addNews():

    #using params
    idKey = request.args.get('idKey')
    title = request.args.get('title')
    author = request.args.get('author')
    topics = request.args.get('topics')
    arr = []
    if ',' in topics:
        topics = topics.split(',')
    else:
        arr.append(topics)
        topics = arr


    status = request.args.get('status')
    print("FUNCTION addNews invoked")
    date = int(time.time())
    msg = {
        "idKey" : idKey,
        "title" : title,
        "author" : author,
        "topics" : topics,
        "createdon" : date,
        "status" : status,
    }
    res =  instanceNews.createNews(msg)

    return res

@app.route('/add/topics/<idKey>/<topics>', methods=['POST'])
def addTopicsToNews(idKey,topics):
    print("FUNCTION addTopicsToNews invoked")
    arr = []
    if ',' in topics:
        topics = topics.split(',')
    else:
        arr.append(topics)
        topics = arr

    msg = {
        "idKey" : idKey,
        "topics" : topics,
    }
    res = instanceNews.addTopicsInNews(msg)
    return res

@app.route('/update/news', methods=['POST'])
def updateNews():
    msg = {}

    #using params

    if request.args.get('idKey') :
        msg["idKey"] = request.args.get('idKey')
        msg["modifiedon"] = int(time.time())
        if request.args.get('title') :
            msg["title"] = request.args.get('title')
        if request.args.get('author') :
            msg["author"] = request.args.get('author')
        if request.args.get('topics') :
            topics = request.args.get('topics')
            arr = []
            if ',' in topics:
                topics = topics.split(',')
            else:
                arr.append(topics)
                topics = arr
            msg["topics"] = topics
        if request.args.get('status') :
            msg["status"] = request.args.get('status')


        if len(msg.keys()) > 2:

            print("FUNCTION updateNews invoked")

            res =  instanceNews.updateNews(msg)

            return res
        else :
            msg = {
                "status" : False,
                "message" : "No Changes because you arent set a field or more field to update"
            }
            return jsonify(msg)

    else:
        msg = {
            "status" : False,
            "message" : "ID cannot Null"
        }
        return jsonify(msg)

if __name__ == '__main__':
    # running in localhost
    app.run(host='127.0.0.1', port=3007,debug=True)
