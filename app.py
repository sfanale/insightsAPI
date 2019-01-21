from flask import (Flask, render_template)
import connexion

from flask_cors import CORS, cross_origin

# create application instance
app = connexion.App(__name__, specification_dir="./")
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.app.config['CORS_HEADERS'] = 'Content-Type'
app.add_api('swagger.yml')

cors = CORS(app.app)
# read swagger.yml to configure endpoints


# add CORS support
#CORS(app.app)
# initialization


@app.route('/')
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def home():
    """
            This function just responds to the browser ULR
            localhost:5000/

            :return:        the rendered template 'home.html'
            """
    return render_template("home.html")


# if we are running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
