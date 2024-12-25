# http://www.compjour.org/tutorials/intro-to-python-requests-and-json/
import json

import requests

# url1 = 'https://status.github.com/api/status.json'
url1 = 'https://www.githubstatus.com/api/v2/components.json'
url2 = 'http://ip.jsontest.com/'


def headers(url):
    resp = requests.get(url)
    print('TYPE', type(resp))
    txt = resp.text
    print('LEN', len(txt))
    print('RESP.OK', resp.ok)
    print('RESP.STATUS_CODE', resp.status_code)
    # print('CONTENT-TYPE', resp.headers['Set-Cookie'])  # KeyError: 'set-cookie'
    print('RESP.HEADERS', resp.headers)
    print()
    print('TEXT', txt)


def git_stat(url):
    resp = requests.get(url)
    obj = resp.json()
    my_status = obj["components"][0]

    # print("GitHub's status is currently:", x['status'], 'as of:', x['last_updated'])
    print("As of:", my_status["updated_at"])
    if my_status["status"] == 'operational':
        print("Github is not f--ked")
    else:
        print("Github may be f--ked")


def serialize():
    my_headers = {
        "content-length": "1270",
        "content-type": "text/html",
        "etag": '359670651"',
        "cache-control": "max-age=604800",
        "server": "ECS (cpm/F9D5)",
        "date": "Mon, 20 Apr 2015 12:16:24 GMT",
        "x-cache": "HIT",
        "x-ec-custom-error": "1",
        "accept-ranges": "bytes",
        "last-modified": "Fri, 09 Aug 2013 23:54:35 GMT",
        "expires": "Mon, 27 Apr 2015 12:16:24 GMT"
    }
    serialized_data = json.dumps(my_headers)
    print(serialized_data)


def github_status(url):
    resp = requests.get(url)
    # print('type', type(resp))
    # print('status code', resp.status_code)
    # print('headers', resp.headers)
    # print('text', resp.text)

    obj = resp.json()
    my_status = obj["components"][0]
    print('status:', my_status["status"])
    print('updated_at:', my_status["updated_at"])


github_status(url1)
# git_stat(url1)
# headers(url2)
# serialize()
