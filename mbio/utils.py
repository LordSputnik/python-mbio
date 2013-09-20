import urllib2
import json

json_str = '{"country":"GB","text-representation":{"script":"Latn","language":"eng"},"status":"Official","date":"1987-02-26","cover-art-archive":{"count":3,"front":true,"artwork":true,"back":true,"darkened":false},"barcode":"077774643627","release-events":[{"area":{"iso_3166_3_codes":[],"sort-name":"United Kingdom","name":"United Kingdom","id":"8a754a16-0027-3a29-b6d7-2b40ea0481ed","iso_3166_2_codes":[],"iso_3166_1_codes":["GB"]},"date":"1987-02-26"}],"packaging":null,"disambiguation":"George Martin mono remaster","id":"479d8f1b-daaf-3eac-9b69-b464cb239660","title":"With The Beatles","asin":"B000002UAC","quality":"normal"}'

def get_json(url):
    #response = urllib2.urlopen(url)
    return json.loads(json_str)
