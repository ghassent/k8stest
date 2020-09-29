from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# |======== CORS CONFIG =========|
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return 'App Works!'
@app.route('/hello_user', methods=['POST'])
def hello():
    payload = request.get_json()
    return  jsonify(dict(data='Hello {}'.format(payload.get("name")))), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)