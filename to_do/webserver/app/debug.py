from xml.etree import ElementTree
import time
#from time import gmtime, strftime

import argparse, urllib2, base64, json


import xmlparsing
import redisfunctions

def main():
  runninghour = '09'
  url = 'http://webservices.nextbus.com/service/publicXMLFeed?command=schedule&a=sf-muni&r=39'
  url2 = 'http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni'
  route = 39
  
  #if xmlparsing.get_times(url,runninghour,route):
  #  print 'transport running'
  #else:
  #  print 'transport not running'

  xmlparsing.get_routes(url2,runninghour)

if __name__ == "__main__": 
  #main()
  s='{"main" : {"aaa" : "10", "bbb" : [1,2,3]}}'
  print(xmlparsing.json2xml(json.loads(redisfunctions.getallStatistics())))
  #print(xmlparsing.json2xml(redisfunctions.getallStatistics()))
