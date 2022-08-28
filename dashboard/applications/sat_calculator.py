from numpy.core.records import array
import streamlit as st
from joblib import load
import numpy as np
import sys


def app():

    # Load Saved Results Data
    model = load(filename='models/satisfaction_model.joblib')

    st.title("Satisfaction Calculator")

    st.header("To calculate a user's satisfaction score, enter values below.")

    session_count = st.number_input('Enter sessions', key='a')
    total_duration = st.number_input('Enter total time', key='b')
    total_data = st.number_input('Enter total data', key='c')
    total_retransmission = st.number_input('Enter tcp retransmission', key='d')
    Round_trip = st.number_input('Enter average RTT', key='e')
    total_throughput = st.number_input('Enter average throughput', key='f')

    if st.button('Predict satisfaction'):
        array = [session_count, total_duration, total_data,
                 total_retransmission, Round_trip, total_throughput]
        val = model.predict([array])
        satisfaction = [i[0] for i in val][0]
        st.write(
            "Predicted Satisfaction score for this user is: {:.3f}".format(satisfaction))
