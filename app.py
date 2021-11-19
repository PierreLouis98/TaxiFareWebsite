import streamlit as st
import requests
from datetime import datetime


st.markdown('''
# TaxiFareModel front
''')


url = 'https://taxifare.lewagon.ai/predict?pickup_datetime=2013-07-06%2017:18:00&pickup_longitude=-73.950655&pickup_latitude=40.783282&dropoff_longitude=-73.984365&dropoff_latitude=40.769802&passenger_count=1'
url2 = 'https://taxifare.lewagon.ai/predict'
url3 = 'https://pl-app2-cont-op4wl2zmrq-ew.a.run.app/predict'

    #date_time = st.text_area('date and time', '''12/09/2021''')
    #pickup_longitude = st.number_input('pickup longitude')
    #pickup_latitude = st.number_input('pickup latitude')
    #dropoff_longitude = st.number_input('dropoff longitude')
    #dropoff_latitude = st.number_input('dropoff latitude')


'''
### Finally, we can display the prediction to the user
'''
passenger_count = st.number_input('passenger_count', min_value=0, max_value=5)

# 2.
params = {
    'pickup_datetime': '2013-07-06 17:18:00',
    'pickup_longitude': -73.950655,
    'pickup_latitude': 40.783282,
    'dropoff_longitude': -73.984365,
    'dropoff_latitude': 40.769802,
    'passenger_count': passenger_count
}

# 3.
response = requests.get(url3, params)
#response = requests.get(url)
pred = response.json()
print(pred)
st.markdown(pred['prediction'])
