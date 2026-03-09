import streamlit as st

# --- INITIALIZATION ---
# We use session_state to track which "page" the user is on
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to change pages
def ch_page(page_name):
    st.session_state.page = page_name

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("📚 Library Nav")
    st.divider()
    
    # 4 Sidebar Buttons
    if st.button("🏠 Home", use_container_width=True):
        ch_page("Home")
    
    # RENAME THESE: Replace "Book Title A" with your actual book name
    if st.button("tensura", use_container_width=True):
        ch_page("Book A")
        
    if st.button("hachiman", use_container_width=True):
        ch_page("Book B")
        
    if st.button("👤 About Me", use_container_width=True):
        ch_page("About")

# --- PAGE LOGIC ---

# 1. HOME TAB
if st.session_state.page == "Home":
    st.title("Welcome Jenwille Robias")
    st.write("Select a book from the sidebar or use the quick links below:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Open Book Title A ➡️"):
            ch_page("Book A")
    with col2:
        if st.button("Open Book Title B ➡️"):
            ch_page("Book B")
    
    st.image("https://images.unsplash.com/photo-1507842217343-583bb7270b66?q=80&w=1000", caption="Your Library Archive")

# 2. BOOK TITLE A TAB
elif st.session_state.page == "Book A":
    st.title("That Time I Got Reincarnated as a slime")
    
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        # REPLACE URL with your image path or a local file
        st.image("https://via.placeholder.com/150", caption="Book A Cover")
    with col_txt:
        st.subheader("Description")
        st.write("This is where you describe the content of Book A.")
    
    st.divider()
    st.write("### Resources")
    # 3 Download Buttons
    dl1, dl2, dl3 = st.columns(3)
    dl1.download_button("📥 Full PDF", data="sample", file_name="bookA_full.pdf")
    dl2.download_button("📥 Summary", data="sample", file_name="bookA_summary.pdf")
    dl3.download_button("📥 Diagrams", data="sample", file_name="bookA_diagrams.zip")

# 3. BOOK TITLE B TAB
elif st.session_state.page == "Book B":
    st.title("📗 Book Title B")
    
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.image("https://via.placeholder.com/150", caption="Book B Cover")
    with col_txt:
        st.subheader("Description")
        st.write("Detailed notes for Book B go here.")
        
    st.divider()
    st.write("### Resources")
    # 3 Download Buttons
    dl1, dl2, dl3 = st.columns(3)
    dl1.download_button("📥 Full PDF", data="sample", file_name="bookB_full.pdf")
    dl2.download_button("📥 Summary", data="sample", file_name="bookB_summary.pdf")
    dl3.download_button("📥 Charts", data="sample", file_name="bookB_charts.png")

# 4. ABOUT ME TAB (Requirement Check)
elif st.session_state.page == "About":
    st.title("👤 About the Project")
    st.info("""
    - **Use-Case:** Academic Digital Library for peer resource sharing.
    - **Target User:** Students in the Networking/IT department.
    - **Inputs:** Navigation clicks and download requests.
    - **Outputs:** Displayed book metadata and downloadable PDF assets.
    """)
    st.write("Developed by **Robz**.")