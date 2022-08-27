import streamlit as st
import pandas as pd
import os, sys


def app():
    
    st.title("User Experiences")
    
    df_avgThr = pd.read_csv('data/top10avgThroughput.csv')
    df_rtt = pd.read_csv('data/top10rtt.csv')
    df_tcp = pd.read_csv('data/top10tcp.csv')
    df_frqThr = pd.read_csv('data/most_freqAvgThr.csv')
    df_frqrtt = pd.read_csv('data/most_freqRTT.csv')
    df_frqtcp = pd.read_csv('data/most_freqTCP.csv')
    
    st.header("Top 10 Users' Experiences")
    st.subheader("Average Throughput")
    st.dataframe(df_avgThr)
    st.bar_chart(df_avgThr['Average throughput'])
    
    st.subheader("Round Trip Time")
    st.dataframe(df_rtt)
    st.bar_chart(df_rtt['Average RTT'])
    
    st.subheader("Transmission Control Protocol")
    st.dataframe(df_tcp)
    st.bar_chart(df_tcp['Average TCP'])
    
    st.header("Most Frequent Users")
    st.subheader('Most Frequent Average Throughput')
    st.dataframe(df_frqThr)
    st.bar_chart(df_frqThr['0'])
    
    st.subheader("Most frequent Round Trip Time")
    st.dataframe(df_frqrtt)
    st.bar_chart(df_frqrtt['0'])
    
    st.subheader("Most frequent Transmission Control Protocols")
    st.dataframe(df_frqtcp)
    st.bar_chart(df_frqtcp['0'])

    st.header("3 clusters of users")
    st.image('data/Kmeans-3 groups of standardized data.JPG')