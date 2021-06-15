import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "HEY"

# app.logger.info('This is an INFO message' + __name__)

# dev mode
app.run() 

# prod mode
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)
