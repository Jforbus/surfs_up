#dependency

from flask import Flask
import random
import numpy as np
#create Flask app instance
app = Flask(__name__)

# Create Flask Route
####################

#Route 1
##root
@app.route('/')

# create function
#def hello_world():
    #return 'Hello world!'
#############################TEST######################################
def hair_colors():
    names = ['bob', 'sally', 'jane',]
    color = ['black', 'red', 'blonde']
    descriptions = []
    for x in names:
        descriptions.append(f'{x} has {random.choice(color)} hair!')
    return f'{descriptions}'
    