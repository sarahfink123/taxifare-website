import streamlit as st
import pandas as pd
import requests
import datetime
'''
# Taxi fare predictor - New York
'''
'''
Enter your fare information
'''
date = st.date_input(
    "Day",
    datetime.date(2019, 7, 6))

time = st.time_input('Time', datetime.time(8, 45))
date_time = datetime.datetime.combine(date, time).strftime('%Y-%m-%d %H:%M:%S')
pickup_lon = st.number_input('Fill in pickup longitude', min_value=-90.0, max_value=90.0, value=-73.950655)
pickup_lat = st.number_input('Fill in pickup latitude', min_value=-90.0, max_value=90.0, value= 40.783282)
dropoff_lon = st.number_input('Fill in dropoff longitude', min_value=-90.0, max_value=90.0, value= -73.984365)
dropoff_lat = st.number_input('Fill in dropoff latitude', min_value=-90.0, max_value=90.0, value= 40.769802)
passenger_count = st.number_input('Fill in passenger count', min_value=1, max_value=100, value= 1)

url = 'https://taxifare.lewagon.ai/predict'


params = {
    'pickup_datetime': date_time,
    'pickup_longitude':pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude':dropoff_lon,
    'dropoff_latitude':dropoff_lat,
    'passenger_count': passenger_count,
}

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

if st.button('Get Fare Prediction'):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        prediction = response.json()['fare']
        st.write(f'The predicted fare is ${prediction:.2f}')
    else:
        st.write('Error in API call')

st.map(
    pd.DataFrame(
        {
            "lat": [pickup_lat, dropoff_lat],
            "lon": [pickup_lon, dropoff_lon]
        }
    )
)
