from flask import Flask, jsonify
import json
app = Flask(__name__)


@app.route('/discharge')
def discharge():
    with open('payload.json') as f:
        return jsonify(json.loads(f.read()))


if __name__ == '__main__':
    app.run()
