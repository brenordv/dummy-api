# Dummy API
## What it is and what is it good for?
This simple webservice have a few methods that helps me play around when i want to create or test the process of 
making post and get requests.

There is no real database connection, authentication or any of that fancy stuff. 

## Methods
### Ping
```
[GET, POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/ping
```
This method will just return the string "Ping? Pong!"


### Echo
```
[POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/echo
```
As the name suggests, this method will return anything passed to it. You post "bacon" and echo will return "bacon".
Please, don't try anything funny. I just decode requests.data and return it.


### Echo Args
```
[POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/echoargs
```
As the name suggests, this method will return anything passed to it via querystring. 


### Hash me 
```
[GET, POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/hashme
```
Will return a random SHA256 hash.


### Users 
```
[GET] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/users
[GET] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/users?&format=json
[GET] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/users?&format=xml
```
This method will return a list of users from my dummy database. The default return format is JSON, but you can use the
query argument "format" to specify if you want a XML instead.


### Catalog 
```
[GET] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/catalog
[GET] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/catalog?&format=json
[GET] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/catalog?&format=xml
```
This method will return a list of products from my dummy database. This list was used in a post where i showed how 
to manipulate XML with XPATH in Python. 
Post: http://raccoon.ninja/pt/dev-pt/usando-xpath-para-manipular-xml-python/
(I have not created this database. Due credits are listed in the post.)

The default return format is JSON, but you can use the query argument "format" to specify if you want a XML instead.


### CD Catalog 
```
[GET, POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/cdcatalog
[GET, POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/cdcatalog?&format=json
[GET, POST] https://raccoon-ninja-dummy-api.herokuapp.com/api/v1/cdcatalog?&format=xml
```
This method will return a list of CDs from my dummy database. This list was used in a post where i showed how 
to manipulate XML using Python. 
http://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/
(I have not created this database. Due credits are listed in the post.)

The default return format is JSON, but you can use the query argument "format" to specify if you want a XML instead.


## Who can use it?
Anyone... for anything. Go nuts. This is not THAT useful.