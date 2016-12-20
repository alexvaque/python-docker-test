# python-docker-test
Python NextBus API, running into docker-compose with proxycache and a redis storage

# Python+Multiple Docker containers (Docker Compose)


## Expose all NextBus endpoints in the NextBus API

using: 
localhost:80/service/*

## Special endpoints

/test -> return Hello World
/allrunning/<runninghour>
/isrunning/<runninghour>/<route>
/statistics/ -> return statistics in Json
/statistics/xml -> return statistics in XML format


running hour = [00,01,02,.23]
route        = http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni
