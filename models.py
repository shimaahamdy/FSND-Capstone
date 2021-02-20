import os
from sqlalchemy import Column, String, Integer, create_engine,DateTime, Table, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "castagency"
#updata database with my local device data
database_path = "postgres://{}:{}@{}/{}".format('postgres','love','localhost:5432', database_name)


db = SQLAlchemy()

# setup_db(app): binds a flask application and a SQLAlchemy service

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://jsyuvjdjaqomin:854c98804b588cd7670dc5133b62bc55aeab92b1489e283c76f4e5c131a8257b@ec2-54-145-249-177.compute-1.amazonaws.com:5432/d6cqpe7baqml8h"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


#relation between actor and moive many to many 
# one actor can act in many moives 
# one moive can have many actors work on
# split relation with assoication table (actors)
# actors have moive id and actor id as foregin keys

actors = db.Table("actors",db.Model.metadata,
                  db.Column("actor_id", db.Integer, db.ForeignKey("actor.id")),
                  db.Column("movie_id", db.Integer, db.ForeignKey("moive.id")),
                  )
# Moives 
class Moive(db.Model):  
  __tablename__ = 'moive'
  
  id = Column(Integer, primary_key=True)
  title = Column(String,nullable=False)
  realse_date = Column(DateTime,nullable=False)
  category = Column(String)
  rate = Column(Integer)
  
  #the relationship 
  actors = db.relationship("Actor", secondary=actors, backref="movies", lazy="select")


  def __init__(self, title, realse_date, category, rate):
    self.title = title
    self.realse_date = realse_date
    self.category = category
    self.rate = rate

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'relase_date': self.realse_date,
      'category': self.category,
      'rate': self.rate
    }

# Actor 
class Actor(db.Model):  
  __tablename__ = 'actor'

  id = Column(Integer, primary_key=True)
  name = Column(String,nullable=False)
  gender = Column(String,nullable=False)
  age = Column(Integer)
  
  
  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'gender': self.gender,
      'age': self.age
    }