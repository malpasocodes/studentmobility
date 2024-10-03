import pandas as pd
import numpy as np
import streamlit as st
from data_loader import load_data, calc_statistics

def show():

    df = load_data()
    stats = calc_statistics(df, 1)
    st.write(stats)

    stats = calc_statistics(df, 2)
    st.write(stats)


    stats = calc_statistics(df, 3)
    st.write(stats)

    stats = calc_statistics(df, 4)
    st.write(stats)

    stats = calc_statistics(df, 8)
    st.write(stats)
    

