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

# Flask Routes
@app.route("/")
def homepage():
    """List all available API routes."""
    # Route descriptions
    routes = {
        "/api/v1.0/precipitation": "Precipitation Data for One Year",
        "/api/v1.0/stations": "List of Active Weather Stations",
        "/api/v1.0/tobs": "Temperature Observations of the Most-Active Station for One Year",
        "/api/v1.0/<start>": "The Min, Avg, and Max Temperature for a specified Start Date",
        "/api/v1.0/<start>/<end>": "The Min, Avg, and Max Temperatures for a specified Start and End Date"
    }
    # Formatting the routes for display
    return 'Welcome to the Hawaii Climate Analysis API!<br/>' + '<br/>'.join([f'{route}: {description}' for route, description in routes.items()])

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    year_ago_date = get_year_ago_date()
    results = session.query(measurement.date, measurement.prcp).filter(measurement.date >= year_ago_date).all()
    session.close()
    return jsonify({date: prcp for date, prcp in results})

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations = session.query(Station.name, Station.station, Station.elevation, Station.latitude, Station.longitude).all()
    session.close()
    return jsonify([{"Name": name, "Station ID": station, "Elevation": elevation, "Latitude": latitude, "Longitude": longitude} for name, station, elevation, latitude, longitude in stations])

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    year_ago_date = get_year_ago_date()
    active_station = session.query(measurement.tobs, measurement.date).filter(measurement.station == 'USC00519281').filter(measurement.date >= year_ago_date).all()
    session.close()
    return jsonify({date: temp for date, temp in active_station})

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    query_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start).all()
    session.close()
    min_temp, max_temp, avg_temp = query_results[0]
    return jsonify({"Start Date": start, "Minimum Temperature": min_temp, "Maximum Temperature": max_temp, "Average Temperature": avg_temp})

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    query_results = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).filter(measurement.date >= start, measurement.date <= end).all()
    session.close()
    min_temp, max_temp, avg_temp = query_results[0]
    return jsonify({"Start Date": start, "End Date": end, "Minimum Temperature": min_temp, "Maximum Temperature": max_temp, "Average Temperature": avg_temp})

if __name__ == '__main__':
    app.run(debug=True)
