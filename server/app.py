#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource

from config import app, db, api
from models import User, UserSchema

class ClearSession(Resource):

  def delete(self):
  
    session['page_views'] = None
    session['user_id'] = None

    return {}, 204
  
class Signup(Resource):
  
  def post(self):
    data = request.get_json()
    
    user = User(username=data.get('username'))
    user.password_hash = data.get('password')
    
    db.session.add(user)
    db.session.commit()
    
    session['user_id'] = user.id

    return UserSchema().dump(user), 201

api.add_resource(ClearSession, '/clear', endpoint='clear')
api.add_resource(Signup, '/signup')

if __name__ == '__main__':
  app.run(port=5555, debug=True)
