# CS257 end-to-end assignment
# written by Yiming Xia
# 11.9.2022


import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password)



@api.route('/fuel_consumption/') 
def get_car_fuel ():
    query = '''SELECT modeltable.model, modeltable.make, fueltable.consumption_comb, linkstable.linkid
                FROM modeltable, fueltable, linkstable
                WHERE modeltable.id = linkstable.modelID
                AND fueltable.id = linkstable.modelID
                ORDER BY fueltable.consumption_comb
                LIMIT 20; '''
    car_fuel_list = [] 
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            car = {'model':row[0],
                      'make':row[1],
                      'fuel_consumption':row[2],
                      'linksID':row[3]}
            car_fuel_list.append(car)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_fuel_list)

@api.route('/co2_emission/') 
def get_car_co2 ():
    query = '''SELECT modeltable.model, modeltable.make, co2table.co2_emission, linkstable.linkid
                FROM modeltable, fueltable, linkstable, co2table
                WHERE modeltable.id = linkstable.modelID
                AND fueltable.id = linkstable.modelID
                ORDER BY co2table.co2_emission
                LIMIT 20; '''
    car_co2_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            car = {'model':row[0],
                      'make':row[1],
                      'co2_emission':row[2],
                      'linksID':row[3]}
            car_co2_list.append(car)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_co2_list)

@api.route('/engine_size/') 
def get_car_engine ():
    query = '''SELECT modeltable.model, modeltable.make, modeltable.engine_size, linkstable.linkid
                FROM modeltable, linkstable
                WHERE linkstable.modelID = modeltable.id
                ORDER BY modeltable.engine_size
                LIMIT 20; '''
    car_engine_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        cursor.execute(query)
        print(cursor.query)
        for row in cursor:
            car = {'model':row[0],
                      'make':row[1],
                      'engine_size':row[2],
                      'linksID':row[3]}
            car_engine_list.append(car)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_engine_list)


@api.route('/search/<make>')
def search_cars_for_make(make):
    query = '''SELECT modeltable.model, modeltable.make, fueltable.consumption_comb, linkstable.linkid
                FROM modeltable, fueltable, linkstable
                WHERE modeltable.model ILIKE CONCAT('%%', %s, '%%')
                AND modeltable.id = linkstable.modelID
                AND fueltable.id = linkstable.fuelID;'''
    car_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (make,))
        for row in cursor:
            car = {'model':row[0], 'make':row[1], 'co2':row[2], 'linksID':row[3]}
            car_list.append(car)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(car_list)


@api.route('/hello/<linksID>')
def get_cars_detail(linksID):
    query = '''SELECT modeltable.model, modeltable.make, modeltable.vehicle_class, modeltable.engine_size, modeltable.cyliners, fueltable.fuel_type, fueltable.consumption_comb, co2table.co2_emission, co2table.co2_rating, co2table.smog_rating
                FROM modeltable, fueltable, linkstable, co2table
                WHERE linkstable.linkid = %s
                AND modeltable.id = linkstable.modelID
                AND fueltable.id = linkstable.fuelID
                AND co2table.id = linkstable.co2ID;'''
    # can make this query better, (ilike concat)
    car = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (linksID,))
        for row in cursor:
            # car = {'model':row[0], 'make':row[1], 'carClass':row[2], 'engine':row[3], 
            #     'cylinder':row[4], 'fueltype':row[5], 'fuelConsumption':row[6], 
            #     'co2Emission':row[7], 'co2Rating':row[8], 'smogRating':row[9]}
            # can't get the right element with dictionary...
            car = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]]
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)
    return flask.render_template('carpage.html', model=car[0], make=car[1], carClass=car[2], 
                                    engine=car[3], cylinder=car[4], fueltype=car[5], 
                                    fuelConsumption=car[6], co2Emission=car[7], 
                                    co2Rating=car[8], smogRating=car[9])

@api.route('/help')
def get_help():
    return flask.send_file('.' + flask.url_for('static', filename='api-design.txt'), mimetype='text')