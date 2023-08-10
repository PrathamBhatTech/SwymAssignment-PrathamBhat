import streamlit as st
from func import queries
import pandas as pd


# Streamlit app
def main():
    st.title("Indian Railways Timetable")

    # Sidebar options
    question = st.sidebar.selectbox("Select a Question",
                                    [
                                        "Select a Question from the Sidebar",
                                        "Find Trains Arriving at Midnight",
                                        "Halt Times",
                                        "Find Trains between Stations",
                                        "Query Sandbox"
                                    ]
                                    )

    if question == "Select a Question from the Sidebar":
        message = '''
This app is a demo of the Indian Railways Timetable database.
The database is hosted on a MySQL server and is queried using Python.
The database contains the following tables:
- Stations
- Trains
- TrainStops

The following questions can be answered using the database:
- Find Trains Arriving at Midnight
- Find Trains between Stations

A query sandbox is also provided to run custom queries on the database.

The source code for this app can be found [here](https://github.com/PrathamBhatTech/SwymAssignment-PrathamBhat).
To see the questions and the queries, click on the arrow on the left.
    '''
        st.write(message)

    elif question == "Find Trains Arriving at Midnight":
        st.sidebar.write("### Question 1")
        station_code = st.text_input("Enter Station Code", "SWV")
        if st.button("Find Trains"):
            midnight_arrivals = queries.find_midnight_arrivals(station_code)
            midnight_arrivals = pd.DataFrame(midnight_arrivals)
            midnight_arrivals.columns = ["Train Number", "Train Name"]
            st.write("Trains arriving at midnight:", midnight_arrivals)

    elif question == "Halt Times":
        st.sidebar.write("### Question 2")
        longest_halt_times, shortest_halt_times, headers = queries.display_halt_times()

        longest_halt_times[4] = [str(halt_time) for halt_time in longest_halt_times[4]]
        longest_halt_times = pd.DataFrame(longest_halt_times)
        longest_halt_times.columns = [header[0] for header in headers]

        shortest_halt_times[4] = [str(halt_time) for halt_time in shortest_halt_times[4]]
        shortest_halt_times = pd.DataFrame(shortest_halt_times)
        shortest_halt_times.columns = [header[0] for header in headers]

        st.write("Trains with longest halt times:", longest_halt_times)
        st.write("Trains with shortest halt times:", shortest_halt_times)

    elif question == "Find Trains between Stations":
        st.sidebar.write("### Question 3")
        start_station = st.text_input("Enter Start Station Code", "JUC")
        end_station = st.text_input("Enter End Station Code", "ASR")
        if st.button("Find Trains"):
            trains_between_stations = queries.find_trains_between_stations(start_station, end_station)
            trains_between_stations = pd.DataFrame(trains_between_stations)
            trains_between_stations.columns = ["Train Number", "Train Name"]
            st.write("Trains between stations:", trains_between_stations)

    elif question == "Query Sandbox":
        st.sidebar.write("### Query Sandbox")
        query = st.text_area("Enter Query", "SELECT * FROM Trains")

        if st.button("Execute Query"):
            result, headers = queries.execute_query(query)

            # add the data to the dataframe
            df = pd.DataFrame(result)

            # Define the headers of the dataframe
            df.columns = [header[0] for header in headers]

            st.write("Result as DataFrame:", df)


if __name__ == "__main__":
    main()
