import hmac, base64, struct, hashlib, time
import crypt, getpass, pwd
import urllib
import json
import datetime
from urllib import request
import feedparser

locu_api = 'YOUR KEY HERE'
#import feedparser
class rssapi:
    def getfeed(url):
        #api_key = locu_api
        #url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
        #url2 = 'https://jsonplaceholder.typicode.com/posts'
        #locality = query.replace(' ', '%20')
        #final_url = url + "&locality=" + locality + "&category=restaurant"
        #final_url = url + "&category=restaurant"
    #    json_obj = request.urlopen(url2)
    #    data = json.load(json_obj)

        #for item in data['objects']:
            #print(item['name'], item['phone']
        return "Works!"
