from flask_restful import Api

from api.cat import CatApi
from api.authentication import TokenApi,RefreshToken

def create_route(api: Api):

    api.add_resource(TokenApi,'/authentication/token')
    api.add_resource(RefreshToken,'/authentication/token/refresh')

    api.add_resource(CatApi, '/cat')
    
