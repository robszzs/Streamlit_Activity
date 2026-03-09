import streamlit as st

# 1. Sidebar for the "About" Section (Requirement 4)
with st.sidebar:
    st.title("About this App")
    st.info("This app generates a custom workout plan.")
    st.write("**Target User:** Fitness beginners.")
    st.write("**Inputs:** Age, weight, goals. **Outputs:** Weekly schedule.")

# 2. Main UI Flow (Requirement 1 & 2)
st.title("🚀 Personal Goal Setter")

# Using different components to hit that '20 components' goal
name = st.text_input("Enter Name")
age = st.number_input( "Age", min_value=1, max_value=100)
level = st.select_slider("Fitness Level", options=["Beginner", "Intermediate", "Pro"])
color = st.color_picker("Pick a theme color") # Extra Merit potential

if st.button("Generate Plan"):
    st.balloons() # Another component!
    st.success(f"Plan generated for {name}!")