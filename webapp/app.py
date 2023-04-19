# CS257 end-to-end assignment
# written by Yiming Xia
# 11.9.2022


import flask
import argparse
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/') 
def home():
    return flask.render_template('index.html')

@app.route('/search') 
def search():
    return flask.render_template('search.html')

@app.route('/sort') 
def sort():
    return flask.render_template('sort.html')

# @app.route('/help')
# def get_help():
#     return flask.send_file('.' + flask.url_for('static', filename='api-design.txt'), mimetype='text')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A books-and-authors application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
