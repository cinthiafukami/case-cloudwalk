import streamlit as st
import pandas as pd

# Load the data
aml_data = pd.read_csv('aml_data.csv')

# Dashboard Layout
st.title('AML Alert Effectiveness Dashboard')

# Total Alerts Raised
st.subheader(f'Total Alerts Raised: {aml_data["Alert Status"].sum()}')

# Alerts Resolved
alerts_resolved = aml_data[aml_data['Alert Resolution'] == True]
st.subheader(f'Alerts Resolved: {alerts_resolved.shape[0]}')

# Alerts by Risk Level
alerts_by_risk = aml_data.groupby('Risk Level').size()
st.subheader('Alerts by Risk Level')
st.bar_chart(alerts_by_risk)

# Top Merchants by Alerts
top_merchants = aml_data.groupby('Merchant ID').size().sort_values(ascending=False).head(10)
st.subheader('Top Merchants by Alerts')
st.bar_chart(top_merchants)

# False Positives (Alerts Raised but not Resolved)
false_positives = aml_data[(aml_data['Alert Status'] == True) & (aml_data['Alert Resolution'] == False)]
st.subheader(f'False Positives: {false_positives.shape[0]}')

# Show the Data Table
st.subheader('Data Preview')
st.write(aml_data.head())

