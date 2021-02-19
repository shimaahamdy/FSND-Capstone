import json
from flask import request, _request_ctx_stack, jsonify, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'idandauth.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'capstone' 

# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header

# implement get_token_auth_header() method
def get_token_auth_header():

    # get header from request
    auth_header = request.headers.get('Authorization', None)

    # raise an AuthError if no header is present
    if not auth_header:
        raise header_missing

    # split bearer and the token
    header_parts = auth_header.split()
    barrer = header_parts[0]
    token = header_parts[1]

    # raise an AuthError if the header is malformed

    # check if header in barrer_token form
    if len(header_parts) > 2 or not barrer:
        raise malformed_auth
    # check first term is bearer
    if barrer.lower() != 'bearer':
        raise barrer_not_found
    # check if token is send
    if not token:
        raise token_not_found

    # return token
    return token



# implement check_permissions(permission, payload) method
def check_permissions(permission, payload):
    # raise an AuthError if permissions are not included in the payload
    if 'permissions' not in payload:
        abort(400)
    # raise an AuthError if the requested permission string is not in the
    # payload permissions array
    if permission not in payload['permissions']:
        raise premission_not_found
    return True


# implement verify_decode_jwt(token) method
def verify_decode_jwt(token):
    # get jwks from Auth0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    # an Auth0 token with key id (kid)
    if 'kid' not in unverified_header:
        raise malformed_auth

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    # verify the token using Auth0 /.well-known/jwks.json
    if rsa_key:
        # decode the payload from the token
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        # validate the claims
        except jwt.ExpiredSignatureError:
            raise token_expired

        except jwt.JWTClaimsError:
            raise incorrect_clamis

        except Exception:
            raise not_pars_auth

    raise not_found_key


# implement @requires_auth(permission) decorator method
def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator


# some implmentation of errors:
header_missing = AuthError({
    'code': 'missing_authorization_header',
    'description': 'an authorization header is expected to be send in request.'
}, 401)

barrer_not_found = AuthError({
    'code': 'invalid_header',
    'description': 'Authorization header must start with "Bearer".'
}, 401)

malformed_auth = AuthError({
    'code': 'invalid_header',
    'description': 'Authorization malformed.'
}, 401)

token_not_found = AuthError({
    'code': 'invalid_header',
    'description': 'Token not found.'
}, 401)

token_expired = AuthError({
    'code': 'token_expired',
    'description': 'Token expired.'
}, 401)

incorrect_clamis = AuthError({
    'code': 'invalid_claims',
    'description': 'Incorrect claims. check the audience and issuer.'
}, 401)

not_pars_auth = AuthError({
    'code': 'invalid_header',
    'description': 'Unable to parse authentication token.'
}, 400)

not_found_key = AuthError({
    'code': 'invalid_header',
    'description': 'Can not find the appropriate key.'
}, 400)

premission_not_found = AuthError({
    'code': 'unauthorized',
    'description': 'Permission Not found',
}, 401)
