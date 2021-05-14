from flask import Flask
from flask_cors import CORS
from flask_jwt_extended.jwt_manager import JWTManager
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

from api.routes import create_route
from flask_swagger_ui import get_swaggerui_blueprint

from blueprints.Home import index

config = {
    'JSON_SORT_KEYS': False,
    'JWT_SECRET_KEY': 'BaNPFol%Dgfgge',
    'JWT_ACCESS_TOKEN_EXPIRES': 300,
    'JWT_REFRESH_TOKEN_EXPIRES': 604800
}

#init app
app = Flask(__name__)


CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


app.config.update(config)

api = Api(app)
create_route(api=api)

# swagger specific
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python Flask RESTful API"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)

# init JWT
jwt = JWTManager(app=app)

app.register_blueprint(index)

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True,use_reloader=True)