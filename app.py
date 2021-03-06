from flask import Flask, jsonify


import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/discharge')
def discharge():
    with open('payload.json') as f:
        return jsonify(json.loads(f.read()))


@app.route('/api/symptomgroups')
def index():
    with open('symptomgroups.json', encoding='latin-1') as f:
        return f.read()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
