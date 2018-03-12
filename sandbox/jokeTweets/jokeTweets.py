#!/usr/bin/python3
"""
Script to start a Flask web application and route the request for /jokeTweets
"""
from flask import Flask, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.url_map.strict_slashes = False;

cors = CORS(app, resources={r"/*": {"origins":"*"}})

@app.route('/jokeTweets', methods=['GET'])
def renderJokePage():
    """
    Method to render the page to display Tweets with #joke
    """
    return render_template("jokeTweets.html");

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
