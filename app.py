from flask import Flask, jsonify

import json
app = Flask(__name__)


@app.route('/discharge')
def discharge():
    with open('payload.json') as f:
        return jsonify(json.loads(f.read()))


@app.route('/api/symptomgroups')
def index():
    with open('symptomgroups.json') as f:
        return jsonify(json.loads(f.read()))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
