import pandas as pd
import numpy as np
import streamlit as st


def load_data():
    df = pd.read_csv('data/mrc_table2.csv')

    # Define conditions for tier groups
    tier_group_conditions = [
        (df['iclevel'] == 1) & (df['type'] == 1),
        (df['iclevel'] == 1) & (df['type'] == 2),
        (df['iclevel'] == 1) & (df['type'] == 3),
        (df['iclevel'] == 2) & (df['type'] == 1),
        (df['iclevel'] == 2) & (df['type'] == 2),
        (df['iclevel'] == 2) & (df['type'] == 3),
    ]

    # Define the corresponding tier group names
    tg_choices = ['4-year public', '4-year private non-profit', '4-year private profit', '2-year public', '2-year private non-profit', '2-year private profit']

    # Create the tier_group column
    df['tier_group'] = np.select(tier_group_conditions, tg_choices, default='Other')

    elite_group_conditions = [
        (df['tier'] == 1),
        (df['tier'] == 3),
    ]

    # define the corresponding elite group names
    eg_choices = ['Ivy Plus', 'Highly Selective Public']

    # create the elite_group column
    df['elite_group'] = np.select(elite_group_conditions, eg_choices, default='Other')

    df = create_composite_mobility_score(df)


    return df

def create_composite_mobility_score(df):

    # compound mobility score is based on mobility transitions
    # define weights for each transition

    weights = {
        'kq2_cond_parq1': 2, # 1st quintile to 2nd quintile
        'kq3_cond_parq1': 2, # 1st quintile to 3rd quintile
        'kq4_cond_parq1': 2, # 1st quintile to 4th quintile
        'kq5_cond_parq1': 5  #  1st quintile to 5th quintile
    }

    # max score 
    max_score = 5
    
    # create a new column for compound mobility score by multiplying each transition probability by its weight

    df['composite_mobility_score'] = (df['kq2_cond_parq1'] * weights['kq2_cond_parq1'] + 
                                        df['kq3_cond_parq1'] * weights['kq3_cond_parq1'] + 
                                        df['kq4_cond_parq1'] * weights['kq4_cond_parq1'] + 
                                        df['kq5_cond_parq1'] * weights['kq5_cond_parq1'])
    
    # normalize the compound mobility score
    df['composite_mobility_score'] = df['composite_mobility_score'] / max_score   

    return df

def get_top_performers(df, iclevel =1, n=50, count=500, par_q1_min=0.1, criterion='composite_mobility_score'):

    # filter out rows where par_q1 is less than par_q1_min
    df = df[df['par_q1'] >= par_q1_min]

    # filter out rows where iclevel is not equal to iclevel
    df = df[df['iclevel'] == iclevel]

    # filter out rows where the number of students is less than count
    df = df[df['count'] >= count]

    # sort the dataframe by compound mobility score in descending order
    df = df.sort_values(by=criterion, ascending=False)

    # get the top n performers
    df = df.head(n)

    columns = ['name', 'state', 'tier_group','composite_mobility_score', 'kq2_cond_parq1', 'kq5_cond_parq1','par_q1', 'count']
    df = df[columns]

    df.columns = ['Name', 'State', 'Tier Group','Composite Mobility Score', '[Q1 to Q2]', '[Q1 to Q5]','[Q1 Pctg]', 'Count']

    return df


def calc_distribution(df):


    columns = ['name', 'state', 'tier_group', 'par_q1', 'par_q2', 'par_q3', 'par_q4', 'par_q5', 'tier']
    df = df[columns]
    

    # Calculate the average of the parental income distribution columns
    columns_to_average = ['par_q1', 'par_q2', 'par_q3', 'par_q4', 'par_q5']
    average_values = df[columns_to_average].mean()

    # create a new dataframe for plotting
    df = pd.DataFrame({'Parent Income Quintile': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'],
                       'Percentage': average_values})
    
    return df



    