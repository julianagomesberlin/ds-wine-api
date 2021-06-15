import json
import flask
from flask import jsonify

# read and parse
with open('wine-detailed-data.json', 'r') as json_file:
    json_str=json_file.read()
all_wines = json.loads(json_str)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "HEY"

@app.route('/all')
def print_all():
    return jsonify(all_wines)

# dev mode
app.run() 

# prod mode
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)
