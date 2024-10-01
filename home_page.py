import streamlit as st

def show():
    st.title("Student Mobility Dashboard")
    st.markdown("""
        Welcome to the student economic mobility dashboard. This dashboard allows you to explore data on economic mobility at different types of colleges. The dashboard is work in progress and we welcome your feedback and suggestions.

        Our aim is to stimulate discussion around the following questions:

        1. **Which colleges are top performers for social mobility?**
        2. **Are elite colleges truly meritocratic or do they mostly serve the wealthy?**
    """) 
    
               
    st.write(
        "The data used in this dashboard is sourced mostly from the "
        "[Opportunity Insights Project](https://opportunityinsights.org). "
        "But please note that any errors or interpretations of the data on this site should not "
        "be attributed to the Opportunity Insights project."
    )
    