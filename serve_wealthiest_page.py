import streamlit as st
import pandas as pd
import plotly.express as px

from data_loader import load_data, calc_distribution
from create_plots import plot_scatter, plot_distribution



def show():
    st.title("Colleges Serving Wealthiest Students")
    
    # load data
    df = load_data()

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    # sort dataframe by fraction of parents in the top 1 percentile
    top1pct= df.sort_values(by='par_top1pc', ascending=False).head(50)

    # display top 50 colleges serving the wealthiest students
    st.write("Top 50 colleges serving the wealthiest students")

    # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    df_top1pct = df.sort_values(by='par_top1pc', ascending=False).head(50)

    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 1:  Colleges with Highest Enrollment from Top 1% Income</h2>", unsafe_allow_html=True)
    fig1 = plot_scatter(df_top1pct, x_axis='par_top1pc', y_axis='par_median')
    st.plotly_chart(fig1)

    df = load_data()

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    df_top20pct = df.sort_values(by='par_q5', ascending=False).head(50)

    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 2:  Colleges with Highest Enrollment from Top 20% Income</h2>", unsafe_allow_html=True)
    fig2 = plot_scatter(df_top20pct, x_axis='par_q5', y_axis='par_median')
    st.plotly_chart(fig2)

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)


    st.markdown("<h2 style='font-size:24px;color:blue'>Figure 3:  Enrollment from Bottom 20% vs Top 20% Income</h2>", unsafe_allow_html=True)


    fig3 = plot_scatter(df_top20pct, x_axis='par_q5', y_axis='par_q1')
    st.plotly_chart(fig3)

     # Add a dashed line separator
    st.markdown("<hr style='border: 1px dashed black;'>", unsafe_allow_html=True)

    st.markdown("<h2 style='font-size:24px;color:blue'>Table 1: Colleges with Highest Enrollment from Top 1% Income</h2>", unsafe_allow_html=True)





    columns = ['name', 'state','par_top1pc', 'par_median']
    top1pct = top1pct[columns]

    top1pct.columns = ['Name', 'State', 'Fraction in Top 1%', 'Median Parent Income']
    top1pct = top1pct.round(2)
    top1pct.reset_index(drop=True, inplace=True)
    top1pct.index += 1

    st.write(top1pct)


"""




    # plot distribution of parent income for highly selective public colleges
    fig4 = plot_distribution(5)
    st.plotly_chart(fig4)


    """
     