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

##

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

##

# define precipitation route
@app.route("/api/v1.0/precipitation")

# precipitation function
def precipitation():

    # select year of precip data 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # write query
    precipitation = session.query(Measurement.date, Measurement.prcp).\
            filter(Measurement.date >= prev_year).all()

    # create dict from query
    precip = {date: prcp for date, prcp in precipitation}
    
    # return precip dict in json format
    return jsonify(precip)

##

# define stations route
@app.route('/api/v1.0/stations')

# stations function
def stations():
    
    # write query
    results = session.query(Station.station).all()

    # create array from results
    stations = list(np.ravel(results))

    # return station data in json format
    return jsonify(stations=stations)
    
##

# define tobs route
@app.route('/api/v1.0/tobs')

# tobs function
def temp_monthly():
    # select year for data 
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    #write query
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    
    # create list from query
    temps = list(np.ravel(results))

    return jsonify(temps=temps)
##

# define temp route

# temp function


