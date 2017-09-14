from flask import Flask, request
from flask import Response
from get_data import add_numbers, get_time_string
import json

app = Flask(__name__)


# /api/addition?numone=22&numtwo=3
@app.route('/api/addition', methods=['GET'])
def addition():

    # get(key, default=None, type=None)

    num_one = request.args.get('numone', default=0, type=int)
    num_two = request.args.get('numtwo', default=0, type=int)

    dict_data = {
        'num_one' : num_one,
        'num_two' : num_two,
        'output' : add_numbers(num_one, num_two)
    }

    return json.dumps(dict_data)


@app.route('/api/time')
def time():
    return json.dumps({'time_str' : get_time_string()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
