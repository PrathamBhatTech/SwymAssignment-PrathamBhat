import streamlit as st
import mysql.connector
from datetime import datetime, timedelta

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
    SELECT TrainNo, TrainName
    FROM TrainStops
    WHERE StationCode = %s AND ArrivalTime = '00:00:00'
    '''
    cursor.execute(query, (station_code,))
    midnight_arrivals = cursor.fetchall()
    return midnight_arrivals

# Example usage
# midnight_arrivals = find_midnight_arrivals('SWV')
# print("Trains arriving at midnight:", midnight_arrivals)
