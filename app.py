# Import Dependencies
################################################

# python
import datetime as dt
import numpy as np
import pandas as pd

# sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# flask
from flask import Flask, jsonify

################################################
# Set Up Database
################################################

# create engine to access database
engine = create_engine('sqlite:///hawaii.sqlite')

# reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references to classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create session link
session = Session(engine)

################################################
# Create Flask App
################################################

# create instance
app = Flask(__name__)

# define welcome route
@app.route('/')

# welcome function creating references to all other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')