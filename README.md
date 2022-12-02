# Sqlalchemy-Challenge

## Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

1. Use the SQLAlchemy create_engine() function to connect to your SQLite database.

<img width="1011" alt="Screenshot 2022-12-02 at 8 27 14 AM" src="https://user-images.githubusercontent.com/112406455/205315515-3c5fe8a9-cfda-4ac4-9d90-61154beb4b9e.png">

2. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

<img width="1009" alt="Screenshot 2022-12-02 at 8 27 45 AM" src="https://user-images.githubusercontent.com/112406455/205316119-f3fdd98a-1689-4e28-9c2c-d5562b1a5fc5.png">

3. Link Python to the database by creating a SQLAlchemy session.

<img width="1009" alt="Screenshot 2022-12-02 at 8 32 50 AM" src="https://user-images.githubusercontent.com/112406455/205316572-dce8f853-b315-4e01-94d9-77980a0a52d6.png">

4. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

### Precipitation Analysis

1. Find the most recent date in the dataset.

<img width="1011" alt="Screenshot 2022-12-02 at 8 35 13 AM" src="https://user-images.githubusercontent.com/112406455/205316906-a86a9878-88fa-4aca-bcaf-98ca736d004b.png">

2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

<img width="526" alt="Screenshot 2022-12-02 at 8 38 22 AM" src="https://user-images.githubusercontent.com/112406455/205317648-67d5a061-43e3-431c-a6d4-1fb1b21dad57.png">

3. Select only the "date" and "prcp" values.

<img width="648" alt="Screenshot 2022-12-02 at 8 39 59 AM" src="https://user-images.githubusercontent.com/112406455/205317880-266d02d8-4402-4540-893d-5edc84bef678.png">

4. Load the query results into a Pandas DataFrame, and set the index to the "date" column.

<img width="901" alt="Screenshot 2022-12-02 at 8 41 04 AM" src="https://user-images.githubusercontent.com/112406455/205318350-cd8bb144-89c9-493b-90e5-139be43c26cd.png">

5. Sort the DataFrame values by "date".

<img width="545" alt="Screenshot 2022-12-02 at 8 43 22 AM" src="https://user-images.githubusercontent.com/112406455/205318575-f071b12f-8467-4367-b0be-f60781cd8329.png">

6. Plot the results by using the DataFrame plot method

<img width="849" alt="Screenshot 2022-12-02 at 8 41 56 AM" src="https://user-images.githubusercontent.com/112406455/205319041-6255dff2-a0bd-4cf3-a938-49409edd69eb.png">

7. Use Pandas to print the summary statistics for the precipitation data.

<img width="1011" alt="Screenshot 2022-12-02 at 8 47 02 AM" src="https://user-images.githubusercontent.com/112406455/205319305-94295066-8b81-4d31-aecc-d83126b44768.png">

### Station Analysis

1. Design a query to calculate the total number of stations in the dataset.

<img width="1011" alt="Screenshot 2022-12-02 at 8 56 03 AM" src="https://user-images.githubusercontent.com/112406455/205321522-4f23d2ba-2367-4c5c-9d3b-091794848a63.png">

2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

* List the stations and observation counts in descending order.

<img width="1010" alt="Screenshot 2022-12-02 at 8 56 19 AM" src="https://user-images.githubusercontent.com/112406455/205322059-6ea1e951-13e6-47c2-b416-335340436a31.png">

* Answer the following question: which station id has the greatest number of observations? 
Station USC00519281 has the greatest number of observations.  

3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

<img width="1011" alt="Screenshot 2022-12-02 at 8 56 26 AM" src="https://user-images.githubusercontent.com/112406455/205322721-637a2637-1ffa-4dca-8e15-cdb97d669cb5.png">

4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

* Filter by the station that has the greatest number of observations.

* Query the previous 12 months of TOBS data for that station.

<img width="1010" alt="Screenshot 2022-12-02 at 9 04 29 AM" src="https://user-images.githubusercontent.com/112406455/205323598-a044799b-a127-4838-a333-aee6dfadc32c.png">

* Plot the results as a histogram with bins=12

<img width="1006" alt="Screenshot 2022-12-02 at 9 06 28 AM" src="https://user-images.githubusercontent.com/112406455/205323957-77bd6955-3579-4d0e-8069-885e2423ea8c.png">

