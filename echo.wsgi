#!/usr/bin/env python2.7

import os
import sys

import bottle

home = os.path.dirname(__file__)
sys.path.append(home)
os.chdir(home)


@bottle.route('/', method=['GET', 'POST'])
def index(name="index"):
    dictionaries = {
        'GET': bottle.request.query,
        'POST': bottle.request.forms,
    }

    return bottle.template('page', dictionaries=dictionaries)

application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8120)
