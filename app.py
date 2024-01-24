from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt

app = Flask(__name__)

# Database setup
engine = create_engine("sqlite:///path_to_your_hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Home route
@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    # Query for the last year of precipitation data
    one_year_ago = dt.datetime.now() - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    session.close()

    # Convert to dictionary
    precipitation_dict = {date: prcp for date, prcp in results}
    return jsonify(precipitation_dict)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    stations_list = [station[0] for station in results]
    return jsonify(stations_list)

# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    # Query for the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    one_year_ago = dt.datetime.now() - dt.timedelta(days=365)
    # Query the last year of temperature observation data for this station
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station, Measurement.date >= one_year_ago).all()
    session.close()

    tobs_list = [{date: tobs} for date, tobs in results]
    return jsonify(tobs_list)

# Start route
@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()

    # Unpack the `min`, `avg`, and `max` temperatures
    min_temp, avg_temp, max_temp = results[0]
    return jsonify({"TMIN": min_temp, "TAVG": avg_temp, "TMAX": max_temp})

# Start-End route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    session.close()

    min_temp, avg_temp, max_temp = results[0]
    return jsonify({"TMIN": min_temp, "TAVG": avg_temp, "TMAX": max_temp})

if __name__ == '__main__':
    app.run(debug=True)
