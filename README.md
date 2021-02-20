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

### auth instructions

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
in sql shell 
```bash
drop database castagency;
createdb castagency;
```
then run in directory 
```bash
python app.py
```
back to sql shell move to castagency  (\c castagency) enter
```bash
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive1','1998-05-07','cat1',3);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive','2021-02-02','cat2',8);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive3','2021-10-10','cat3',5);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive4','2022-06-11','cat4',4);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive5','2023-08-7','cat5',6);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive6','2020-02-20','cat6',2);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive7','2025-04-15','cat4',7);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive8','2026-11-20','cat6',9);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive9','2020-02-8','cat4',5);
INSERT INTO Moive(title, realse_date, category,rate) VALUES ('moive10','2024-03-12','cat5',2);
INSERT INTO Actor(name, gender, age) VALUES ('actor1','male',32);
INSERT INTO Actor(name, gender, age) VALUES ('actor2','female',52);
INSERT INTO Actor(name, gender, age) VALUES ('actor3','female',35);
INSERT INTO Actor(name, gender, age) VALUES ('actor4','male',80);
INSERT INTO Actor(name, gender, age) VALUES ('actor5','female',22);
INSERT INTO Actor(name, gender, age) VALUES ('actor6','male',19);
INSERT INTO Actor(name, gender, age) VALUES ('actor7','male',44);
INSERT INTO Actor(name, gender, age) VALUES ('actor8','female',58);
INSERT INTO Actor(name, gender, age) VALUES ('actor9','male',12);
INSERT INTO Actor(name, gender, age) VALUES ('actor10','female',41);
INSERT INTO Actor(name, gender, age) VALUES ('actor11','female',58);
INSERT INTO Actor(name, gender, age) VALUES ('actor12','male',12);
INSERT INTO Actor(name, gender, age) VALUES ('actor13','female',41);
```
## API Reference
### Getting Started

Base URL: Casting Agency can run locally
* Backend Base URL: `http://127.0.0.1:5000/`
Or hosted
* host URL : `https://castfinal.herokuapp.com/`

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
{
    "moives": [
        {
            "category": "cat1",
            "id": 1,
            "rate": 3,
            "relase_date": "Thu, 07 May 1998 00:00:00 GMT",
            "title": "moive1"
        },
        {
            "category": "cat2",
            "id": 2,
            "rate": 8,
            "relase_date": "Tue, 02 Feb 2021 00:00:00 GMT",
            "title": "moive"
        },
        {
            "category": "cat3",
            "id": 3,
            "rate": 5,
            "relase_date": "Sun, 10 Oct 2021 00:00:00 GMT",
            "title": "moive3"
        },
        {
            "category": "cat4",
            "id": 4,
            "rate": 4,
            "relase_date": "Sat, 11 Jun 2022 00:00:00 GMT",
            "title": "moive4"
        },
        {
            "category": "cat5",
            "id": 5,
            "rate": 6,
            "relase_date": "Mon, 07 Aug 2023 00:00:00 GMT",
            "title": "moive5"
        },
        {
            "category": "cat6",
            "id": 6,
            "rate": 2,
            "relase_date": "Thu, 20 Feb 2020 00:00:00 GMT",
            "title": "moive6"
        },
        {
            "category": "cat4",
            "id": 7,
            "rate": 7,
            "relase_date": "Tue, 15 Apr 2025 00:00:00 GMT",
            "title": "moive7"
        },
        {
            "category": "cat6",
            "id": 8,
            "rate": 9,
            "relase_date": "Fri, 20 Nov 2026 00:00:00 GMT",
            "title": "moive8"
        },
        {
            "category": "cat4",
            "id": 9,
            "rate": 5,
            "relase_date": "Sat, 08 Feb 2020 00:00:00 GMT",
            "title": "moive9"
        },
        {
            "category": "cat5",
            "id": 10,
            "rate": 2,
            "relase_date": "Tue, 12 Mar 2024 00:00:00 GMT",
            "title": "moive10"
        }
    ],
    "success": true
}   
```

#### GET /actors
- General:
    -  return all available actors exist in application
- sample: `curl --location --request GET 'http://127.0.0.1:5000/actors' \ --header 'Authorization: Bearer $TOKEN_VALUE`

