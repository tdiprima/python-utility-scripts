# Logs into a specified account with user credentials, retrieves and displays headers and cookies, and obtains and
# prints a list of images in JSON format from the server using the cookies for authentication.
import requests


class GetToken(object):
    @classmethod
    def main(cls, args):
        username = "xxxxx"
        password = "xxxxx"
        auth = "{\"name\":\"" + username + "\", \"pass\": \"" + password + "\"}"
        r1 = requests.post('https://example.edu/user/login?_format=json', data=auth)
        # print('TEXT', response.text) # It's just the main page.
        print('HEADERS', r1.headers)
        print('COOKIE', r1.headers['Set-Cookie'])
        r2 = requests.get('https://example.edu/listofimages/48?_format=json', cookies=r1.cookies)
        print(r2.json())


if __name__ == '__main__':
    import sys

    GetToken.main(sys.argv)
