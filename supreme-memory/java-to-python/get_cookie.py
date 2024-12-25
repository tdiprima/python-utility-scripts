#!/usr/bin/env python
import requests


class GetToken(object):
    @classmethod
    def main(cls, args):
        username = "xxxxx"
        password = "xxxxx"
        auth = "{\"name\":\"" + username + "\", \"pass\": \"" + password + "\"}"
        r1 = requests.post('https://quip.bmi.stonybrook.edu/user/login?_format=json', data=auth)
        # print('TEXT', response.text) # It's just the main page.
        print('HEADERS', r1.headers)
        print('COOKIE', r1.headers['Set-Cookie'])
        r2 = requests.get('https://quip.bmi.stonybrook.edu/listofimages/48?_format=json', cookies=r1.cookies)
        print(r2.json())


if __name__ == '__main__':
    import sys

    GetToken.main(sys.argv)
