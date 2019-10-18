# Part-1 consist two microservices.
```
Service-1 called micro-1.py
Service-2 called  micro-2.py
```
## Challange
```
You have to develop the microservices in two parts.
Microservice 1 should have input string message. It should respond with json of
reverse and random number.
{“message”: “abcdef”} --> {“message”: “fedcba”, “random”: 2.45}
In order to avoid load on microservice 1, we want to delegate the reverse string
task to microservice 2 which will just return reverse of the string
{“message”: “abcdef”} --> {“message”: “fedcba”}
```
 
## Solution:-
```
1:- service-1 gives reverse-string 
2:- service-2 gives random number
3:- service-2 is callable using service-1 as per challange demand.
```

## Result Screenshot (from pod) :-

![Screenshot](https://github.com/Gaurav2586/saloodo/blob/master/screenshot/pods-final-sceenshot.png?raw=true "pods-final-sceenshot")

# Quick look :-
## micro-1.py 

```
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
   
   ```

## micro-2.py

```
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
    
```

## THE END


