import os
import re
from flask import Flask, jsonify, render_template, request, url_for
from flask_jsglue import JSGlue

# configure application
app = Flask(__name__)
JSGlue(app)

@app.route('/')
def home():
    """Render file."""
    return render_template('shots.html')

if __name__ == '__main__':
    port = 80
    app.run(port = port)
