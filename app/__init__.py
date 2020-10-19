from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.blog_controller import api as blog_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Supplements API',
          version='1.0',
          description='api for supplements'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(blog_ns, path='/blog')