5. Close your session.

<img width="1010" alt="Screenshot 2022-12-02 at 9 06 45 AM" src="https://user-images.githubusercontent.com/112406455/205324177-0ee9a706-66bf-4b19-b15b-d25d9d228f54.png">

## Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

### 1. /

* Start at the homepage.

<img width="1067" alt="Screenshot 2022-12-02 at 9 38 47 AM" src="https://user-images.githubusercontent.com/112406455/205330075-02b5d7a9-0186-4ce0-bc86-474542a853e7.png">

* List all the available routes.

<img width="1440" alt="Screenshot 2022-12-02 at 10 03 25 AM" src="https://user-images.githubusercontent.com/112406455/205334655-86ab1367-776b-4c42-900c-683981da7006.png">

### 2. /api/v1.0/precipitation

* Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

<img width="1061" alt="Screenshot 2022-12-02 at 9 39 57 AM" src="https://user-images.githubusercontent.com/112406455/205330477-24a15e18-ced4-410d-a411-e39a01348c8b.png">

* Return the JSON representation of your dictionary.

<img width="1440" alt="Screenshot 2022-12-02 at 9 59 58 AM" src="https://user-images.githubusercontent.com/112406455/205334217-78b5eb9a-70b9-48f3-83cc-5bb797f449a8.png">

### 3. /api/v1.0/stations

<img width="976" alt="Screenshot 2022-12-02 at 9 42 54 AM" src="https://user-images.githubusercontent.com/112406455/205330940-63663419-abfb-4bdc-a7ca-e830802e5ccb.png">

* Return a JSON list of stations from the dataset.

<img width="1440" alt="Screenshot 2022-12-02 at 9 59 08 AM" src="https://user-images.githubusercontent.com/112406455/205333814-bef3f528-c7e2-4cf1-be98-1f3ed85f9621.png">

### 4. /api/v1.0/tobs

* Query the dates and temperature observations of the most-active station for the previous year of data.

<img width="1063" alt="Screenshot 2022-12-02 at 9 45 00 AM" src="https://user-images.githubusercontent.com/112406455/205331322-a8f401cc-87b0-4641-8e82-ca4fc2872da0.png">

* Return a JSON list of temperature observations for the previous year.

<img width="1440" alt="Screenshot 2022-12-02 at 9 57 03 AM" src="https://user-images.githubusercontent.com/112406455/205333503-6c1ed9cf-5a33-42fe-ae6d-6990a5242bc7.png">

### 5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

* Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

* For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

<img width="1065" alt="Screenshot 2022-12-02 at 9 47 22 AM" src="https://user-images.githubusercontent.com/112406455/205331989-554c07e9-b839-4118-8478-05580c7ca0b4.png">

<img width="1440" alt="Screenshot 2022-12-02 at 9 55 15 AM" src="https://user-images.githubusercontent.com/112406455/205333052-0aaaebb4-b054-48a7-95ff-1a4da41c874a.png">

* For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

<img width="1064" alt="Screenshot 2022-12-02 at 9 47 29 AM" src="https://user-images.githubusercontent.com/112406455/205332135-17d43e9e-1d81-4b67-994f-f19bb531be03.png">

<img width="1440" alt="Screenshot 2022-12-02 at 9 54 08 AM" src="https://user-images.githubusercontent.com/112406455/205332909-f5cc337f-cd75-424c-b926-73d3fc8997b5.png">

## Code Execution Instructions:
* Download the repository onto you computer.
* Open the "climate.ipynb" file in a Jupyter Notebook.
* Select the "Kernel" tab and click "Restart Kernel and Clear all Outputs".
* Then proceed to hit shift + enter to cycle through the script cell by cell.
* The code is accompanied by an outline to walk you through the process step by step.
* Open the app.py file to see how the Flask application is created.
* To run the application, first open up a terminal or git bash window.
* Navigate to the SurfsUp folder.
* Once inside the SurfsUp folder run the program by typing in "python app.py"
* Then copy the link where it says running on: "http://127.0.0.1:5000/" and paste it in any web browser of your chosing.
* The landing page will pop up with all available routes
* Then just copy the extensions and paste at the end of the url to navigate to each page. 


## References
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1.

© 2022 edX Boot Camps LLC



