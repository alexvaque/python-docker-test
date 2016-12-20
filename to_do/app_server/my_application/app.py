#!/usr/bin/env python
# Alex Vaque TEST 

#import Flask
from flask import Flask
from flask import abort, make_response
from flask import jsonify, request
import time
from flask import redirect, url_for

import urllib2
import json

import xmlparsing
import redisfunctions
import timeit

PORT=80

#url      = 'http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a=sf-muni&r=39'
#url2    = 'http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni'
#hostname = 'webservices.nextbus.com'
hostname = 'proxy:80'

app = Flask(__name__)



# Error management
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/test')
def hello():
    return "Hello World!"

# Extra:  
#@app.route('/', methods=['GET'])
#def get_extra():
#    return jsonify({'extra': extra})

@app.route('/isrunning/<int:runninghour>', methods=['GET'])
def get_more(runninghour):
    return runninghour  #get_routes(url2,runninghour)

@app.route('/allrunning/<runninghour>')
def get_all_no_routetime(runninghour):
    return xmlparsing.get_all_routes(hostname,runninghour)

@app.route('/isrunning/<runninghour>/<route>')
def get_no_routetime(runninghour,route):
    response = []
    running = xmlparsing.get_times(hostname,runninghour,route)
    response.append({'route': route, 'hourtime': runninghour,'running':running})
    return json.dumps(response)

#@app.route('/statistics/<format>')
#def statistics():
#    if format == 'xml':
#        return xmlparsing.json2xml(json.loads(redisfunctions.getallStatistics()))
#    else:
#        return redisfunctions.getallStatistics()

@app.route('/statistics/')
def statistics():
    return redisfunctions.getallStatistics()

@app.route('/statistics/xml/')
def statistics_xml():
    return xmlparsing.json2xml(json.loads(redisfunctions.getallStatistics()))


@app.route('/redirect/')
def redirect():
    #req = urllib2.Request(url2)
    #response = urllib2.urlopen(req) #(req,data)
    #html = response.read()
    #return html
    return redirect(url2,code=301)

if __name__ == "__main__":
    app.run()


