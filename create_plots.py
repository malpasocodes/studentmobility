import streamlit as st
import pandas as pd
import plotly.express as px

from data_loader import calc_distribution




tier_group_colors = {
    '4-year public': 'blue',
    '4-year private for-profit': 'red',
    '4-year private non-profit': 'green',
    '2-year public': 'green',
    '2-year private for-profit': 'red',
    '2-year private non-profit': 'green',
    'Other': 'gray'
}

elite_group_colors = {
    'Ivy Plus': 'green',
    'Highly Selective Public': 'purple',
}

def plot_top_performers(top_performers, criterion):

    fig = px.scatter(top_performers, x='[Q1 Pctg]', y=criterion, color='Tier Group', size='Count',
                     color_discrete_map=tier_group_colors, hover_name='Name', hover_data=['[Q1 Pctg]', 'State', 'Count'],
                     labels={'[Q1 Pctg]': 'Percent Enrolled from Bottom Quintile (Q1)', criterion: criterion})
    
    # Update x-axis to display percentages
    fig.update_xaxes(tickformat=".0%")
    return fig


def plot_mobility_score_distribution(df, criterion):

    fig = px.histogram(df, x=criterion, color='Tier Group', marginal='box', color_discrete_map=tier_group_colors,
                       labels={criterion: criterion})
    return fig


def plot_scatter(df, x_axis, y_axis):


    fig = px.scatter(df, x=x_axis, y=y_axis, size='count', color='tier_group', color_discrete_map=tier_group_colors,
                     hover_name='Name', hover_data=[x_axis, y_axis, 'State', 'count'],)
    return fig

def plot_distribution(tier):

    average_df = calc_distribution(tier)

    fig = px.bar(
        average_df, 
        x='Parent Income Quintile', 
        y='Percentage',
        title='Average Distribution of Parental Income Quintiles',
        labels={'Average': 'Average Proportion', 'Parental Income Quintile': 'Income Quintile'},
        )
    
     # Add text annotations
    fig.update_traces(texttemplate='%{y:.2f}', textposition='outside')
    return fig


def plot_3d_scatter(df, x_axis, y_axis, z_axis):

    fig = px.scatter_3d(df, x=x_axis, y=y_axis, z=z_axis, color='tier_group', color_discrete_map=tier_group_colors,
                        hover_name='name', hover_data=[x_axis, y_axis, z_axis, 'state', 'count'])
    
    fig.update_traces(marker=dict(size=2))
    return fig


