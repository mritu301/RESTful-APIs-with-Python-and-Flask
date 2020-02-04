# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:08:07 2020

@author: MJ
"""

from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
