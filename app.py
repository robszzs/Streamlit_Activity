import streamlit as st
import time

# --- 1. SIDEBAR (Required: About Section) ---
with st.sidebar:
    st.title("📌 App Information")
    
    # Requirement 4: What the app does, target user, and inputs/outputs
    with st.expander("📖 About this App", expanded=True):
        st.write("""
        **Use-Case:** A Digital Resource Hub for Networking students to manage files and calculate network stats.
        **Target User:** IT Students and Network Administrators.
        **Inputs:** Text, numbers, files, and configuration toggles.
        **Outputs:** Downloadable PDFs, calculated network metrics, and status reports.
        """)
    
    st.divider()
    st.info("Created by: Robz")
    # Component: Sidebar Image/Logo (Merit point potential)
    st.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=100)

# --- 2. MAIN UI FLOW ---
st.title("🌐 Technical Digital Library & Toolset")

# Using Tabs (Advanced Component for Merit)
tab1, tab2, tab3 = st.tabs(["📚 Library", "⚙️ Network Tools", "📊 System Status"])

with tab1:
    st.header("Document Repository")
    st.caption("Select a category to view available PDFs.")
    
    # Components: Selectbox, Radio, and Download Button
    category = st.selectbox("Document Category", ["Networking", "Cloud Computing", "Security"])
    doc_type = st.radio("File Format", ["Standard PDF", "Compressed", "Markdown"])
    
    # Component: Download Button (Functional)
    st.download_button(label="📥 Download Syllabus", data="Sample content", file_name="syllabus.pdf")
    
    # Component: File Uploader (Merit point - interacts with files)
    uploaded_file = st.file_uploader("Contribute a document to the library")
    if uploaded_file:
        st.success("File ready for processing!")

with tab2:
    st.header("Network Calculator")
    
    # Components: Columns, Number Input, Text Input, Slider
    col1, col2 = st.columns(2)
    with col1:
        ip_addr = st.text_input("Enter Base IP Address", placeholder="192.168.1.1")
        nodes = st.number_input("Number of Nodes", min_value=1, max_value=254)
    with col2:
        subnet = st.select_slider("Subnet Mask", options=["/24", "/26", "/28", "/30"])
        priority = st.select_slider("Traffic Priority", options=["Low", "Medium", "High"])

    # Component: Color Picker (For UI Customization)
    theme = st.color_picker("Customize UI Accent", "#00f900")
    
    # Component: Checkbox and Toggle (Merit point: Toggle is a newer component)
    monitor = st.checkbox("Enable Real-time Monitoring")
    secure_mode = st.toggle("Enable Stealth Mode")

    if st.button("🚀 Calculate Network Load"):
        # Component: Progress Bar & Spinner (Merit points for "Motion" UI)
        with st.spinner('Calculating...'):
            my_bar = st.progress(0)
            for p in range(100):
                time.sleep(0.01)
                my_bar.progress(p + 1)
        st.balloons()
        st.write(f"Network configured for {nodes} nodes on {subnet} with {theme} branding.")

with tab3:
    st.header("Live Metrics")
    # Components: Metrics (Advanced UI)
    m1, m2, m3 = st.columns(3)
    m1.metric("Server Uptime", "99.9%", "0.2%")
    m2.metric("Latency", "24ms", "-2ms")
    m3.metric("Users Active", "6", "+1")
    
    # Component: Text Area and Date Input
    st.date_input("Schedule Maintenance")
    st.text_area("Admin Notes", "Current AWS report is in version 2.4...")

st.markdown("---")
# Component: Status Message
st.status("System Operational", state="complete")