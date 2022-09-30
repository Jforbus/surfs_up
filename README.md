# surfs_up

## Project Overview
Investors have requested analysis of Weather Data in order to guide location selection for a new business venture, a surf and shake shop. Precipitation and temperature data for the desired location has been provided in an SQLite database, and investors have requested the summary statistics for temperatures from two months: June and December.  

### Resources
- Data Source: hawaii.sqlite
- Software: Python 3.7.1, VS Code 1.71.2, Jupyter Notebook 6.4.8, Pandas 1.4.3, SQLite3, SQLAlchemy 1.4.41

## Results
Two queries are written using the SQLAlchemy `extract()` function to collect all the temperature data for the selected months. The results of each query are then passed into a Pandas DataFrame, and the `describe()` function is used to generate the summary statistics for each. 

### June Temperature Summary
![jun_temps](https://github.com/Jforbus/surfs_up/blob/main/Resources/Jun_Temps.png)

### December Temperature Summary
![dec_temps](https://github.com/Jforbus/surfs_up/blob/main/Resources/Dec_Temps.png)


### Analysis
From the summary statistics we can discern three things:
'''
    * The December minumum temperature is relatively low compared to June's, while the maximum temperatures do not differ a meaningful amount. The temperature in this dataset shows the potential for temperature falloffs in December, but does not show a corresponding temperature spike in June.

    * The average temperatures for the two months are very close to being the same, with only 3 degrees difference in the mean. This shows relatively consistent temperatures in the two months, with slightly elevated temperatures in June as compared to December.

    * The standard deviation for the temperature data in both months is the same and relatively small, showing a tight grouping of the data. This corresponds with the range of our dataset being fairly limited. The temperature in the location measured does not vary wildy either within or between the two months measured.  
'''

## Summary
The temperature data for June and December suggests a positive outlook for the desired location, with consistent comfortable temperatures in both of the months measured. Two additional queries that could be written to gather additional data for the months of June and December and further expand the information provided by the analysis would be: A query to provide the summary statistics for precipitation in June, and a query to provide the summary statistics for precipitation in December. With this data we can further determine the viablity of the surf and shake shop in the selected location, as heavy rainfall in one of the months could indicate a potential business hazard. 
