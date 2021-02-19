import os
import json
from flask import Flask, request, abort, jsonify
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import AuthError, requires_auth
#import models
from models import setup_db, Actor, Moive, actors



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)
  
  #index page
  @app.route('/')
  def index():
    return 'welcome in casting agency'


  #view moives endpoint
  #allowed to (Casting Assistant,Casting Director, Executive Producer)
  @app.route('/moives')
  @requires_auth('get:moives')
  def get_moives(payload):
    # select all moives from database
    selection = Moive.query.all()

    # return json object formated for drinks
    return jsonify({
      'success': True,
      'moives': [moive.format() for moive in selection]
        })

  #view actors endpoint
  #allowed to (Casting Assistant,Casting Director, Executive Producer)
  @app.route('/actors')
  @requires_auth('get:actors')
  def get_actors(payload):
    # select all actors from database
    selection = Actor.query.all()

    # return json object formated for drinks
    return jsonify({
      'success': True,
      'actors': [moive.format() for moive in selection]
    })
  
  #create moive endpoint
  # allowed to (Executive Producer) 
  @app.route('/moives', methods=['POST'])
  @requires_auth('post:moives')
  def create_moive(payload):
    # get requet body and content data of request
    body = request.get_json()
    title = body.get('title')
    realse_date = body.get('realse_date')
    category = body.get('category')
    rate = body.get('rate')
    
    if not title or not realse_date:
        abort(400)
    
    try:
      
      # create a new row in the moive table
      moive = Moive(title=title,realse_date=realse_date,category=category,rate=rate)
      moive.insert()

      # return json object format for moive
      return jsonify({
        'success': True,
        'moive': moive.format()
        })
    except BaseException:
        abort(422)

  #create actor endpoint
  # allowed to (Casting Director, Executive Producer) 
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actor(payload):
    
    # get requet body and content data of request
    body = request.get_json()
    name = body.get('name')
    gender = body.get('gender')
    age = body.get('age',None)
    
    if not name or not gender:
      abort(400)
    try:
      
      # create a new row in the actor table
      actor = Actor(name=name,gender=gender,age=age)
      actor.insert()

      # return json object format for actor
      return jsonify({
        'success': True,
        'actor': actor.format()
            })
    except BaseException:
      abort(422)
  
  #delete moive endpoint
  # allowed to (Executive Producer) 
  @app.route('/moives/<int:moive_id>', methods=['DELETE'])
  @requires_auth('delete:moives')
  def delete_moive(payload,moive_id):
    # get moive with id
    moive = Moive.query.filter(Moive.id == moive_id).one_or_none()
    show_delted_moive = moive
    # respond with a 404 error if <id> is not found
    if not moive:
      abort(404)

    try:
      # delete the corresponding row for <id>
      moive.delete()
      # return json object format for moive
      return jsonify({
        'success': True,
        'delete': show_delted_moive.format()
        })
    except BaseException:
      abort(422)

  #delete actor endpoint
  # allowed to (Casting Director,Executive Producer) 
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(payload,actor_id):
    # get actor with id
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    show_delted_actor = actor
    # respond with a 404 error if <id> is not found
    if not actor:
      abort(404)

    try:
      # delete the corresponding row for <id>
      actor.delete()
      # return json object format for moive
      return jsonify({
        'success': True,
        'delete': show_delted_actor.format()
        })
    except BaseException:
        abort(422)
  
  #update moive endpoint
  # allowed to (Casting Director,Executive Producer) 
  @app.route('/moives/<int:moive_id>', methods=['PATCH'])
  @requires_auth('patch:moives')
  def update_moive(payload,moive_id):
    
    # get moive with id
    moive = Moive.query.filter(Moive.id == moive_id).one_or_none()

    # respond with a 404 error if <id> is not found
    if not moive:
      abort(404)

    # get requet body and content data of request
    body = request.get_json()
    title = body.get('title')
    realse_date = body.get('realse_date')
    category = body.get('category')
    rate = body.get('rate')
    
    #if not title and not realse_date and not category and not rate:
      #abort(400)
    
    try:
      
      # update the corresponding row for <id>
      if title:
        moive.title = title
        
      if realse_date:
        moive.realse_date = realse_date
        
      if category:
        moive.category = category

      if rate:
        moive.rate = rate
          
      moive.update()

      # return json object
      return jsonify({
        'success': True,
        'moive': [moive.format()]
        })

    except BaseException:
        abort(422)
  
  #update actor endpoint
  # allowed to (Casting Director,Executive Producer) 
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(payload,actor_id):
    
    # get actor with id
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

    # respond with a 404 error if <id> is not found
    if not actor:
      abort(404)

    # get requet body and content data of request
    body = request.get_json()
    name = body.get('name')
    gender = body.get('gender')
    age = body.get('age')
    
    try:
      # update the corresponding row for <id>

      if name:
        actor.name = name
        
      if gender:
        actor.gender = gender
        
      if age:
        actor.age = age

          
      actor.update()

      # return json object
      return jsonify({
        'success': True,
        'actor': [actor.format()]
        })
    
    except BaseException:
        abort(422)
    
  # Error Handling

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "unprocessable"
      }), 422


  @app.errorhandler(400)
  def bad_request(error):
    
    return jsonify({
      "success": False,
      "error": 400,
      "message": "bad request structure"
    }), 400


  @app.errorhandler(403)
  def forbidden_request(error):
    return jsonify({
      "success": False,
      "error": 403,
      "message": "forbidden requiest:Permission Not found"
      }), 403


  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "resource not found"
      }), 404


  @app.errorhandler(AuthError)
  def auth_error(error):
     #print the error that arise in auth functions
    print(error)
    return jsonify({
      "success": False,
      "error": error.status_code,
      "code": error.error['code'],
      "message": error.error['description']
    }), error.status_code

  return app
#run applicatiom
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)