import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Moive


class CastingAgncyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','love','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.assistant_token = os.getenv('ASSISTANT_TOKEN')
        self.director_token = os.getenv('DIRECTOR_TOKEN')
        self.producer_token = os.getenv('PRODUCER_TOKEN')

        self.assistant_header = {'Authorization': self.assistant_token}
        self.director_header = {'Authorization': self.director_token}
        self.producer_header = {'Authorization': self.producer_token}

        self.new_movie = {
            "title":"lala land",
            "release_date": "5-7-1998",
            "category":"action",
            "rate":4
            }
        self.new_actor = {
            "name":"jane",
            "gender": "female",
            "age":30
            }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    
    def test_get_moives(self):
        #run test and get result in json format
        res = self.client().get('/moives',headers=self.assistant_header)
        data = json.loads(res.data)

        #check the response data
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['moives'])

    def test_get_actors(self):
        #run test and get result in json format
        res = self.client().get('/actors',headers=self.producer_header)
        data = json.loads(res.data)

        #check the response data
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_create_moive(self):
        res = self.client().post('/moives',json=self.new_movie,headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['moive'])

    def test_400_fail_create_movie(self):
        res = self.client().post('/moives',json={},headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request structure')    
    
    def test_401_unauth_create_movie(self):
        res = self.client().post('/moives',json=self.new_movie,headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')      
    
    def test_create_actor(self):
        res = self.client().post('/actors',json=self.new_actor,headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_400_fail_create_actor(self):
        res = self.client().post('/actors',json={},headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['message'], 'bad request structure')    
    
    def test_401_unauth_create_actor(self):
        res = self.client().post('/actors',json=self.new_movie,headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'unauthorized')      
        
    def test_delete_moive(self):
        res = self.client().delete('/moives/2',headers=self.producer_header)
        data = json.loads(res.data)
        
        moive = Moive.query.filter(Moive.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delted'])
        self.assertEqual(moive, None)
    
    def test_404_delete_moive_not_exist(self):
        res = self.client().delete('/moives/1000',headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_401_delete_moive_unauth(self):
        res = self.client().delete('/moives/3',headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['code'], 'unauthorized')

    def test_delete_actor(self):
        res = self.client().delete('/actor/2',headers=self.director_header)
        data = json.loads(res.data)
        
        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['delted'])
        self.assertEqual(actor, None)
    
    def test_404_delete_actor_not_exist(self):
        res = self.client().delete('/actors/1000',headers=self.producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_401_delete_actor_unauth(self):
        res = self.client().delete('/actor/3',headers=self.assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['code'], 'unauthorized')

    def test_update_moive(self):
        res = self.client().patch('/moives/4',json=self.new_movie,headers=self.director_header)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['moive'])


    def test_404_update_moive_not_exist(self):
        res = self.client().patch('/moives/999',json=self.new_movie,headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_update_actor(self):
        res = self.client().patch('/actor/4',json=self.new_movie,headers=self.producer_header)
        data = json.loads(res.data)
        
        actor = Actor.query.filter(Actor.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])
        self.assertEqual(actor,None)

    def test_404_update_actor_not_exist(self):
        res = self.client().patch('/actor/999',json=self.new_movie,headers=self.director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    
    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
