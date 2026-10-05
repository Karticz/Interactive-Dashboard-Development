import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Interactive Executive Dashboard")
st.write("Key insights and performance metrics for decision-making.")


data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 200, 180, 220, 250, 300],
    'Profit': [50, 70, 60, 90, 110, 140]
}
df = pd.DataFrame(data)


st.subheader("Sales Trend (Over Time)")
fig_line = px.line(df, x='Month', y='Sales', markers=True, text='Sales')
st.plotly_chart(fig_line)


st.subheader("Profit Metrics")
fig_bar = px.bar(df, x='Month', y='Profit', color='Profit')
st.plotly_chart(fig_bar)