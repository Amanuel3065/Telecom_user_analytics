from turtle import pd
import streamlit as st
import pandas as pd
import os, sys

def app():
    st.title("User Satisfaction")
    
    df_satisfaction = pd.read_csv('data/top10_satisfied_customers.csv')
    df_score = pd.read_csv('data/score_table.csv')

    st.header("Top 10 Satisfied Customers")
    st.dataframe(df_satisfaction)
    st.bar_chart(df_satisfaction['satisfaction_score'])

    st.subheader("Satisfaction Score Table")
    st.dataframe(df_score)
    st.bar_chart(df_score['satisfaction_score'])

    st.header("User Clustering based on both scores")
    st.image('data/satisfaction.jpg')
    st.markdown(
        'By raising the experience score of a user, which means improving the round trip time, average throughput and TCP of handsets, we can improve user satisfaction.')
