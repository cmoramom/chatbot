import datetime

import jwt
from flask import request, make_response, jsonify, json
from flask_restful import Resource

from config import config
from dao.user import User
from utils import mylogger


class Auth(Resource):

    # @TokenCheck.token_required
    def post(self):
        logger = mylogger.get_logger()
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        user_badge = json_data['b']

        auth = request.authorization
        logger.info('starting the user verification process for user '
                    '(' + auth.username + str(json_data) + '), Module: ' + __name__)

        if not auth or not auth.username or not auth.password:
            logger.debug('We were not able to verify the user, auth data required')
            return make_response("Usuario no se puede verificar", 401,
                                 {'www-Authenticate': 'Basic Realm= "user data required"'})
        user = User(user=auth.username, password=auth.password).verify_user()
        logger.debug('user request status code: ' + str(user.status_code))
        if user.status_code == 200:
            logger.info('user authorized, Module: ' + __name__)
            badge = json.loads(user.data)
            badge = badge['Badge']
            logger.debug('db bagde:' + str(badge))
            logger.debug('request bagde:' + str(user_badge))

            if user_badge == str(badge):
                logger.info('Badge authorized,  Module: ' + __name__)
                logger.info('Token generating process started,  Module: ' + __name__)
                data = json.loads(user.data)
                token = jwt.encode(
                    {'public_id': data['Public_id'],
                     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
                     'role': data['Role']}, config.SECRET_KEY)
                logger.info('Token generated properly, sending token,  Module: ' + __name__)
                return jsonify({'token': token.decode('UTF-8')})

            return make_response("Badge no autorizado", 401,
                                 {'www-Authenticate': 'Basic Realm= "usuario no autorizado"'})
        return make_response("Usuario no autorizado", 401,
                             {'www-Authenticate': 'Basic Realm= "usuario no autorizado"'})
