from xml.etree import ElementTree
import argparse, urllib2, base64, json
import time
import timeit
import main


# class xmlparsing:
# def __init__(self):
#    self.classType   = 'xmlparsing'

@timeit.timeit
def get_url(url):
    # Specify the url
    try:
        request = urllib2.Request(url)
    except IOError, e:
        print "ERROR: ", e

    # Sends the request and catches the response
    response = urllib2.urlopen(request)
    # Extracts the response
    html = response.read()
    return html


@timeit.timeit
def get_times(hostname, runninghour, route):
    print "< Route %s - hour %s " % (route, runninghour)

    try:
        url = "http://" + str(hostname) + "/service/publicXMLFeed?command=schedule&a=sf-muni&r=" + str(route) + ""
        tree = ElementTree.parse(urllib2.urlopen(url))
    except IOError, e:
        print "ERROR Connecting to the endpoint: ", e

    for node in tree.iter():
        hour = str(node.get('epochTime'))
        if hour != -1 and hour != 'None':
            hour2 = time.strftime("%H", time.gmtime(int(hour) / 1000))
            # print "Epoch Time %s - Hour %s Running Hour %s " % (hour, hour2, runninghour)
            if hour2 == runninghour:
                print "running>"
                return True
    print "not running>"
    return False

@timeit.timeit
def get_times_minutes(hostname, runninghour, runningminute, route):
    print "< Route %s - hour %s minute %s " % (route, runninghour, runningminute)
    is_running = False
    minutelist = []
    is_between_max = -1 
    is_between_min = -1
    try:
        url = "http://" + str(hostname) + "/service/publicXMLFeed?command=schedule&a=sf-muni&r=" + str(route) + ""
        tree = ElementTree.parse(urllib2.urlopen(url))
    except IOError, e:
        print "ERROR Connecting to the endpoint: ", e

    for node in tree.iter():
        hour = str(node.get('epochTime'))
        if hour != -1 and hour != 'None':
            hour2  = time.strftime("%H", time.gmtime(int(hour) / 1000))
            minute = time.strftime("%M", time.gmtime(int(hour) / 1000)) 
            print "Epoch Time %s - Hour %s Running Hour %s Min %s " % (hour, hour2, runninghour, minute)
            if hour2 == runninghour:
                minutelist.append(int(minute))
                print "MAX %s" % max(minutelist)
                print "MIN %s" % min(minutelist)
                #is_running = True
                if minute >= min(minutelist) and minute < max(minutelist):
                  print "running>"
                  return True
                
    print "not running>"
    return is_running



@timeit.timeit
def get_all_routes(hostname, runninghour):
    response = []

    try:
        url = 'http://' + hostname + '/service/publicXMLFeed?command=routeList&a=sf-muni'
        tree = ElementTree.parse(urllib2.urlopen(url))
    except IOError, e:
        print "ERROR Connecting to the endpoint ", e

    for node in tree.iter():
        routes = str(node.get('tag'))
        if routes != -1 and routes != 'None':
            if not get_times(hostname, runninghour, routes):
                print 'Route %s not trunning' % routes
                response.append({'route': routes, 'hourtime': runninghour, 'running': 'False'})
    return json.dumps(response)


