#!/usr/bin/env python
# -*- coding: utf8 -*-

import time

from jwt import JWT, jwk_from_pem, jwk_from_dict
import requests


class JWTAuth(requests.auth.AuthBase):
    def __init__(self, iss, key, expiration=10 * 60):
        self.iss = iss
        self.expiration = expiration
        self.key = jwk_from_pem(bytes(key, 'utf-8'))

    def generate_token(self):
        jwt = JWT()
        # Generate the JWT
        payload = {
          # issued at time
          'iat': int(time.time()),
          # JWT expiration time (10 minute maximum)
          'exp': int(time.time()) + self.expiration,
          # GitHub App's identifier
          'iss': self.iss
        }

        token = jwt.encode(payload, self.key, 'RS256')

        return token

    def __call__(self, r):
        r.headers['Authorization'] = 'bearer {}'.format(self.generate_token())
        return r


class TokenAuth(requests.auth.AuthBase):
    def __init__(self, app, access_token):
        self._app = app
        self._access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = 'token {}'.format(self._access_token['token'])
        return r
