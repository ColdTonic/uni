import os
from sodapy import Socrata
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#Client code/import environment variables into code

client = Socrata("data.melbourne.vic.gov.au",
                  st.secrets["TOKEN_ENV"],
                  username=st.secrets["USER"],
                  password=st.secrets["PASSWORD"])

#import parking sensor dataset
parking = client.get("7pgd-bdf2", limit=2000)
#import records into a pd dataframe
parking_df = pd.DataFrame.from_records(parking)

st.title('Displaying parking sensor data')
parking_df

st.title('Show time spent at each parking sensor')
parking_df['durationminutes'] = parking_df['durationminutes'].astype('int')
present_vehicles = parking_df.where(parking_df.vehiclepresent ==True).groupby('deviceid').count()
#send output to streamlit
st.bar_chart(present_vehicles, y='durationminutes')
