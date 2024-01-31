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
#### Counting Total Weather Stations
```python
# Design a query to calculate the total number stations in the dataset
total_stations = session.query(func.count(station.station.distinct())).scalar()

print("Total number of stations:", total_stations)
```
This code segment is designed to determine the total number of distinct weather stations in the dataset. By utilizing a SQLAlchemy query with `func.count`, we count the unique instances of the `station` identifier in the station table. The `scalar()` method is then used to extract this count as a single value, which we store in `total_stations`. Finally, we output this value, giving us a clear understanding of the number of unique weather stations contributing to our dataset.
#### Identifying the Most Active Weather Stations
```python
# Design a query to find the most active stations (i.e. what stations have the most rows?)
# List the stations and the counts in descending order.
most_active_stations = session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
for station, count in most_active_stations:
    print(f"Station: {station}, Count: {count}")
```
In this code, we design a query to determine the most active weather stations, defined by the frequency of their data entries. The query counts the number of occurrences of each station in the `measurement` table, groups them by station ID, and then orders the results in descending order based on these counts. The `all()` method retrieves the entire result set, which we then iterate through. For each station, we print its ID along with its respective data entry count, effectively listing the stations from most to least active. This provides valuable insights into which stations have the most comprehensive data records in our dataset.
#### Analyzing Temperature Data of the Most Active Station
```python
# Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
temperatures = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.station == 'USC00519281').all()
lowest_temp, highest_temp, average_temp = temperatures[0]
station_id = 'USC00519281'
print(f"Station ID: {station_id}")
print(f"Lowest Temperature: {lowest_temp}")
print(f"Highest Temperature: {highest_temp}")
print(f"Average Temperature: {average_temp:.2f}")
```
This snippet focuses on analyzing temperature data for the most active station, identified as 'USC00519281'. We calculate the lowest, highest, and average temperatures recorded at this station by executing a SQLAlchemy query, which utilizes functions like `func.min`, `func.max`, and `func.avg` on the `tobs` (temperature observations) column. After retrieving these values, we assign them to respective variables for clarity and display them. This provides a detailed snapshot of the temperature range and typical conditions at the station, encapsulating key climatic information for this specific location in our dataset.
#### Temperature Histogram for the Most Active Station
```python
# Using the most active station id
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
temperature_data = session.query(measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= one_year_ago).all()
most_active_station = pd.DataFrame(temperature_data)
most_active_station.plot(kind = 'hist', figsize = (10,6), bins=12)
plt.title(f"Temperature Observations for Station USC00519281 (Last 12 Months)")
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()
```
Here, we query and visualize the last 12 months of temperature data for the most active station, 'USC00519281'. First, we retrieve the temperature observations (tobs) for this specific station since the date calculated as one year ago. This data is then transformed into a Pandas DataFrame for ease of manipulation. Utilizing Pandas' plotting capabilities, we create a histogram with 12 bins to represent the frequency distribution of temperatures observed at this station over the past year. The plot is appropriately titled and labeled, providing a clear and informative visualization of the temperature trends and variations at the most active station in our dataset.
#### Closing the Database Session
```python
# Close Session
session.close()
```
This line of code is crucial as it closes the open database session. Closing the session is an important best practice in database management as it releases the resources held by the session, ensuring there are no lingering connections or transactions. This helps maintain the integrity of the data and the efficiency of the database interactions within your application.
### Part 2: Design Your Climate App
#### Setting Up Flask App
```python
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
```
This code block sets the foundation for a Flask application that interacts with a database. First, essential libraries such as NumPy and datetime are imported for numerical operations and handling date/time respectively. SQLAlchemy tools are then imported for Object Relational Mapping (ORM) and database interaction, which includes `create_engine` for connecting to the database, `automap_base` for reflecting the database tables into models, `Session` for managing database transactions, and `func` for SQL function operations. Finally, Flask and its `jsonify` function are imported, setting the stage to create a web application that can serve data from the database in a structured JSON format, facilitating easy access and manipulation of the data through web APIs.
#### Database Configuration for Flask App
```python
# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)
measurement = Base.classes.measurement
Station = Base.classes.station
```
In this section of the Flask application, we're setting up the database connection and preparing our ORM models. We start by creating an `engine` that connects to the `hawaii.sqlite` database stored in the `Resources` directory. The `automap_base` function from SQLAlchemy is then used to create a base class for an automap schema, which helps in reflecting the database tables into Python classes automatically. With `Base.prepare`, the database schema is loaded into SQLAlchemy, making the table structures accessible as classes. We then save references to these classes (`measurement` and `Station`) for easy interaction with the corresponding tables in the database. This setup is integral for the subsequent data retrieval and manipulation within our Flask application.
#### Flask Application Initialization and Utility Functions
```python
# Flask Setup
app = Flask(__name__)

def get_year_ago_date():
    """Helper function to get the date one year ago from the last record."""
    session = Session(engine)
    latest_date = session.query(func.max(measurement.date)).scalar()
    session.close()
    return dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=365)

def valid_date(datestr):
    """Helper function to check if a date string is valid."""
    try:
        dt.datetime.strptime(datestr, "%Y-%m-%d")
        return True
    except ValueError:
        return False
```
This code initializes our Flask application and defines two utility functions to assist with date handling:

