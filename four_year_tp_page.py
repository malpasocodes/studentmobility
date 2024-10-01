import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data, create_composite_mobility_score, get_top_performers
from create_plots import plot_top_performers



def show():

    st.title("4-Year Colleges (Top Performers)")
    st.write("The college enrolls at least 10% from the bottom quintile (Q1) and has a minimum of 500 students.")
   
    
    # load data
    df = load_data() 

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)
    
    ############################ Q1 to Q5 Mobility Rate ################################

    # add title for figure
    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 1: Top 50 Performers - Q1 to Q5 Mobility Rate</h2>", unsafe_allow_html=True)

    
    # get top performers
    top_performers_q1q5 = get_top_performers(df, iclevel =1, n=50, count=500, par_q1_min=0.1, criterion='kq5_cond_parq1')

    # plot top performers
    fig1 = plot_top_performers(top_performers_q1q5, "[Q1 to Q5]")
    st.plotly_chart(fig1)

    # add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    ############################ Composite Mobility Score ################################


    # add title for figure
    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 2: Top 50 Performers - Composite Mobility Score</h2>", unsafe_allow_html=True)


    # plot top performers based on composite mobility score
    top_performers_cms = get_top_performers(df, iclevel=1, n=50, count=500, par_q1_min=0.1, criterion='composite_mobility_score')
    fig2 = plot_top_performers(top_performers_cms, 'Composite Mobility Score')

    st.plotly_chart(fig2)


    # Add a dashed line separator   
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    ############################ Table for Q1 to Q5 Mobility Rate ################################


    # add title for table   
    st.markdown("<h2 style='font-size:24px;color:blue'>Top 50 Performers - Q1 to Q5 Mobility Rate</h2>", unsafe_allow_html=True)

    # display top performers based on Q1 to Q5 mobility rate
    columns = ['Name', 'State', '[Q1 to Q5]', '[Q1 Pctg]', 'Tier Group']
    top_performers_q1q5 = top_performers_q1q5[columns]
    top_performers_q1q5 = top_performers_q1q5.round(2)

    st.write(top_performers_q1q5)


    ############################ Top Performers Table (Composite Mobility Score) ################


     # display top performers
    st.markdown("<h2 style='font-size:24px;color:blue'>Table 2: Top 50 Performers - Composite Mobility Score</h2>", unsafe_allow_html=True)
    
    columns = ['Name', 'State', 'Composite Mobility Score', '[Q1 Pctg]', 'Tier Group']
    top_performers_cms = top_performers_cms[columns]
    top_performers_cms = top_performers_cms.round(2)

    st.write(top_performers_cms)
    


    