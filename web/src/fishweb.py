from bottle import route, run, template

@route('/api/value')
def save_values():
    tank_id = bottle.request.get('tank_id')
    values = bottle.request.get('values')
    for sample_time, value in values: 
        print sample_time
        print value
        print
    return {'message': 'Thank You'}

run(host='localhost', port=8080)
