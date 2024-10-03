import streamlit as st
import pandas as pd
import plotly.express as px

from data_loader import load_data, calc_distribution
from create_plots import plot_scatter, plot_distribution, plot_3d_scatter



def show():
    st.title("Colleges Serving Wealthiest Students")
    
    # load data
    df = load_data()

    # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    ### Colleges with Highest Enrollment from Top 1% Income ###

    df_top1pct = df.sort_values(by='par_top1pc', ascending=False).head(50)

    df_top1pct = df_top1pct[['name', 'state', 'par_top1pc','par_median', 'count','tier_group']]
    df_top1pct.columns = ['Name', 'State', 'Percentage in Top 1%', 'Median Parent Income', 'count', 'tier_group'] 

    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 1:  Colleges with Highest Enrollment from Top 1% Income</h2>", unsafe_allow_html=True)
    fig1 = plot_scatter(df_top1pct, x_axis='Percentage in Top 1%', y_axis='Median Parent Income')
    st.plotly_chart(fig1)

    ### Colleges with Highest Enrollment from Top 20% Income ###


     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    df_top20pct = df.sort_values(by='par_q5', ascending=False).head(50)
    df_top20pct = df_top20pct[['name', 'state', 'par_q5', 'par_q1','par_median', 'count','tier_group']]
    df_top20pct.columns = ['Name', 'State', 'Percentage in Top 20%', 'Percentage in Bottom 20%','Median Parent Income', 'count', 'tier_group']

    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 2:  Colleges with Highest Enrollment from Top 20% Income</h2>", unsafe_allow_html=True)
    fig2 = plot_scatter(df_top20pct, x_axis='Percentage in Top 20%', y_axis='Median Parent Income')
    st.plotly_chart(fig2)

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 3:  Enrollment from Bottom 20% vs Top 20% Income</h2>", unsafe_allow_html=True)


    fig3 = plot_scatter(df_top20pct, x_axis='Percentage in Top 20%', y_axis='Percentage in Bottom 20%')
    st.plotly_chart(fig3)



    ############################################################################################################

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    st.markdown("<h2 style='font-size:24px;color:blue'>Table 1: Colleges with Highest Enrollment from Top 1% Income</h2>", unsafe_allow_html=True)


    df_top1pct = df_top1pct.round(2)
    df_top1pct.reset_index(drop=True, inplace=True)
    df_top1pct.index += 1

    st.write(df_top1pct)

    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    st.markdown("<h2 style='font-size:24px;color:blue'>Table 2: Colleges with Highest Enrollment from Top 20% Income</h2>", unsafe_allow_html=True)

    df_top20pct = df_top20pct.round(2)
    df_top20pct.reset_index(drop=True, inplace=True)
    df_top20pct.index += 1

    st.write(df_top20pct)



