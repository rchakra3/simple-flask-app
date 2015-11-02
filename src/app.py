from flask import Flask
from flask import abort
from flask import make_response
import requests

app = Flask(__name__)

giphy_string = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="
retries = 5


@app.route('/')
def party_gif():
    resp = get_resp_dict(giphy_string + "party")
    if resp is None:
        abort(make_response('Something went wrong:<br>No gif for you', 500))

    if resp['data']['image_url']:
        img_url = resp['data']['image_url']
        return '<img src=' + img_url + '>'


def get_resp_dict(url):
    tries_left = retries

    while(tries_left > 0):
        resp = requests.get(url)
        resp = resp.json()
        if resp['meta']:
            if resp['meta']['status'] == 200:
                return resp
        tries_left -= 1
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')