from flask import Flask, render_template
import requests
import pprint

app = Flask(__name__)


def api_url(url_bit):
    pipedrive_api = "https://api.pipedrive.com/v1/"
    api_token = "f94a09cf0301bc69b97523b127f4e01501251fca"
    return pipedrive_api + url_bit + "?api_token=" + api_token


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/deals/')
def list_deals():
    url = api_url("deals")
    r = requests.get(url)
    return render_template('deallist.html', deal_list=r.json()['data'])

@app.route('/confirms/')
def list_confirms():
    url = api_url("deals")
    r = requests.get(url)
    confirm_list = [d for d in r.json()['data'] if d['stage_id'] == 6]
    return render_template('deallist.html', deal_list=confirm_list)

@app.route('/deals/<deal_id>')
def show_deal(deal_id):
    url = api_url("deals/"+deal_id)
    r = requests.get(url)
    return '<pre>' + pprint.pformat(r.json()) + '</pre>'


if __name__ == '__main__':
    app.debug = True
    app.run()