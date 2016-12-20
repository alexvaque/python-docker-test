# python-docker-test
Python NextBus API, running into docker-compose with proxycache and a redis storage

# Python+Multiple Docker containers (Docker Compose)


## HOW TO CREATE THE INFRASTRUCTURE

##### Main dependencies: Docker, Docker-compose v2
##### Tested on Linux Ubuntu 16.04 LTS
##### Technologies: Nginx, Python, Flask, Docker, Redis, HAproxy, Docker-compose

./run.sh 

Basically creates 3 docker builds and runs the docker compose after that exposes the app at "http://localhost:80/test"


## HTTP DEMO

### Expose all NextBus endpoints in the NextBus API
localhost:80/service/* 

### Special endpoints
 /test -> return Hello World

 "/allrunning/<hour>"          return bus that are not running at <runninghour>
 
 "/isrunning/<hour>/<route>"   return if the bus <route> is running or not at <runninghour>

 "/isrunning/<hour>/<minute>/<route>"

 "/statistics/"                       return statistics in Json
 
 "/statistics/xml"                    return statistics in XML format



	running hour = [00,01,02, .., 23]
	minute       = [00,01,02, ...,60]
	route        = http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni


Examples:

	At 12:XXh route 39
	> http://localhost/isrunning/12/39  

	At 12:30h route 39
	> http://localhost/isrunning/12/30/39  

	Proxy-server with cache
	> localhost/service/publicXMLFeed?command=routeList&a=sf-muni

	Routes that are not working at 12h ?
	> http://localhost/allrunning/12

	Statistics
	> http://localhost/statistics/

	Statistics with XML format
	> http://localhost/statistics/xml

## CODE INFORMATION

path: flask-index/app

	./config.py         -> Config files (redis  hostname, proxy hostname or direct url and port to use)
	./main.py           -> FLASK PROJECT with the MAIN functions


	./xmlparsing.py     -> Parsing the information and to get the information 
	./json2xml.py       -> class to convert json 2 xml
	./timeit.py         -> to save statistics
	./redisfunctions.py -> redis functions used to store the statistics into Redis

### HOW TO TEST THE CODE WITHOUT DOCKER

cd flask-index/app

flask-index/app/config.py 
	HOSTNAME  = 'webservices.nextbus.com'
	REDISHOST = 'localhost'

and run 

python main.py 

services is http://localhost:5000/test

## INFRAESTRUCUTURE INFORMATION

                        1 haproxy
                   /       |         \
      nginx+python    nginx-python    nginx-python
                                        
                              
        PROXY (nginx+proxycache)      REDIS
