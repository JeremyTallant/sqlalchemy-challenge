# Honolulu Climate Analysis and API Tool Project
![image](https://user-images.githubusercontent.com/112406455/210906725-e8a875aa-4f0f-4372-8741-05269db7d9d7.png)
## Background
In the Honolulu Climate Analysis and API Tool project, a comprehensive exploration and analysis of climate data for Honolulu, Hawaii, was conducted to assist in planning a long holiday vacation. Utilizing Python, SQLAlchemy, Pandas, and Matplotlib, the project delved into a detailed climate database, employing SQLAlchemy ORM queries for data extraction. The analysis began with a thorough precipitation study, tracing back 12 months from the most recent data point in the dataset, and involving meticulous data loading and plotting to visualize precipitation trends. This was followed by an extensive station analysis, focusing on identifying the most active weather stations and examining their observation counts. Critical temperature metrics such as the lowest, highest, and average temperatures were calculated, particularly for the station with the highest frequency of observations. The project culminated in the development of a Flask API, offering diverse endpoints to access climate data, including routes for precipitation data, station listings, temperature observations, and temperature statistics for specific date ranges. This Flask API serves as a versatile tool, providing JSON formatted responses for seamless integration with other applications, thereby elevating the project's utility for effective trip planning and broader climate research endeavors.
## Objective
### Part 1: Analyze and Explore the Climate Data
The primary objective of Part 1 is to perform a thorough climate analysis and data exploration of Honolulu, Hawaii, in preparation for a holiday vacation. Using Python, SQLAlchemy, Pandas, and Matplotlib, this part involves a detailed examination of a climate database, emphasizing precipitation and station analysis. The process includes:
* Connecting to the SQLite database using SQLAlchemy `create_engine()`.
* Reflecting tables into classes using `automap_base()`, focusing on `station` and `measurement`.
* Creating and closing a SQLAlchemy session to link Python to the database.
* Conducting a precipitation analysis by querying the last 12 months of data, loading the results into a Pandas DataFrame, and visualizing the data through plotting.
* Performing a station analysis to determine the total number of stations, identifying the most active stations, and calculating temperature statistics (lowest, highest, and average) for the most active station.
### Part 2: Design Your Climate App
The objective of Part 2 is to develop a Flask API based on the findings and queries from the initial analysis. This part of the project involves creating a user-friendly API with the following capabilities:
* Presenting a homepage that lists all available API routes.
* Offering an endpoint (`/api/v1.0/precipitation`) to retrieve and return the last 12 months of precipitation data in JSON format.
* Providing a route (`/api/v1.0/stations`) to return a JSON list of all weather stations in the dataset.
* Creating an endpoint (`/api/v1.0/tobs`) to query and return a JSON list of temperature observations for the most active station over the previous year.
* Implementing routes (`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`) to return JSON lists of temperature statistics for specified start and/or end date ranges.

This comprehensive analysis and API development aim to equip users with insightful climate data and easy access to relevant information for planning a delightful vacation in Honolulu.
## Data
The Honolulu Climate Analysis and API Tool project utilizes two primary data sources stored in CSV files, which are then integrated into a SQLite database (`hawaii.sqlite`) for streamlined querying and analysis:
1. **Hawaii Measurements (hawaii_measurements.csv)**: This dataset comprises detailed daily climate measurements from various stations across Hawaii. Key columns in this dataset include:
	* `station`: Identifier for the weather station.
	* `date`: The date of observation.
	* `prcp`: Daily precipitation in inches.
	* `tobs`: Temperature observed at the station on a given day (in Fahrenheit).

Example entries from `hawaii_measurements.csv`:
```csv
station,date,prcp,tobs
USC00519397,2010-01-01,0.08,65
USC00519397,2010-01-02,0,63
USC00519397,2010-01-03,0,74
```
2. **Hawaii Stations (hawaii_stations.csv)**: This dataset contains information about each weather station in Hawaii. The columns include:
	* `station`: Unique identifier of the weather station.
	* `name`: Name and location of the station.
	* `latitude`: Geographic latitude.
	* `longitude`: Geographic longitude.
	* `elevation`: Elevation above sea level.

Example entries from `hawaii_stations.csv`:
```csv
station,name,latitude,longitude,elevation
USC00519397,"WAIKIKI 717.2, HI US",21.2716,-157.8168,3
USC00513117,"KANEOHE 838.1, HI US",21.4234,-157.8015,14.6
```
The datasets were curated from the Global Historical Climatology Network-Daily Database (Menne et al., 2012). The comprehensive nature of these datasets facilitates a robust and in-depth analysis of Hawaii's climate, providing valuable insights for the planning of a holiday vacation in Honolulu.

The `hawaii.sqlite` database consolidates these datasets, offering a unified platform for executing complex SQL queries via SQLAlchemy, enabling efficient data retrieval for analysis and visualization.
## Implementation
This section delves into the implementation details of the Honolulu Climate Analysis and API Tool project, showcasing the technical methodologies and tools utilized to transform raw climate data into actionable insights. It outlines the step-by-step process of data extraction, analysis, and API development, providing a comprehensive overview of how Python, SQLAlchemy, and Flask were employed to analyze climate patterns and create an interactive data access platform.
### Part 1: Analyze and Explore the Climate Data
#### Matplotlib Configuration for Inline Visualization
```python
%matplotlib inline
%config InlineBackend.figure_format = 'svg'
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
```
Let's begin by configuring Matplotlib to suit our visualization needs within the Jupyter Notebook. By setting it to inline mode, our plots will display directly in the notebook. We also adopt the 'fivethirtyeight' style – known for its clean and visually appealing graphs. Additionally, we opt for SVG format for our output figures, ensuring they are sharp and scalable, enhancing both the quality and clarity of our visual data representations.
#### Essential Library Imports
```python
import numpy as np
import pandas as pd
import datetime as dt
```
Next up, we import the core libraries that will power our data analysis. We bring in NumPy for efficient numerical computations, Pandas for sophisticated data manipulation and exploration, and the datetime module for handling all date and time-related tasks. These libraries lay the groundwork for our journey through the project's data processing and analysis phases.
#### Setting Up SQLAlchemy for Database Interaction
```python
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
```
Here, we set the stage for interacting with our database using SQLAlchemy, a comprehensive set of Python tools for working with databases. We import the necessary components: `create_engine` to connect to our database, `automap_base` to reflect the database tables into models, `Session` to establish a link for database transactions, and `func` for SQL function operations. This setup is crucial for mapping our database schema into Python objects and executing database operations seamlessly within our analysis.
#### Creating a Database Engine
```python
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
```
Now, we create an engine to connect to the `hawaii.sqlite` database. This engine acts as the primary access point for our database, allowing us to execute SQL queries and access the data stored in `Resources/hawaii.sqlite`. With this connection established, we're ready to dive into the data and start our exploration.
#### Reflecting Database Schema into Models
```python
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
```
In this step, we utilize SQLAlchemy's `automap_base` to reflect our existing database schema into a new model. This automatic mapping translates the `hawaii.sqlite` database tables into Python classes, creating a clear and direct correspondence between the database structure and our Python code. After establishing the base model, we call `Base.prepare` with the engine we created, setting `reflect=True` to introspect the database tables and create mapped classes. This reflection process is crucial for enabling an ORM-based approach to interact with our database in a Pythonic way.
#### Viewing Reflected Classes
```python
# View all of the classes that automap found
Base.classes.keys()
```
Here, we're leveraging the `Base.classes.keys()` method to list all the classes that SQLAlchemy's automapper has discovered in the database. This step essentially shows us the names of the tables that have been automatically mapped to Python classes, providing a clear view of what we're working with and ensuring that our database schema has been accurately reflected into our Python environment. It's an essential checkpoint to verify that our ORM setup correctly recognizes the database structure.
#### Storing Table References
```python
# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station
```
Having reflected our database, we now save references to each table for easy access. We assign `Base.classes.measurement` to `measurement` and `Base.classes.station` to `station`. This creates convenient Python variables representing each table in our database, allowing us to interact with them directly in our upcoming queries. This step simplifies our code and makes our interactions with the `measurement` and `station` tables more intuitive.
#### Establishing a Database Session
```python
# Create our session (link) from Python to the DB
session = Session(engine)
```
With this code, we're creating a session, which is our gateway for communicating with the database. The `Session` object, instantiated with the `engine` we previously created, establishes a link from Python to our database. This session will be used to execute queries and interact with the database, enabling us to retrieve, add, or manipulate data within our `hawaii.sqlite` database directly from Python. Think of it as opening a conversation with our database, ready to send and receive information.
#### Retrieving the Most Recent Date from the Database
```python
# Find the most recent date in the data set.
most_recent_date = session.query(func.max(measurement.date)).scalar()
print("Most Recent Date:", most_recent_date)
```
This code segment is focused on extracting the most recent date available in our dataset. We achieve this by executing a query through our established session, where we use `func.max(measurement.date)` to find the latest date in the `measurement` table. The `scalar()` method then fetches this single value, which we store in `most_recent_date`. Finally, we print out this date, giving us a clear understanding of the up-to-date extent of our climate data, a crucial piece of information for subsequent analysis.
#### Visualizing Yearly Precipitation Data
```python
# Design a query to retrieve the last 12 months of precipitation data and plot the results. 
# Starting from the most recent data point in the database. 

# Calculate the date one year from the last date in data set.
one_year_ago = dt.datetime.strptime(most_recent_date, '%Y-%m-%d') - dt.timedelta(days=365)

# Perform a query to retrieve the data and precipitation scores
precipitation_data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= one_year_ago).order_by(measurement.date).all()

# Save the query results as a Pandas DataFrame and set the index to the date column
df = pd.DataFrame(precipitation_data, columns=['date', 'precipitation'])
df.set_index('date', inplace=True)

# Sort the dataframe by date
df = df.sort_index()

# Use Pandas Plotting with Matplotlib to plot the data
df.plot(rot=90,figsize=(12,6), legend=False)
plt.title("Precipitation Over the Last 12 Months")
plt.ylabel("Inches")
plt.xlabel("Date")
plt.show()
```
In this section, we query the last 12 months of precipitation data from the `measurement` table, starting from the most recent date in the dataset. After calculating the date one year back, we retrieve and sort this data chronologically. It's then transformed into a Pandas DataFrame with dates as the index. Using Pandas and Matplotlib, we plot these precipitation trends, providing a clear, visual understanding of the rainfall patterns over the past year, essential for analyzing the climate of the region.
#### Computing Summary Statistics for Precipitation
```python
# Use Pandas to calculate the summary statistics for the precipitation data
df.describe()
```
This line of code utilizes Pandas' `describe()` function to compute summary statistics for the precipitation data stored in our DataFrame `df`. This function generates descriptive statistics including mean, standard deviation, minimum, maximum, and the quartile values for the dataset, offering a comprehensive statistical overview of the precipitation trends over the last year.
