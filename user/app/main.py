from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    """
    Health endpoint

    :return:
    :rtype:
    """

    return Response(json.dumps({"status": "ok"}), status=200, mimetype='application/json')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
