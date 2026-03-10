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
        
    if st.button("All the Lovers in the Night", use_container_width=True):
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
            st.image("images/lovers_in_the_night.jpg", use_container_width=True)
            if st.button("All the Lovers in the Night", use_container_width=True):
                ch_page("Book B")
    
    st.divider()
    st.image("images/kitty_banner.jpg", caption="This project is still under development")

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
        
        # --- PASTE START ---
        try:
            # Open and read the actual files from your 'tensura_pdfs' folder
            with open("tensura_pdfs/That Time I Got Reincarnated as a Slime Vol 1.pdf", "rb") as f1:
                pdf_v1 = f1.read()
            with open("tensura_pdfs/That Time I Got Reincarnated as a Slime Vol 2.pdf", "rb") as f2:
                pdf_v2 = f2.read()
            with open("tensura_pdfs/That Time I Got Reincarnated as a Slime Vol 3.pdf", "rb") as f3:
                pdf_v3 = f3.read()

            # The buttons now use the 'pdf_v' variables instead of "sample"
            st.download_button("Volume 1", data=pdf_v1, file_name="Tensura Vol 1.pdf", use_container_width=True)
            st.download_button("Volume 2", data=pdf_v2, file_name="Tensura Vol 2.pdf", use_container_width=True)
            st.download_button("Volume 3", data=pdf_v3, file_name="Tensura Vol 3.pdf", use_container_width=True)

        except FileNotFoundError:
            st.error("Check your filenames! The PDFs weren't found in 'tensura_pdfs'.")
        # --- PASTE END ---



# 3. BOOK TITLE B TAB
elif st.session_state.page == "Book B":
    st.title("All the Lovers in the Night")
    
    st.markdown("#### About the Book")
    st.write("a quiet, poignant novel about Fuyuko Irie, a lonely 34-year-old freelance proofreader in Tokyo. After realizing her life is void of connection, she begins a journey of self-discovery, fueled by a new, intense friendship with an older teacher named Mitsutsuka, leading her to confront her past traumas and emotional isolation.")
    
    st.markdown("#### About the Author")
    st.write("Mieko Kawakami")
    
    st.divider()
    
    col_img, col_dl = st.columns([1, 2])

    with col_img:
        st.image("images/lovers_in_the_night.jpg", caption="All the Lovers in the Night")
    
    with col_dl:
        st.subheader("Download Book")
        
        # --- PASTE START ---
        try:
            # Open and read the actual files from your 'tensura_pdfs' folder
            with open("Mieko_pdf/All the Lovers in the Night.pdf", "rb") as f1:
                pdf_v1 = f1.read()
         

            # The buttons now use the 'pdf_v' variables instead of "sample"
            st.download_button("Download", data=pdf_v1, file_name="All the Lovers in the Night.pdf", use_container_width=True)


        except FileNotFoundError:
            st.error("Check your filenames! The PDFs weren't found in 'All the Lovers in the Night.pdf'.")
        # --- PASTE END ---


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