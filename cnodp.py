import streamlit as st

# Create a sidebar for navigation
menu = st.sidebar.radio("Menu", ["The Challenge", "Insights", "Benefits"])

# Define content based on menu selection

if menu == "The Challenge":
    st.header("The Challenge")
    # Add content related to the challenge here

elif menu == "Insights":
    st.header("Insights")
    # Add content related to insights here

elif menu == "Benefits":
    st.header("Benefits")
    # Add content related to benefits here

else:
    st.error("Invalid menu selection")