1. **Flask App Initialization**: We begin by creating an instance of the Flask class. This instance, `app`, becomes our WSGI application which we can use to handle requests and responses.

2. **get_year_ago_date Function**: This helper function calculates the date one year before the most recent record in our database. It opens a session, queries the latest date from the `measurement` table, closes the session, and then computes the date one year prior to this latest date. This is particularly useful for analyses that require a year's worth of data leading up to the most recent entry.

3. **valid_date Function**: This function checks the validity of a date string. It attempts to parse the provided string as a date in the format 'YYYY-MM-DD'. If successful, it returns `True`, indicating the string is a valid date; otherwise, it returns `False`. This is essential for validating user input in routes where dates are required parameters.
#### Homepage Setup for Hawaii Climate Analysis API
```python
# Flask Routes
@app.route("/")
def homepage():
    """List all available API routes."""
    return """
    <html>
        <head>
            <title>Hawaii Climate Analysis API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #dae8fc; }
                h1 { color: #333366; }
                p { color: #333366; font-weight: bold;}
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                a { color: color: #333366; text-decoration: none; }
                a:hover { color: #0077cc; text-decoration: underline; }
                label { color: #333366; font-weight: bold; }
                button {
                    background-color: #333366; 
                    color: white; 
                    border: none;
                    padding: 10px 15px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 5px; 
                }
            </style>
            <script>
                function redirectToStartRoute() {
                    var startDate = document.getElementById('start-date').value;
                    if (startDate) {
                        window.location.href = '/api/v1.0/' + startDate;
                    } else {
                        alert('Please enter a start date.');
                    }
                }

                function redirectToStartEndRoute() {
                    var startDate = document.getElementById('start-end-date').value;
                    var endDate = document.getElementById('end-date').value;
                    if (startDate && endDate) {
                        window.location.href = '/api/v1.0/' + startDate + '/' + endDate;
                    } else {
                        alert('Please enter both start and end dates.');
                    }
                }
            </script>
        </head>
        <body>
            <h1>Welcome to the Hawaii Climate Analysis API</h1>
            <p>Available Routes:</p>
            <ul>
                <li><a href="/api/v1.0/precipitation">Precipitation Data for One Year</a></li>
                <li><a href="/api/v1.0/stations">List of Active Weather Stations</a></li>
                <li><a href="/api/v1.0/tobs">Temperature Observations of the Most-Active Station for One Year</a></li>
                <li>
                    <label for="start-date">Select a date to get temperature data:</label>
                    <input type="date" id="start-date" min="2010-01-01" max="2017-08-23">
                    <button onclick="redirectToStartRoute()">Get Start Date Data</button>
                </li>
                <li>
                    <label for="start-end-date">Select a date range to get temperature data: Start Date:</label>
                    <input type="date" id="start-end-date" min="2010-01-01" max="2017-08-23">
                    <label for="end-date">End Date:</label>
                    <input type="date" id="end-date" min="2010-01-01" max="2017-08-23">
                    <button onclick="redirectToStartEndRoute()">Get Start-End Date Data</button>
                </li>
            </ul>
        </body>
    </html>
    """
```
The `/` route in your Flask app serves as the homepage and provides a user-friendly interface listing all available API routes. It features:

