import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)
measurement = Base.classes.measurement
Station = Base.classes.station

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

# Flask Routes
@app.route("/")
def homepage():
    """List all available API routes."""
    return """
    <html>
        <head>
            <title>Hawaii Climate Analysis API</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                h1 { color: #333366; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                a { color: #0077cc; text-decoration: none; }
                a:hover { text-decoration: underline; }
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

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    year_ago_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago_date).all()
    session.close()

    if not results:
        return "<p>No precipitation data found.</p>"

    # Create HTML content with enhanced styling
    html = """
    <html>
    <head>
        <title>Precipitation Data</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #f4f4f4;
                text-align: center;
            }
            h1 {
                color: #333366;
            }
            table {
                margin: 20px auto;
                border-collapse: collapse;
                width: 80%;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #333366;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <h1>Precipitation Data for the Last Year</h1>
        <table>
            <tr>
                <th>Date</th>
                <th>Precipitation (inches)</th>
            </tr>
    """

    for date, prcp in results:
        prcp_display = prcp if prcp is not None else "N/A"  # Handle None values
        html += f"<tr><td>{date}</td><td>{prcp_display}</td></tr>"

    html += "</table></body></html>"
    return html

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Station.name, Station.station, Station.elevation, Station.latitude, Station.longitude).all()
    session.close()

    if not stations:
        return "<p>No station data found.</p>"

    # Create HTML content
    html = """
    <html>
    <head>
        <title>Weather Stations</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #f4f4f4;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            table {
                margin: 20px auto;
                border-collapse: collapse;
                width: 80%;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #333366;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <h1>List of Active Weather Stations</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Station ID</th>
                <th>Elevation</th>
                <th>Latitude</th>
                <th>Longitude</th>
            </tr>
    """

    for name, station, elevation, latitude, longitude in stations:
        html += f"<tr><td>{name}</td><td>{station}</td><td>{elevation}</td><td>{latitude}</td><td>{longitude}</td></tr>"

    html += "</table></body></html>"
    return html

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    year_ago_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    active_station = session.query(measurement.tobs, measurement.date).filter(measurement.station == 'USC00519281').filter(measurement.date >= year_ago_date).all()
    session.close()

    if not active_station:
        return "<p>No temperature observations found for the most active station.</p>"

    # Create HTML content with enhanced styling
    html = """
    <html>
    <head>
        <title>Temperature Observations</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background: #f4f4f4;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            table {
                margin: 20px auto;
                border-collapse: collapse;
                width: 80%;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #333366;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <h1>Temperature Observations for the Most Active Station (One Year)</h1>
        <table>
            <tr>
                <th>Date</th>
                <th>Temperature (°F)</th>
            </tr>
    """

    for temp, date in active_station:
        html += f"<tr><td>{date}</td><td>{temp}°F</td></tr>"

    html += "</table></body></html>"
    return html


@app.route("/api/v1.0/<start>")
def start(start):
    if not valid_date(start):
        return "<p>Invalid start date format. Use YYYY-MM-DD.</p>"

    session = Session(engine)
    query_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).all()
    session.close()

    if not query_results:
        return "<p>No temperature data found for the given start date.</p>"

    min_temp, max_temp, avg_temp = query_results[0]

    html = "<html><head><title>Temperature Statistics</title></head><body>"
    html += f"<h1>Temperature Statistics from {start}</h1>"
    html += "<ul>"
    html += f"<li>Minimum Temperature: {min_temp}°F</li>"
    html += f"<li>Maximum Temperature: {max_temp}°F</li>"
    html += f"<li>Average Temperature: {avg_temp:.2f}°F</li>"
    html += "</ul></body></html>"

    return html

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    if not valid_date(start) or not valid_date(end):
        return "<p>Invalid date format. Use YYYY-MM-DD.</p>"

    session = Session(engine)
    query_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start, measurement.date <= end).all()
    session.close()

    if not query_results:
        return "<p>No temperature data found for the given date range.</p>"

    min_temp, max_temp, avg_temp = query_results[0]

    html = "<html><head><title>Temperature Range Statistics</title></head><body>"
    html += f"<h1>Temperature Statistics from {start} to {end}</h1>"
    html += "<ul>"
    html += f"<li>Minimum Temperature: {min_temp}°F</li>"
    html += f"<li>Maximum Temperature: {max_temp}°F</li>"
    html += f"<li>Average Temperature: {avg_temp:.2f}°F</li>"
    html += "</ul></body></html>"

    return html

if __name__ == '__main__':
    app.run(debug=True)
