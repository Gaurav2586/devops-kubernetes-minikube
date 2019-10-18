#!/usr/bin/env python

from flask import Flask, jsonify
import urllib
import json 

app = Flask(__name__)

@app.route('/reverse_random/<string:string>', methods=['GET'])
def reverse(string):
    content = urllib.request.urlopen('http://127.0.0.1:5001').read().decode('utf-8')
    print('response from m2: ', content)
    string = string[::-1]
    return jsonify({'message': string, 'random' : json.loads(content)['message']})


if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0", port=5000)
