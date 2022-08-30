import os
from dotenv import load_dotenv
from sodapy import Socrata
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#Client code/import environment variables into code
load_dotenv()
TOKEN = os.getenv('TOKEN_ENV')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

client = Socrata("data.melbourne.vic.gov.au",
                  TOKEN,
                  username=USER,
                  password=PASSWORD)

#import parking sensor dataset
parking = client.get("7pgd-bdf2", limit=2000)
#import records into a pd dataframe
parking_df = pd.DataFrame.from_records(parking)

pedestrian_data = client.get("b2ak-trbp", limit=2000)
pedestrian_df =pd.DataFrame.from_records(pedestrian_data)


st.title('Displaying parking sensor data')
parking_df

st.title('Show time spent at each parking sensor')
parking_df['durationminutes'] = parking_df['durationminutes'].astype('int')
present_vehicles = parking_df.where(parking_df.vehiclepresent ==True).groupby('deviceid').count()
#send output to streamlit
st.bar_chart(present_vehicles, y='durationminutes')


#1 day period of sensor data 34
st.title('1 day period of sensor data 34')
pedestrian_df['mdate'] = pedestrian_df['mdate'].astype('int')
pedestrian_df['hourly_counts'] = pedestrian_df['hourly_counts'].astype('int')
sensor_34 = pedestrian_df.loc[(pedestrian_df['sensor_id'] == '34') & (pedestrian_df['mdate'] < 2)]
#send output to streamlit
st.line_chart(sensor_34, x='date_time', y='hourly_counts')




