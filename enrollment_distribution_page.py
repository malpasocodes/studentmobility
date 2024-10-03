import pandas as pd
import plotly.express as px
import streamlit as st

from data_loader import load_data, calc_distribution
from create_plots import plot_distribution


def show():

    st.title("Enrollment Distributions")

    
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    st.write("This papge presents enrollment distributions by income quintiles for different types of colleges. ")


    ############################ IvyPlus ################################

    df = load_data()
    ivyplus = df[df['tier'] == 1]

    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 1: IvyPlus Distribution</h2>", unsafe_allow_html=True)

    # plot plot_distribution
    fig1 = plot_distribution(ivyplus)
    st.plotly_chart(fig1)

    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    ############################ Other Elite ################################


    otherelite = df[df['tier'] == 2]

    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 2: Other Elite</h2>", unsafe_allow_html=True)

    # plot plot_distribution
    fig2 = plot_distribution(otherelite)
    st.plotly_chart(fig2)

    ############################ Highly Selective Public ################################

    highly_selective_public = df[df['tier'] == 3]

    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 3: Highly Selective Public</h2>", unsafe_allow_html=True)

    # plot plot_distribution
    fig3 = plot_distribution(highly_selective_public)
    st.plotly_chart(fig3)

    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    ############################ Highly Selective Private ################################


    highly_selective_private = df[df['tier'] == 4]

    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 4: Highly Selective Private</h2>", unsafe_allow_html=True)

    # plot plot_distribution
    fig3 = plot_distribution(highly_selective_private)
    st.plotly_chart(fig3)

    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    ############################ Four-year for-profit ################################

    four_year_for_profit = df[df['tier'] == 10]

    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 5: Four-year for-profit</h2>", unsafe_allow_html=True)

    # plot plot_distribution
    fig4 = plot_distribution(four_year_for_profit)
    st.plotly_chart(fig4)