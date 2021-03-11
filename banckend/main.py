from flask import Flask, request
from flask_cors import *
import requests
from util import detect_list


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/', methods=["POST"])
def first_flask():
    data = request.get_json()
    re_url = data.get('url')
    prefix = re_url.split('://')
    if len(prefix) == 1:
        re_url = 'http://' + re_url
    response = requests.get(re_url)
    content = response.text
    is_cont = False
    result = ''
    for i in detect_list:
        is_cont = False
        for k, v in i.items():
            for j in v:
                if j in content:
                    is_cont = True
                    break
            if not is_cont:
                result = result + k + '\t' + "没有使用" + "\n"
            else:
                result = result + k + '\t' + "使用" + "\n"
    return result  # response


if __name__ == '__main__':
    app.run()
