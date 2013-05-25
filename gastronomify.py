#!/usr/bin/env python2
import os

from requests import session

EMAIL = os.environ['SAFEWAY_EMAIL']
PASSWORD = os.environ['SAFEWAY_PASSWORD']

def login():
    s = session()
    s.get('https://shop.safeway.com/ecom/account/sign-in')
    data = {
        'form': 'signIn',
        'SignIn.EmailAddress': EMAIL,
        'SignIn.Password': PASSWORD,
        'SignIn.RememberMe': 'false',
        'signInButton': 'Sign In',
    }
    s.post('https://shop.safeway.com/ecom/account/sign-in', data = data)
    return s
