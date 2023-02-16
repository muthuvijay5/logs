from django.shortcuts import render
import pymongo

def viewlogs(request):
    connection = pymongo.MongoClient("mongodb://localhost:27017/")
    db = connection["logs"]
    collection = db["errors_and_exceptions"]
    response = collection.find({})
    docs = list(response)
    for i in range(len(docs)):
        docs[i]["id"] = docs[i]["_id"]
        del docs[i]["_id"]
    
    return render(request, 'viewlogs.html', {"docs": docs})
