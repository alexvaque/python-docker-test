# python-docker-test
Python NextBus API, running into docker-compose with proxycache and a redis storage

# Python+Multiple Docker containers (Docker Compose)


## CREATE THE INFRAESTRUCTURE

### Dependencies Docker, Docker-compose 
### Tested on Ubuntu 16.04 LTS

./run.sh 

basicly creates 3 docker builds and runs the docker compose
after that
localhost:80/test 

and:

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



## CODE INFORMATION

path: flask-index/app

	./config.py         -> Config files (redis  hostname, proxy hostname or direct url and port to use)
	./main.py           -> FLASK PROJECT with the MAIN functions


	./xmlparsing.py     -> Parsing the information and to get the information 
	./json2xml.py       -> class to convert json 2 xml
	./timeit.py         -> to save statistics
	./redisfunctions.py -> redis functions used to store the statistics into Redis


## INFRAESTRUCUTURE INFORMATION

                        1 haproxy
                   /       |         \
      nginx+python    nginx-python    nginx-python
                                        
                              
        PROXY (nginx+proxycache)      REDIS
