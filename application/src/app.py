import json
from abc import ABCMeta, abstractmethod
from datetime import date, datetime
from bson import ObjectId

from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin

from functools import wraps
from flask import request, Response


OK, CREATED, PRECONDITION_FAILED, UNSUPPORTED_MEDIA_TYPE, NOT_FOUND, UNAUTHORIZED = 200, 201, 412, 415, 404, 401
app = Flask('CaptchaAnalysisService')


class JSONSerializable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def toJson(self):
        pass


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if isinstance(o, JSONSerializable):
            return o.toJson()
        return json.JSONEncoder.default(self, o)


app.json_encoder = JSONEncoder
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def jsonify(o):
    return JSONEncoder().encode(o)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method != 'OPTIONS':
            auth = request.headers['Authorization']
            if auth != 'Bearer e15597764b887a9e784d820f5f7c1aa2333d2a68753f8a13cb4d04f95359400b':
                return jsonify({'error': 'UNAUTHORIZED.'}), UNAUTHORIZED
        return f(*args, **kwargs)

    return decorated


@requires_auth
@app.route('/captcha_analysis', methods=['POST'])
def image_analysis_post():
    try:
        content = request.get_json()
    except Exception as e:
        return "Error while try to get request from json. Error: %s" % e, 404
    try:
        return 'Working!', 200
    except Exception as e:
        return "Error while try to read the provide data. Error: %s" % e, 404


if __name__ == '__main__':
    app.run('0.0.0.0', port=8090)
