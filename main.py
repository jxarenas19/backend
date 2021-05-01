import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.admin.resources.resource_admin import admin_v1_0_bp, AdminListResource
from app.ext import ma
from config.config import app_config

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(app_config[os.getenv('FLASK_ENV')])
jwt = JWTManager(app)
ma.init_app(app)
# Captura todos los errores 404
Api(app, catch_all_404s=True)

# Deshabilita el modo estricto de acabado de una URL con /
app.url_map.strict_slashes = False

# Registra los blueprints
app.register_blueprint(admin_v1_0_bp)


