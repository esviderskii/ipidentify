from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    return str(request.remote_addr), 200

@app.route("/api", methods=["GET"])
def api():
    return jsonify({'ip': request.remote_addr}), 200
