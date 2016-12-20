import redis
import json
import pprint

r_server = redis.Redis('localhost')    #this line creates a new Redis object and connects to our redis server


def incrCounter(type,time):
    if time < 2:
        return r_server.incr('query.'+str(type)+"")   #we increase the key value by 1, has to be int
    else:
        return r_server.incr('slow.query.'+str(type)+"")


def getvarStatistics():
    return r_server.keys()

def getallStatistics():
    response = []
    for key in r_server.scan_iter():
        #print key, r_server.get(key) 
        response.append({'query': key, 'times': r_server.get(key)})
    return json.dumps(response)   

def getallStatistics2():
    for key in r_server.scan_iter():
        print key, r_server.get(key)    
    return '0'  
