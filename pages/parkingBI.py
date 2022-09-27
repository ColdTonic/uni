import streamlit as st


client = Socrata("data.melbourne.vic.gov.au",
                  st.secrets["TOKEN_ENV"],
                  username=st.secrets["USER"],
                  password=st.secrets["PASSWORD"])

st.header('Welcome to the Parking Data Streamlit Web App')
st.subheader('This section is displays general information regarding parking data across melbourne run via PowerBI. See the other pages for more information.')
st.markdown('https://app.powerbi.com/links/GQQYSYJxUj?ctid=df7f7579-3e9c-4a7e-b844-420280f53859&pbi_source=linkShare', unsafe_allow_html=True)