1. **Styling and Layout**: The page is styled with CSS for a clean and organized look. The body has a light blue background (`#dae8fc`), and main titles are colored in a deep blue (`#333366`). Links and buttons are styled consistently to enhance user experience.

2. **Interactive Elements**: Two date input fields and corresponding buttons are included, allowing users to select dates for temperature data queries. JavaScript functions `redirectToStartRoute()` and `redirectToStartEndRoute()` handle button clicks, redirecting to the appropriate routes with the selected dates.

3. **Navigation Links**: The page offers easy navigation to different data endpoints:
	* `/api/v1.0/precipitation`: Shows precipitation data for the last year.
	* `/api/v1.0/stations`: Lists all active weather stations.
	* `/api/v1.0/tobs`: Displays temperature observations for the most active station over the last year.

This homepage effectively serves as a guide for users to explore various aspects of the Hawaii Climate Analysis API, making the data accessible and easy to interact with.
#### Precipitation Data Retrieval Endpoint
```python
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    year_ago_date = get_year_ago_date()
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago_date).all()
    session.close()

    if not results:
        return jsonify({"error": "No precipitation data found."})

    # Format the results as a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)
```
This route in the Flask app, `/api/v1.0/precipitation`, fetches and returns the last year's precipitation data from the database. It utilizes a SQLAlchemy session to connect to the SQLite database and query the `measurement` table. The `get_year_ago_date()` function is used to determine the date one year prior to the most recent record, ensuring the data retrieved is for the last 12 months. The results are then formatted into a dictionary where each date is mapped to its corresponding precipitation value. If no data is found, a JSON response with an error message is returned. This endpoint provides an API access point for clients to retrieve historical precipitation data for climate analysis.
#### Weather Stations Data Endpoint
```python
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Query to retrieve all station data
    stations_results = session.query(Station.name, Station.station, Station.elevation, Station.latitude, Station.longitude).all()
    session.close()

    if not stations_results:
        return jsonify({"error": "No station data found."})

    # Format the results as a list of dictionaries
    stations_data = [{"name": name, "station": station, "elevation": elevation, "latitude": latitude, "longitude": longitude} for name, station, elevation, latitude, longitude in stations_results]

    return jsonify(stations_data)
```
This section of the Flask app, accessible via `/api/v1.0/stations`, handles the retrieval of weather station data. The route establishes a session with the SQLite database to query the `Station` table, fetching details such as station name, ID, elevation, latitude, and longitude. The data, if found, is structured into a list of dictionaries, each representing a station. This format is ideal for JSON serialization, facilitating easy consumption by clients. Should no data be available, a JSON-formatted error message is returned. This endpoint is crucial for providing comprehensive information about each weather station involved in the climate analysis.
#### Temperature Observations Endpoint
```python
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    year_ago_date = get_year_ago_date()

    # Query to retrieve temperature observations for the most active station for the last year
    tobs_results = session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= year_ago_date).all()
    session.close()

    if not tobs_results:
        return jsonify({"error": "No temperature observation data found."})

    # Format the results as a list of dictionaries
    tobs_data = [{"date": date, "temperature": tobs} for date, tobs in tobs_results]

    return jsonify(tobs_data)
```
The `/api/v1.0/tobs` route of the Flask app is dedicated to providing temperature observation data (TOBS) for the most active weather station over the past year. It first calculates the date one year prior to the latest record using the `get_year_ago_date()` function. A query is then executed to retrieve temperature data (`tobs`) along with their respective dates from the `measurement` table, specifically for station 'USC00519281'. The results are structured into a JSON-friendly format—a list of dictionaries, each entry pairing a date with its corresponding temperature. In case no data is found, a JSON error message is returned. This endpoint is particularly useful for users interested in detailed temperature trends of the most actively reporting station in the Hawaii climate dataset.

