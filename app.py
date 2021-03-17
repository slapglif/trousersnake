from flask import Flask, jsonify
from flask_swagger import swagger

import json
app = Flask(__name__)


@app.route('/discharge')
def discharge():
    with open('payload.json') as f:
        return jsonify(json.loads(f.read()))


@app.route('/api/symptomgroups')
def discharge():
    with open('symptomgroups.json') as f:
        return jsonify(json.loads(f.read()))


@app.route("/spec")
def spec():
    return jsonify(swagger(app))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
