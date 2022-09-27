import os
from sodapy import Socrata
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#Client code/import environment variables into code

client = Socrata("data.melbourne.vic.gov.au",
                  None)

pedestrian_data = client.get("b2ak-trbp", limit=2000)
pedestrian_df =pd.DataFrame.from_records(pedestrian_data)

st.title('Displaying pedestrian count data')
pedestrian_df

#Day period of sensor data
st.title('View trend by day of week')

dow_list = pedestrian_df['day'].unique()
sensor_list = pedestrian_df['sensor_id'].unique()

sensor_val = st.sidebar.selectbox("Select a sensor:", sensor_list)
dow_val = st.sidebar.selectbox("Select a day of the week:", dow_list)

pedestrian_df['hourly_counts'] = pedestrian_df['hourly_counts'].astype('int')
sensor_query = pedestrian_df.loc[(pedestrian_df['sensor_id'] == sensor_val) & (pedestrian_df['day'] == dow_val)]
#send output to streamlit
st.header("Display data for sensor: " + sensor_val)
st.line_chart(sensor_query, x='date_time', y='hourly_counts')


#https://app.powerbi.com/links/rJKFdKXem5?ctid=df7f7579-3e9c-4a7e-b844-420280f53859&pbi_source=linkShare
st.markdown("https://app.powerbi.com/groups/me/reports/a418c44f-ca82-4803-997b-1420c07c28c9/ReportSection?ctid=df7f7579-3e9c-4a7e-b844-420280f53859", unsafe_allow_html=True)
