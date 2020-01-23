import streamlit as st
import pandas as pd
import plotly.graph_objects as go

class ViewThings:
    def __init__(self,filename, name):
        st.title( name +"'s Stock Data")
        st.subheader('Your Portfolio Data')
        df = pd.read_excel(filename)
        #buysell plot
        #uses the FOM and creates a pie chart.
        buy = 0
        sell = 0
        vals = df['Golden Cross']
        vals = vals.tolist()
        for i in vals:
            if i == True:
                buy = buy + 1
            else:
                sell = sell + 1
        labels = ['buy','sell']
        values = [buy,sell]
        # Use `hole` to create a donut-like pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        st.subheader('Overall Recommended Buy And Sell of This Portfolio')
        st.write(fig)
        # fig.show()
        # st.subheader(buy)
        # st.subheader(sell)
        st.subheader('''Your Portfolio's key stats''')
        st.write(df)
view = ViewThings('stonksresearch.xlsx', 'Russ')
