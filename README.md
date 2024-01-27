# Honolulu Climate Analysis and API Tool
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



