import streamlit as st
import os

# 1. App Styling
st.set_page_config(page_title="Dr. Ravi's Pathology", layout="wide", page_icon="🔬")

# 2. Add the Logo to Sidebar
# This specifically looks for your file: logo.png
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", use_container_width=True)
else:
    st.sidebar.error("Error: 'logo.png' not found. Check GitHub file name.")

st.sidebar.title("Dr. Ravi's Academy")
st.sidebar.markdown("---")

# 3. App Title
st.title("🔬 Dr. Ravi's Pathology Education Portal")
st.write("Welcome to the training hub for Lab Technicians.")

# 4. Search and Filter
search_query = st.sidebar.text_input("🔍 Search Lessons")
selected_cat = st.sidebar.selectbox("📂 Category", ["All", "Hematology", "Histopathology", "Cytology"])

# 5. Video Data
video_data = [
    {"title": "Peripheral Blood Smear", "cat": "Hematology", "url": "https://www.youtube.com/watch?v=EXAMPLE1"},
    {"title": "H&E Staining", "cat": "Histopathology", "url": "https://www.youtube.com/watch?v=EXAMPLE2"},
]

# 6. Show Videos
for video in video_data:
    if (search_query.lower() in video["title"].lower()) and (selected_cat == "All" or video["cat"] == selected_cat):
        st.subheader(f"[{video['cat']}] {video['title']}")
        st.video(video["url"])
        st.write("---")
