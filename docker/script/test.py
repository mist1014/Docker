#! /bin/python3
import requests
import sys

url= sys.argv[1]
content = requests.get (url+'/favicon.ico',allow_redirects=True)
open('/usr/local/bin/favicon.ico', 'wb').write(content.content)