```json
{
    "actors": [
        {
            "age": 32,
            "gender": "male",
            "id": 1,
            "name": "actor1"
        },
        {
            "age": 52,
            "gender": "female",
            "id": 2,
            "name": "actor2"
        },
        {
            "age": 35,
            "gender": "female",
            "id": 3,
            "name": "actor3"
        },
        {
            "age": 80,
            "gender": "male",
            "id": 4,
            "name": "actor4"
        },
        {
            "age": 22,
            "gender": "female",
            "id": 5,
            "name": "actor5"
        },
        {
            "age": 19,
            "gender": "male",
            "id": 6,
            "name": "actor6"
        },
        {
            "age": 44,
            "gender": "male",
            "id": 7,
            "name": "actor7"
        },
        {
            "age": 58,
            "gender": "female",
            "id": 8,
            "name": "actor8"
        },
        {
            "age": 12,
            "gender": "male",
            "id": 9,
            "name": "actor9"
        },
        {
            "age": 41,
            "gender": "female",
            "id": 10,
            "name": "actor10"
        },
        {
            "age": 58,
            "gender": "female",
            "id": 11,
            "name": "actor11"
        },
        {
            "age": 12,
            "gender": "male",
            "id": 12,
            "name": "actor12"
        },
        {
            "age": 41,
            "gender": "female",
            "id": 13,
            "name": "actor13"
        }
    ],
    "success": true
}   
```

#### POST /moives
- General:
  - POST a new moive, which will require the title and realse date 
  - for creation, return moive we creat and its id

- Sample: `curl --location --request POST 'http://127.0.0.1:5000/movies' \ --header 'Authorization: Bearer $TOKEN_VALUE' \ --header 'Content-Type: application/json' \ --data-raw '{"title":"lala land" "realse_date": "1998-07-13","categooory":"action","rate":4}'`

```json
{
    "moive": {
        "category": null,
        "id": 11,
        "rate": 4,
        "relase_date": "Mon, 13 Jul 1998 00:00:00 GMT",
        "title": "lala land"
    },
    "success": true
}
```

#### POST /actors
- General:
  - POST a new actor, which will require the name and gender 
  - for creation, return actor we creat and its id

- Sample: `curl --location --request POST 'http://127.0.0.1:5000/actors' \ --header 'Authorization: Bearer $TOKEN_VALUE' \ --header 'Content-Type: application/json' \ --data-raw '{"name":"jane" "gender": "female","age":30}'`

```json
{
    "actor": {
        "age": 30,
        "gender": "female",
        "id": 14,
        "name": "jane"
    },
    "success": true
}
```
#### DELETE /moives
- General:
  - Delete moive with id number
  - return the delted item

- Sample: `curl  --request DELETE 'http://127.0.0.1:5000/movies/11' \ --header 'Authorization: Bearer $TOKEN_VALUE'`

```json
{
    "delete": {
        "category": null,
        "id": 11,
        "rate": 4,
        "relase_date": "Mon, 13 Jul 1998 00:00:00 GMT",
        "title": "lala land"
    },
    "success": true
}
```
#### DELETE /actors
- General:
  - Delete an actor with id number
  - return delted item

- Sample: `curl  --request DELETE 'http://127.0.0.1:5000/actors/14' \ --header 'Authorization: Bearer $TOKEN_VALUE'`

```json
{
    "delete": {
        "age": 30,
        "gender": "female",
        "id": 14,
        "name": "jane"
    },
    "success": true
}
```
#### PSTCH /moives
- General:
  - update current moive with specific data  
  - return the updated item 

- Sample: `curl --location --request PATCH 'http://127.0.0.1:5000/movies/5' \ --header 'Authorization: Bearer $TOKEN_VALUE' \ --header 'Content-Type: application/json' \ --data-raw '{"title":"lala land" "realse_date": "1998-07-13","categooory":"action","rate":4}'`

```json
{
    "moive": [
        {
            "category": "cat5",
            "id": 5,
            "rate": 4,
            "relase_date": "Mon, 13 Jul 1998 00:00:00 GMT",
            "title": "lala land"
        }
    ],
    "success": true
}
```
#### PATCH /actors
- General:
  -update current actor with specific data

- Sample: `curl --location --request PATCH 'http://127.0.0.1:5000/actors/5' \ --header 'Authorization: Bearer $TOKEN_VALUE' \ --header 'Content-Type: application/json' \ --data-raw '{"name":"jane" "gender": "female","age":30}'`

```json
{
    "actor": [
        {
            "age": 30,
            "gender": "female",
            "id": 5,
            "name": "jane"
        }
    ],
    "success": true
}
```
## Authors
- shimaa hamdy
