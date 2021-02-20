# Casting Agency

Casting Agency is a backend for web application (filming and casting online agency)
 
The application features:

1) Display all moives also all actors in the system. 
2) Delete moives or actors that no longer belong to agency.
3) Add moives and require that they include moive's title and realse_data.
4) Add actors and require that they include actor's name and gender.
5) Update moives and actors data


## Getting Started

### Prerequisites & Installation

#### Python 3.7
install python 3.7 version is a need (other versions cause problems) for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP installations

navigate to the project directory and run:

```bash
pip install -r requirements.txt
```

This will install all of the required packages in the `requirements.txt` file.
##### the basic dependencies

- Flask
- SQLAlchemy
- Flask-CORS
- jose

#### Database Setup

-make sure Postgres server is runing
create database called "capstone" run:
```bash
create database castagency;
```

### auth dependecny

1. Create Auth0 Account
2. Create a new, single page web application
3. Create a new API
    - in API Settings:
        - Enable RBAC
4. Create new API permissions for each endpoint
6. Create new roles for:
    - Assistant
    - Director
    - Producer
    
    -after creation add to each role the specific endpoint they can hit
7. Test your endpoints with [Postman](https://getpostman.com) or with cURL as mentioned below in the testing section.
8. Register 3 users - assign them to roles(Assistant, Director, Producer)
9. Sign into each account and make note of the JWT to use it in auth0.
### Running the server

From project directory, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

or simply run :
'''bsdh
python app.py 
'''
### Arcitecture
## CastingAgency  General Architecture

* Models:
    
    * Movies 
    * Actors
    * Many to many realation

* Endpoints:

    * GET /actors  
    * GET /movies

    * DELETE /actors/
    * DELETE /movies/
    
    * POST /actors 
    * POST  /movies 
    
    * PATCH /actors/ 
    * PATCH /movies/

* Roles:
    
* Assistant
    
    * Can view actors and movies

* Director
    
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database
    * Modify actors or movies

* Producer
    
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database


### Testing
To run the tests, run
```
dropdb castagency_test
createdb castagency_test
psql castagency_test < castagency
python test_app.py
```
## API Reference
### Getting Started

Base URL: Casting Agency can run locally
* Backend Base URL: `http://127.0.0.1:5000/`
Or hosted
* host URL : `http://127.0.0.1:5000/`

### Error Handling

Errors returned as object (json format):

```json
      {
        "success": "False",
        "error": 400,
        "message": "bad request structure",
      }
```

The error that will return when request fail:

* 400 – bad request structure
* 404 – resource not found
* 422 – requist unprocessable
* 403 - forbidden requiest:Permission Not found
* 401 - auth error
### Endpoints

#### GET /moives
- General:
    -  return all available moives exist in application
- sample: `curl --location --request GET 'http://127.0.0.1:5000/moives' \ --header 'Authorization: Bearer $TOKEN_VALUE`

```json
    
```

#### GET /actors
- General:
    -  return all available actors exist in application
- sample: `curl --location --request GET 'http://127.0.0.1:5000/actors' \ --header 'Authorization: Bearer $TOKEN_VALUE`

```json
    
```

#### POST /moives
- General:
  - POST a new moive, which will require the title and realse date 
  - for creation, return moive we creat and its id

- Sample: `curl --location --request POST 'http://127.0.0.1:5000/moives' \ --header 'Authorization: Bearer $TOKEN_VALUE' \ --header 'Content-Type: application/json' \ --data-raw '{"name" : "arwa","age" : 80,"gender":"female"}'`

```json

```

#### POST /actors
- General:
  - POST a new actor, which will require the name and gender 
  - for creation, return actor we creat and its id

- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{    "title": "la la land", "relase_data": "1999-02-13", "category": "Action", "rate":5 }'`

```json

```
#### DELETE /moives
- General:
  - POST a new actor, which will require the name and gender 
  - for creation, return actor we creat and its id

- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{    "title": "la la land", "relase_data": "1999-02-13", "category": "Action", "rate":5 }'`

```json

```
#### DELETE /actors
- General:
  - POST a new actor, which will require the name and gender 
  - for creation, return actor we creat and its id

- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{    "title": "la la land", "relase_data": "1999-02-13", "category": "Action", "rate":5 }'`

```json

```
#### PSTCH /moives
- General:
  - POST a new actor, which will require the name and gender 
  - for creation, return actor we creat and its id

- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{    "title": "la la land", "relase_data": "1999-02-13", "category": "Action", "rate":5 }'`

```json

```
#### PSTCJ /actors
- General:
  - POST a new actor, which will require the name and gender 
  - for creation, return actor we creat and its id

- Sample: `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -d '{    "title": "la la land", "relase_data": "1999-02-13", "category": "Action", "rate":5 }'`

```json

```
## Authors
- shimaa hamdy
