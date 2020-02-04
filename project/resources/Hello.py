# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 15:08:07 2020

@author: MJ
"""

from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "Hello, World!"}
