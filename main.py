import mysql.connector
from datetime import datetime, timedelta

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='swym'
)
cursor = conn.cursor()

def find_midnight_arrivals(station_code):
    query = '''
    SELECT TrainNo, TrainName
    FROM TrainStops
    WHERE StationCode = %s AND ArrivalTime = '00:00:00'
    '''
    cursor.execute(query, (station_code,))
    midnight_arrivals = cursor.fetchall()
    return midnight_arrivals

# Example usage
midnight_arrivals = find_midnight_arrivals('SWV')
print("Trains arriving at midnight:", midnight_arrivals)
