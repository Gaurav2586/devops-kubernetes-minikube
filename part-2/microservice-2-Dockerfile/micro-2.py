#!/usr/bin/env python
import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def myRandom():
    r1 = random.uniform(0, 10)

    return jsonify({'message': r1 })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
