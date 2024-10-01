import streamlit as st
import home_page
import definitions
import two_year_tp_page
import four_year_tp_page
import serve_wealthiest_page
import enrollment_distribution_page


# create sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Go to', ['Home', 'Definitions', '2-Year Colleges (Top Performers)', '4-Year Colleges (Top Performers)', "Colleges Serving Wealthiest Students", "Enrollment Distibutions"])

# display the selected page

if page == 'Home':
    home_page.show()
elif page == 'Definitions':
    definitions.show()
elif page == '2-Year Colleges (Top Performers)':
    two_year_tp_page.show()
elif page == '4-Year Colleges (Top Performers)':
    four_year_tp_page.show()
elif page == "Colleges Serving Wealthiest Students":
    serve_wealthiest_page.show()
elif page == "Enrollment Distibutions": 
    enrollment_distribution_page.show()
else:    
    home_page.show()

    