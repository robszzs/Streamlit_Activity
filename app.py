import streamlit as st

# 1. Sidebar for branding
with st.sidebar:
    st.title("🎮 Command Center")
    st.info("Identify your gaming persona and get a custom gear recommendation.")
    st.write("**Developed by:** Robz")

# 2. Main UI
st.title("🕹️ Gamer Persona Generator")
st.markdown("---")

# Inputs
name = st.text_input("Enter your Gamertag")
genre = st.selectbox("What's your primary genre?", ["FPS (Valorant/CS)", "RPG (Elden Ring/Skyrim)", "MOBA (LoL/Dota 2)", "Creative (Minecraft/Sims)"])
budget = st.select_slider("Select your Budget Level", options=["Budget", "Mid-Range", "High-End", "Overkill"])
color = st.color_picker("Pick your RGB Theme Color", "#00FFAA")

# 3. Logic for recommendations
if st.button("Generate My Setup"):
    st.balloons()
    
    st.header(f"Results for {name}")
    
    # Simple logic based on genre
    if "FPS" in genre:
        persona = "The Sharpshooter"
        gear = "High-polling rate mouse & 240Hz Monitor"
    elif "RPG" in genre:
        persona = "The Loreseeker"
        gear = "Ultrawide 4K Monitor & Mechanical Keyboard"
    elif "MOBA" in genre:
        persona = "The Tactician"
        gear = "Multi-button Macro Mouse & Dual Monitors"
    else:
        persona = "The Architect"
        gear = "Color-accurate Display & Ergonomic Chair"

    # Display results in a nice layout
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Your Persona")
        st.info(f"**{persona}**")
    
    with col2:
        st.subheader("Recommended Upgrade")
        st.warning(f"**{gear}**")

    st.write(f"Your setup theme color code: `{color}`")
    st.success("Configuration Complete! Ready to deploy.")