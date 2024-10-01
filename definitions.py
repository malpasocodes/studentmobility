import streamlit as st


def show():


    st.header("Definitions")
    st.write("1. **Economic Mobility**: We can define economic mobility as the ability of a person, familiy, or group to improve their economic status over time."
                " In this dashboard, we focus on generational economic mobility of students who attend different colleges. "
                "We are interested in understanding the probability that a student who attends a particular college can move up the income ladder compared to their parents. ")
                

    st.write("2. **Fading American Dream**: The term *'Fading American Dream'* refers to the idea that the economic mobility of students in the United States has been declining over time."
             " According to the Opportunity Insights Project, *'The defining feature of the American Dream is upward mobility – "
             "the aspiration that all children have a chance at economic success, no matter their background. "
             "However, our research shows that children's chances of earning more than their parents have been declining. "
             "90% of children born in 1940 grew up to earn more than their parents. Today, only half of all children earn more than their parents did.'*")
    

    
    st.write("3. **Restoring the American Dream**: The term *'Restoring the American Dream'* refers to the idea that the economic mobility of students in the United States can be improved over time. "
             "With this dashboard, we aim to provide insights into the economic mobility of students who attend different colleges.")
    
    st.write("4. **Income Quintiles and Generational Mobility**: Our basic unit of analysis will be economic quintiles. Our focus is generational mobility. Think of placing the population in five income buckets. If a student's parents belong to a certain income quintile (e.g. Q1),"
            "what is the probability they can move up to a higher income quintile (e.g. Q2, Q3, Q4, Q5) when they attend a particular college."
            "The student cohort (years 1980, 1981, 1982) is divided into income quintiles based on the income of their parents. Which income quintile does the student end up in 2014 after attending a particular college." 
            "Q1 to Q2 means the probability that a student who comes from the bottom 20% of the income distribution (Q1) can move up to the second quintile (Q2) after attending a particular college."
            "Q1 to Q5 means the probability that a student who comes from the bottom 20% of the income distribution (Q1) can move up to the top quintile (Q5) after attending a particular college.")
    