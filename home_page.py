import streamlit as st

def show():

    st.markdown("<h1 style='font-size:32px;color:brown'>Student Mobility Dashboard</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        Welcome to the student mobility dashboard. This dashboard allows you to explore data on economic mobility at different types of colleges in the United States.
        The dashboard is work in progress. Please see the **About** page for more information.

        Our aim is to stimulate discussion, particulary on the following questions:

        1. **Which colleges are top performers for social mobility?**
        2. **Are elite colleges truly meritocratic or do they mostly serve the wealthy?**
    """) 
    
               
    st.write(
        "The data used in this dashboard is sourced mostly from the "
        "[Opportunity Insights Project](https://opportunityinsights.org), led by the economist Raj Chetty. "
        "Please note that any errors or interpretations of the data on this site should not "
        "be attributed to the Opportunity Insights project."
    )
    

    st.markdown("<h2 style='font-size:24px;color:brown'>Navigation</h2>", unsafe_allow_html=True)

    st.write(
        "Use the navigation bar on the left to explore different sections of the dashboard. "
        "The sections include:"
    )

    st.markdown("""
        - **Methodology**: Explanation of the methodology used in this dashboard. Coming soon.
        - **2-Year Colleges (Top Performers):** Top 2-year colleges based on different mobility rates.
        - **4-Year Colleges (Top Performers)**: Top 4-year colleges based on different mobility rates.
        - **Colleges Serving Wealthiest Students**: Colleges with the highest enrollment from upper income brackets.
        - **Enrollment Distributions**: Distribution of students across different income brackets for different types of colleges.
        - **Statistical Analysis**: More arcane statistics for the cognoscenti. Coming soon.
    """)

    st.markdown("<h2 style='font-size:24px;color:brown'>Overview</h2>", unsafe_allow_html=True)

    st.write("1. **Economic Mobility**: We can define economic mobility as the ability of a person, familiy, or group to improve their economic status over time. "
                "In this dashboard, we focus on *generational economic mobility* of students. "
                "We are interested in understanding the probability that a student who attends a particular college can move up the income ladder compared to their parents. "
                "Think of the income ladder as a series of rungs, with the bottom rung representing the lowest income bracket and the top rung representing the highest income bracket. "
                "The ladder begins at Q1. The rungs of the ladder are Q2, Q3, Q4, and Q5.")
    
    # insert image 


    col1, col2, col3 = st.columns([1,3,1])

    with col1:
        st.write("")

    with col2:
        st.image("images/income_ladder.png", use_column_width=False, caption="Income Ladder", width=350)
    with col3:
        st.write("")
    
    st.write("2. **Income Quintiles**: Income quintiles will be a primary unit of analysis (though not exclusively) in this dashboard. What are Q1, Q2, Q3, Q4, and Q5? Income quintiles," 
              "as used by economists, divide a population into five equal parts based on household income. "
              "Each quintile represents 20% of the population, ranked from the lowest to the highest income levels. Here’s how they are typically defined:")

    st.markdown("""
            
                - **Q1**: The bottom 20% of the population.
                - **Q2**: The second 20% of the population.
                - **Q3**: The middle 20% of the population.
                - **Q4**: The fourth 20% of the population.
                - **Q5**: The top 20% of the population.""")
    
    st.write("3. **Student Mobility**: What is meant by student mobility? Student mobility refers to the ability of a student to move up the income ladder compared to their parents. "
             "If a student's parents belong to a certain income quintile (e.g. Q1), what is the probability they can move up to a higher income quintile (e.g. Q2, Q3, Q4, Q5) "
             "when they attend a particular college.")
    
    st.write("4. **Dataset**: The dataset used in this dashboard looks at cohorts of students who entered a specific college in the years 1980, 1981, and 1982. Their starting income quintile is based on their parents' income. "
                "The dataset tracks these students until 2014 to see which income quintile they end up in. The dataset also includes information on the college they attended. "
                "**Q1 to Q2** means the probability that a student from the bottom 20% of the income distribution (Q1) can move up to the second quintile (Q2) after having attended a particular college. "
                "**Q1 to Q5** means the probability that a studentfrom the bottom 20% of the income distribution (Q1) can move up to the top quintile (Q5) after having attended a particular college. "
                "We also calculate a **composite mobility score** for each college based on the probability of moving each of the income ladder rungs from **Q1 to Q5**.")