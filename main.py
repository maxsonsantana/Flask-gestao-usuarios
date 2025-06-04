from flask import Flask
from routes.home import home_route # Import the home route from the routes package 

app = Flask(__name__) # Create a Flask application instance

app.register_blueprint(home_route) # Register the home route blueprint with the application

app.run(debug=True) # Run the application in debug mode(this will reload the server on code changes)