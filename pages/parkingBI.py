import streamlit as st

st.header('Welcome to the Parking Data Streamlit Web App')
st.subheader('This section is displays general information regarding parking data across melbourne run via PowerBI. See the other pages for more information.')
st.subheader('hello')
st.components.v1.html("""<iframe title="parkingbi" width=1140, height=600 src="https://app.powerbi.com/reportEmbed?reportId=cb31e468-2410-4b5b-825c-cef573f14a49&autoAuth=true&ctid=df7f7579-3e9c-4a7e-b844-420280f53859" frameborder="0" allowFullScreen="true"></iframe>""", width=1500, height=1000)


#https://app.powerbi.com/links/GQQYSYJxUj?ctid=df7f7579-3e9c-4a7e-b844-420280f53859&pbi_source=linkShare