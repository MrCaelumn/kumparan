# Flask (Python) CRUD API

Kumparan Test

### Prerequisites

* MongoDB
* Python 2.7
* Flask
* PyMongo



### Installing

* [MongoDB](https://docs.mongodb.com/manual/installation/)
* [Python 2.7](https://www.python.org/downloads/)
* [Flask](pip install Flask)
* [PyMongo](pip install PyMongo)



## Running the tests

* you can run like this - python triggers.py

## Field in MongoDB
* idKey
* title
* author
* topics
* createdon
* status
* modifiedon

## Spec API

* localhost:5000/api/v1 - Testing Connection Method ALL
* localhost:5000/api/v1/add/news?idKey=8&topics=nature,ekonomi&title=Raja Empat Menjadi Pusat Wisata Papua&status=publish&author=Adit - Add News Method POST
* localhost:5000/api/v1/list/news - get All News Method GET
* localhost:5000/api/v1/list/news?topics=<topics> - get News By Topics Method GET
* localhost:5000/api/v1/list/news?status=<status> - get News By Status Method GET
* localhost:5000/api/v1/remove/news/<idKey> - remove News By idKey Method POST
* localhost:5000/api/v1/remove/topics/<idKey>/<topics> - remove Topics in news Method POST
* localhost:5000/api/v1/add/topics/<idKey>/<topics> - add Topics in news Method POST
* localhost:5000/api/v1/update/news?idKey=8&topics=nature,ekonomi&title=Raja Empat Menjadi Pusat Wisata Papua&status=publish&author=Adit - add Topics in news Method POST
