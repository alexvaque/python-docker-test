#!/usr/bin/env python
# Alex Vaque TEST 

from flask import Flask
from flask import abort, make_response, jsonify, request, redirect, url_for
import urllib2, json
import xmlparsing
import json2xml
import redisfunctions
import time
import timeit
import config

app = Flask(__name__)

port     = config.PORT
hostname = config.HOSTNAME


# Error management
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/test')
def hello():
    return "Hello API!"


@app.route('/allrunning/<runninghour>')
def get_all_no_routetime(runninghour):
    check_input_data(runninghour)
    return xmlparsing.get_all_routes(hostname, runninghour)


@app.route('/isrunning/<runninghour>/<route>')
def get_no_routetime(runninghour, route):
    check_input_data(runninghour)
    response = []
    running = xmlparsing.get_times(hostname, runninghour, route)
    response.append({'route': route, 'hourtime': runninghour, 'running': running})
    return json.dumps(response)


@app.route('/isrunning/<runninghour>/<runningminute>/<route>')
def get_no_routetime_minutes(runninghour, runningminute, route):
    check_input_data(runninghour)
    check_input_data(runningminute)
    response = []
    running = xmlparsing.get_times_minutes(hostname, runninghour, runningminute, route)
    response.append({'route': route, 'hourtime': runninghour, 'running': running})
    return json.dumps(response)


@app.route('/statistics/')
def statistics():
    return redisfunctions.getallStatistics()


@app.route('/statistics/xml/')
def statistics_xml():
    converter = json2xml.Json2XmlConverter()
    return converter.convert(json.loads(redisfunctions.getallStatistics()))

#Controling the Input 
def check_input_data(input_data):
    if not input_data.isnumeric():
        #raise Exception('Invalid Input, use hour or minute digits')
        print 'Invalid Input, use hour or minute digits'
        return 'Invalid Input, use hour or minute digits'


if __name__ == "__main__":
    app.run()           # DEBUG MODE WITHOUT NGINX
    #app.run(host='0.0.0.0', debug=True, port=port)
