from flask import Blueprint, request
from flask_restful import Resource, Api
from marshmallow import ValidationError

from app.admin.models import User
from app.admin.schemas import UserSchema
from app.common.db_util import DatabaseUtils
from app.common.pagination import PaginationData
from app.common.response import Response
from app.common.response_data import ResponseData
from app.common.strings import ELEMENT_INSERT, ELEMENT_UPDATE, ELEMENT_DELETE

admin_schema = UserSchema()
admin_v1_0_bp = Blueprint('admin_v1_0_bp', __name__)
api = Api(admin_v1_0_bp)


class AdminListResource(Resource):
    """

    """

    def get(self):
        pagination_obj = PaginationData(User, '', '')
        items = pagination_obj.get_data_paginate()
        pagination_obj.close_connection()
        result = admin_schema.dump(items, many=True)
        return ResponseData('200', {}, [], result, []).get_response()

    def post(self):
        data = request.get_json()
        try:
            user_dict = admin_schema.load(data)
            user = User(**user_dict)
            db_util = DatabaseUtils(user)
            db_util.save()
            resp = admin_schema.dump(user)
            db_util.close_connection()
            return Response('200', {}, [resp],
                            ELEMENT_INSERT).get_response()
        except ValidationError as err:
            return Response('500', err.messages, {},
                            {}).get_response()


class AdminResource(Resource):

    def get(self, user_id):
        db_util = DatabaseUtils(model=User)
        user = db_util.get_by_id_specific(dimension_id=user_id)
        if user is None:
            return Response().reponse_no_exist_element()
        resp = admin_schema.dump(user)
        db_util.close_connection()
        return Response('200', {}, resp, {}).get_response()

    def put(self, user_id):
        data = request.get_json()
        db_util = DatabaseUtils(model=User)
        user = db_util.get_by_id(user_id)
        if user is None:
            return Response().reponse_no_exist_element()
        try:
            user_dict = admin_schema.load(data)
        except ValidationError as err:
            return Response('500', err.messages, {},
                            {}).get_response()
        db_util.update(user_dict)
        db_util.close_connection()
        return Response('200', {}, [user_dict],
                        ELEMENT_UPDATE).get_response()

    def delete(self, user_id):
        db_util = DatabaseUtils(model=User)
        user = db_util.get_by_id(user_id)
        if user is None:
            return Response().reponse_no_exist_element()
        db_util.delete()
        db_util.close_connection()
        return Response('200', {}, user_id,
                        ELEMENT_DELETE).get_response()


api.add_resource(AdminListResource, '/admin_users')

api.add_resource(AdminResource, '/admin_users/<int:user_id>')
