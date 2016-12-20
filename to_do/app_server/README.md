# Technical Test 1 #
## Deploying and running on docker ##
First of all you will need to clone the repo :)
```
git clone https://github.com/temp-omarti/test-1.git
```
When you have the repo locally build the image
```
cd test-1
docker build -t nginx_test .
```
And run it! :)
```
docker run -d -p 80 nginx_test
```
To access with http you will have to know the mapped port:
```
docker ps -l
# take the name, for example reverent_poincare and look at the assignated port
docker port reverent_poincare
```
With this port and the IP you can start doing requests to your API.
http://$IP:$port

The URL is protected by basic auth, the user/password is test/test

## Testing with the api_requester script ##
```
usage: api_requester.py [-h] [-r URL] [-p PASSWORD] [-u USERNAME]

optional arguments:
  -h, --help   show this help message and exit
  -r URL       Url of the API - default value http://localhost/
  -p PASSWORD  Password of the basic auth user - default: test
  -u USERNAME  Username of the basic auth - default: test
```

Run the api_requester.py script with the parameters, if you have ran
docker like the example the port on the local machine won't be 80
, if for example, it's the 49153 an usage example will be:
```
python api_requester.py -r http://localhost:49153/ -p test -u test
```
The api_requester script has been optimized to only do a request to 
get all the servers and not doing one request for every server

Enjoy ;)
