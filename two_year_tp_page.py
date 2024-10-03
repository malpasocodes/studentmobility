import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data, create_composite_mobility_score, get_top_performers
from create_plots import plot_top_performers



def show():

    st.title("2-Year Colleges (Top Performers)")
    st.write("To qualify as top performer, the college must enroll at least 10% of its students" 
             "from the bottom quintile (Q1) and have a minimum of 1000 students in the cohort group."
             "For 2-year colleges, we present mobility rates for **Q1 to Q2**, **Q1 to Q5**, and a composite mobility score.")
    
    # load data
    df = load_data()
    
    # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)
    
    
    ############################ Q1 to Q2 Mobility Rate ################################
    # get top performers for Q1 to Q2 mobility rate
    top_performers_q1q2 = get_top_performers(df, iclevel=2, n=50, count=500, par_q1_min=0.1, criterion='kq2_cond_parq1')
    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 1: Top 50 Performers - Q1 to Q2 Mobility Rate</h2>", unsafe_allow_html=True)


    # plot top performers
    fig1 = plot_top_performers(top_performers_q1q2, '[Q1 to Q2]')
    st.plotly_chart(fig1)

    # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    ############################ Q1 to Q5 Mobility Rate ################################

    # get top performers for Q1 to Q5 mobility rate
    top_performers_q1q5 = get_top_performers(df, iclevel=2, n=50, count=500, par_q1_min=0.1, criterion='kq5_cond_parq1')
    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 2: Top 50 Performers - Q1 to Q5 Mobility Rate</h2>", unsafe_allow_html=True)



    # plot top performers
    fig2 = plot_top_performers(top_performers_q1q5, '[Q1 to Q5]')
    st.plotly_chart(fig2)

    # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)



    ############################ Composite Mobility Score ################################
     # get top performers
    top_performers_cms = get_top_performers(df, iclevel= 2, n=50, count=500, par_q1_min=0.1, criterion='composite_mobility_score')
    st.markdown("<h2 style='font-size:24px;color:brown'>Figure 3: Top 50 Performers - Composite Mobility Score</h2>", unsafe_allow_html=True)
    fig3 = plot_top_performers(top_performers_cms, 'Composite Mobility Score')
    st.plotly_chart(fig3)

    # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    ############################ Top Performers Table (Q1 to Q2) ################################
    # display top performers
    st.markdown("<h2 style='font-size:24px;color:brown'>Table 1: Top 50 Performers - Q1 to Q2 Mobility Rate</h2>", unsafe_allow_html=True)
    
    columns = ['Name', 'State', '[Q1 to Q2]', '[Q1 Pctg]', 'Tier Group']
    top_performers_q1q2 = top_performers_q1q2[columns]
    top_performers_q1q2 = top_performers_q1q2.round(2)
    top_performers_q1q2.reset_index(drop=True, inplace=True)
    top_performers_q1q2.index += 1

    st.write(top_performers_q1q2)
    # Add a dashed line separator

    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    ############################ Top Performers Table (Q1 to Q5) ################################

    # display top performers
    st.markdown("<h2 style='font-size:24px;color:brown'>Table 2: Top 50 Performers - Q1 to Q5 Mobility Rate</h2>", unsafe_allow_html=True)

    columns = ['Name', 'State', '[Q1 to Q5]', '[Q1 Pctg]', 'Tier Group']
    top_performers_q1q5 = top_performers_q1q5[columns]
    top_performers_q1q5 = top_performers_q1q5.round(2)
    top_performers_q1q5.reset_index(drop=True, inplace=True)
    top_performers_q1q5.index += 1


    st.write(top_performers_q1q5)


    ############################ Top Performers Table (Composite Mobility Score) ################


     # display top performers
    st.markdown("<h2 style='font-size:24px;color:brown'>Table 3: Top 50 Performers - Composite Mobility Score</h2>", unsafe_allow_html=True)
    
    columns = ['Name', 'State', 'Composite Mobility Score', '[Q1 Pctg]', 'Tier Group']
    top_performers_cms = top_performers_cms[columns]
    top_performers_cms = top_performers_cms.round(2)
    top_performers_cms.reset_index(drop=True, inplace=True)
    top_performers_cms.index += 1

    st.write(top_performers_cms)
    
   