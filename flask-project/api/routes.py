from flask_restful import Api

from api.cat import CatsApi,CatApi
from api.authentication import TokenApi,RefreshToken
from api.machine import MLware
def create_route(api: Api):

    api.add_resource(TokenApi,'/authentication/token')
    api.add_resource(RefreshToken,'/authentication/token/refresh')
    api.add_resource(MLware,'/machine')
    api.add_resource(CatsApi, '/cat')
    api.add_resource(CatApi, '/cat/<catname>')
    


