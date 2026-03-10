import streamlit as st

# --- INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"

def ch_page(page_name):
    st.session_state.page = page_name

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("My Library")
    st.divider()
    
    if st.button("Home", use_container_width=True):
        ch_page("Home")
    
    # RENAME: Put your actual Book Titles here
    if st.button("That time i got reincarnated as a slime", use_container_width=True):
        ch_page("Book A")
        
    if st.button("Oregairu", use_container_width=True):
        ch_page("Book B")
        
    if st.button("About the Project", use_container_width=True):
        ch_page("About")

# --- PAGE LOGIC ---

# 1. HOME TAB
if st.session_state.page == "Home":
    st.title("Library")
    st.markdown("Read some samples below")
    st.write("Quickly navigate to your favorite series below:")
    

    # Navigation buttons with images
    col_nav1, col_nav2 = st.columns(2)
    
    with col_nav1:
        # container keeps the image and button grouped
        with st.container():
            st.image("images/slime_home_page_cover.jpg", use_container_width=True) 
            if st.button("That time i got reincarnated as a slime", use_container_width=True):
                ch_page("Book A")
            
    with col_nav2:
        with st.container():
            st.image("images/oregairu_home_page_cover.jpg", use_container_width=True)
            if st.button("Oregairu", use_container_width=True):
                ch_page("Book B")
    
    st.divider()
    st.image("images/kitty_banner.jpg", caption="more books to come")

# 2. BOOK TITLE A TAB
elif st.session_state.page == "Book A":
    st.title("That time i got reincarnated as a slime")
    
    # Space for Book & Author Info
    st.markdown("#### About the Book")
    st.write("Lonely thirty-seven-year-old Satoru Mikami is stuck in a dead-end job, unhappy with their mundane life, but after dying at the hands of a robber, they awaken to a fresh start in a fantasy realm... as a slime! As Rimuru acclimates to their goopy new existence, their exploits with the other monsters set off a chain of events that will change the world forever!")
    
    st.markdown("#### Author")
    st.write("Fuse")
    
    st.divider()
    
    # Layout with Image and Volume Downloads
    col_img, col_dl = st.columns([1, 2])
    
    with col_img:
        st.image("images/slime_home_page_cover.jpg", caption="That time i got reincarnated as a slime")
        
    with col_dl:
        st.subheader("Download Volumes")
        # 3 Individual Volume Buttons
        st.download_button("Volume 1", data="sample", file_name="BookA_Vol1.pdf", use_container_width=True)
        st.download_button("Volume 2", data="sample", file_name="BookA_Vol2.pdf", use_container_width=True)
        st.download_button("Volume 3", data="sample", file_name="BookA_Vol3.pdf", use_container_width=True)

# 3. BOOK TITLE B TAB
elif st.session_state.page == "Book B":
    st.title("📗 Book Title B")
    
    st.markdown("#### About the Book")
    st.write("Insert a detailed summary of Book B here.")
    
    st.markdown("#### About the Author")
    st.write("Author details for Book B series.")
    
    st.divider()
    
    col_img, col_dl = st.columns([1, 2])
    
    with col_img:
        st.image("https://via.placeholder.com/200x280", caption="Book B Series Cover")
        
    with col_dl:
        st.subheader("Download by Volume")
        st.download_button("📥 Download Volume 1", data="sample", file_name="BookB_Vol1.pdf", use_container_width=True)
        st.download_button("📥 Download Volume 2", data="sample", file_name="BookB_Vol2.pdf", use_container_width=True)
        st.download_button("📥 Download Volume 3", data="sample", file_name="BookB_Vol3.pdf", use_container_width=True)

# 4. ABOUT THE PROJECT (Mandatory Requirement)
elif st.session_state.page == "About":
    st.title("👤 Project Documentation")
    st.info("""
    - **Use-Case:** A structured digital library for multi-volume technical documentation.
    - **Target User:** Students and researchers needing specific volume access.
    - **Inputs:** Sidebar navigation buttons and file download requests.
    - **Outputs:** Specific PDF volumes and contextual author information.
    """)
    st.success("App Architecture: Session State Navigation with Multi-Component layout.")