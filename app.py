import streamlit as st
import os

# 1. App Configuration
st.set_page_config(page_title="Dr. Ravi's Pathology", layout="wide", page_icon="🔬")

# 2. Smart Logo Loader
# This look for common names so the app doesn't crash
logo_names = ["dr ravi logo.jpg", "logo.jpg", "logo.png", "image_0.png"]
found_logo = None

for name in logo_names:
    if os.path.exists(name):
        found_logo = name
        break

if found_logo:
    st.sidebar.image(found_logo, use_container_width=True)
else:
    st.sidebar.warning("Logo file not found. Please ensure your logo is uploaded to GitHub.")

# 3. App Title
st.title("🔬 Dr. Ravi's Pathology Education Portal")
st.markdown("---")

# 4. Search and Categories
search_query = st.sidebar.text_input("🔍 Search Topic (e.g., Malaria)")
category_list = ["All Categories", "Hematology", "Histopathology", "Cytology", "Biochemistry"]
selected_cat = st.sidebar.selectbox("📂 Filter by Subject", category_list)

# 5. Video Data (Replace 'EXAMPLE' with your actual YouTube codes)
video_data = [
    {"title": "Peripheral Blood Smear Examination", "cat": "Hematology", "url": "https://www.youtube.com/watch?v=EXAMPLE1"},
    {"title": "Malaria Parasite Identification", "cat": "Hematology", "url": "https://www.youtube.com/watch?v=EXAMPLE2"},
]

# 6. Display Logic
for video in video_data:
    is_searched = search_query.lower() in video["title"].lower()
    is_in_cat = (selected_cat == "All Categories") or (video["cat"] == selected_cat)
    
    if is_searched and is_in_cat:
        st.subheader(video["title"])
        st.video(video["url"])
        st.write("---")
