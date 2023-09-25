import db_connector
from flask import Flask , Response
import json
from bson import json_util
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/getPets')
def get_pets():
    pets = db_connector.get_pets()
    response_data = json.dumps({'pets': pets}, default=json_util.default)
    return Response(response_data, mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)