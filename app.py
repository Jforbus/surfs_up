#dependency

from flask import Flask
import random
import numpy as np
import datetime as dt
import numpy as np
import pandas as pd
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import base64
from io import BytesIO
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
#def hair_colors():
    #names = ['bob', 'sally', 'jane',]
    #color = ['black', 'red', 'blonde']
    #descriptions = []
    #for x in names:
        #descriptions.append(f'{x} has {random.choice(color)} hair!')
    #return f'{descriptions}'
    
def chart():
    # create engine
    engine = create_engine('sqlite:///hawaii.sqlite')

    # reflect an existing database into a new model
    Base = automap_base()
    # reflect the tables
    Base.prepare(engine, reflect=True)
    
    # Save references to each table
    Measurement = Base.classes.measurement
    Station = Base.classes.station

    # Create our session (link) from Python to the DB
    session = Session(engine)


    ## use datetime to calculate date one year prior to selected date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores

    ## create variable to store results of query
    results = []

    # Use Pandas Plotting with Matplotlib to plot the data
    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
    df = pd.DataFrame(results, columns=['tobs'])
    df.plot.hist(bins=12)
    plt.tight_layout()
    
    buf = BytesIO()
    plt.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"