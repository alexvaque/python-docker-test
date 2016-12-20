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
/allrunning/<runninghour>          return bus that are not running at <runninghour>
/isrunning/<runninghour>/<route>   return if the bus <route> is running or not at <runninghour>
/statistics/                       return statistics in Json
/statistics/xml                    return statistics in XML format


running hour = [00,01,02, .., 23]
route        = http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni
