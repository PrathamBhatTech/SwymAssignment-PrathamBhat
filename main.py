import streamlit as st
import queries
import pandas as pd


# Streamlit app
def main():
    st.title("Indian Railways Timetable")

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

The source code for this app can be found [here]().
To see the questions and the queries, click on the arrow on the left.
    '''

    st.write(message)

    # Sidebar options
    question = st.sidebar.selectbox("Select a Question",
                                    [
                                        "",
                                        "Find Trains Arriving at Midnight",
                                        "Find Trains between Stations",
                                        "Query Sandbox"
                                    ]
                                    )

    if question == "Find Trains Arriving at Midnight":
        st.sidebar.write("### Question 1")
        station_code = st.text_input("Enter Station Code", "SWV")
        if st.button("Find Trains"):
            midnight_arrivals = queries.find_midnight_arrivals(station_code)
            st.write("Trains arriving at midnight:", midnight_arrivals)

    elif question == "Find Trains between Stations":
        st.sidebar.write("### Question 3")
        start_station = st.text_input("Enter Start Station Code", "JUC")
        end_station = st.text_input("Enter End Station Code", "ASR")
        if st.button("Find Trains"):
            trains_between_stations = queries.find_trains_between_stations(start_station, end_station)
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

            st.write("Result:", result)


if __name__ == "__main__":
    main()
