import mysql.connector

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='swym',
        password='password',
        database='swym'
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print("Error:", err)
    exit(1)


def execute_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result, cursor.description


def find_midnight_arrivals(station_code):
    query = '''
    SELECT ts.TrainNo, t.TrainName
    FROM TrainStops ts
    JOIN Trains t ON ts.TrainNo = t.TrainNo
    WHERE ts.StationCode = %s AND ts.ArrivalTime = '00:00:00';
    '''
    cursor.execute(query, (station_code,))
    midnight_arrivals = cursor.fetchall()
    return midnight_arrivals


# Function to calculate halt times for trains
def display_halt_times():
    # Query to find halt times for trains
    query = '''
    SELECT ts.TrainNo, t.TrainName, ts.ArrivalTime, ts.DepartureTime,
    TIMEDIFF(ts.DepartureTime, ts.ArrivalTime) AS HaltTime
    FROM TrainStops ts
    JOIN Trains t ON ts.TrainNo = t.TrainNo
    ORDER BY HaltTime DESC;
    '''
    cursor.execute(query)
    halt_times = cursor.fetchall()
    return halt_times, cursor.description


def find_trains_between_stations(start_station, end_station):
    # Query to find trains between stations
    query = '''
    SELECT DISTINCT ts.TrainNo, t.TrainName
    FROM TrainStops ts
    JOIN Trains t ON ts.TrainNo = t.TrainNo
    WHERE ts.StationCode = %s OR ts.StationCode = %s;
    '''
    cursor.execute(query, (start_station, end_station))
    trains_between_stations = cursor.fetchall()
    return trains_between_stations

