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

port = config.PORT
hostname = config.HOSTNAME


# Error management
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/test')
def hello():
    return "Hello World!"


# Extra:
# @app.route('/', methods=['GET'])
# def get_extra():
#    return jsonify({'extra': extra})

@app.route('/isrunning/<int:runninghour>', methods=['GET'])
def get_more(runninghour):
    return runninghour  # get_routes(url2,runninghour)


@app.route('/allrunning/<runninghour>')
def get_all_no_routetime(runninghour):
    return xmlparsing.get_all_routes(hostname, runninghour)


@app.route('/isrunning/<runninghour>/<route>')
def get_no_routetime(runninghour, route):
    response = []
    running = xmlparsing.get_times(hostname, runninghour, route)
    response.append({'route': route, 'hourtime': runninghour, 'running': running})
    return json.dumps(response)


# @app.route('/statistics/<format>')
# def statistics():
#    if format == 'xml':
#        return xmlparsing.json2xml(json.loads(redisfunctions.getallStatistics()))
#    else:
#        return redisfunctions.getallStatistics()

@app.route('/statistics/')
def statistics():
    return redisfunctions.getallStatistics()


@app.route('/statistics/xml/')
def statistics_xml():
    converter = json2xml.Json2XmlConverter()
    return converter.convert(json.loads(redisfunctions.getallStatistics()))


if __name__ == "__main__":
    app.run()  # DEBUG MODE WITHOUT NGINX
    # app.run(host='0.0.0.0', debug=True, port=PORT)
