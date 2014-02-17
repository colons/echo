#!/usr/bin/env python2.7

import bottle


@bottle.route('/', method=['GET', 'POST'])
def index(name="index"):
    dictionaries = {
        'GET': bottle.request.query,
        'POST': bottle.request.forms,
    }

    return bottle.template('page.html', dictionaries=dictionaries)

appliction = bottle.default_app()

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8120)
