from flask import Flask, jsonify
from ftfy import fix_text

import json
app = Flask(__name__)


@app.route('/discharge')
def discharge():
    with open('payload.json') as f:
        return jsonify(json.loads(f.read()))


@app.route('/api/symptomgroups')
def index():
    with open('symptomgroups.json', encoding='latin-1') as f:
        fixed_text = fix_text(f.read())
        return jsonify(json.dumps(fixed_text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
