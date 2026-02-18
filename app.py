import streamlit as st

# 1. App Styling and Layout
st.set_page_config(page_title="Dr. Ravi's Pathology Lab", layout="wide", page_icon="🔬")

st.title("🔬 Dr. Ravi's Pathology Education Portal")
st.markdown("---")

# 2. Database of Videos (Add your actual YouTube links here)
# You can add as many videos as you want to this list!
video_data = [
    {"title": "Peripheral Blood Smear Examination", "cat": "Hematology", "url": "https://www.youtube.com/watch?v=EXAMPLE1"},
    {"title": "Malaria Parasite Identification", "cat": "Hematology", "url": "https://www.youtube.com/watch?v=EXAMPLE2"},
    {"title": "Tissue Processing & Embedding", "cat": "Histopathology", "url": "https://www.youtube.com/watch?v=EXAMPLE3"},
    {"title": "H&E Staining Protocol", "cat": "Histopathology", "url": "https://www.youtube.com/watch?v=EXAMPLE4"},
    {"title": "Platelet Count Manual Method", "cat": "Hematology", "url": "https://www.youtube.com/watch?v=EXAMPLE5"},
    {"title": "Fine Needle Aspiration Cytology (FNAC)", "cat": "Cytology", "url": "https://www.youtube.com/watch?v=EXAMPLE6"},
]

# 3. Sidebar Navigation & Search
# Add the logo to the top of the sidebar
st.sidebar.image("image_0.png", use_column_width=True)
st.sidebar.header("🔍 Find a Lesson")
search_query = st.sidebar.text_input("Search by topic (e.g. 'Malaria' or 'Platelets')")

st.sidebar.header("📂 Filter by Category")
category_list = ["All Categories", "Hematology", "Histopathology", "Cytology", "Biochemistry"]
selected_cat = st.sidebar.selectbox("Choose a subject", category_list)

# 4. Search Logic
filtered_videos = []

for video in video_data:
    # Check if search term is in the title
    is_searched = search_query.lower() in video["title"].lower()
    
    # Check if it matches the selected category
    is_in_cat = (selected_cat == "All Categories") or (video["cat"] == selected_cat)
    
    if is_searched and is_in_cat:
        filtered_videos.append(video)

# 5. Displaying the Results
if search_query:
    st.subheader(f"Results for: '{search_query}'")
elif selected_cat != "All Categories":
    st.subheader(f"Viewing: {selected_cat}")
else:
    st.subheader("All Training Videos")

# Create a clean grid for the videos
if filtered_videos:
    # This creates 2 columns for a nice mobile/web look
    cols = st.columns(2) 
    for index, video in enumerate(filtered_videos):
        with cols[index % 2]:
            st.info(f"**{video['cat']}**")
            st.markdown(f"### {video['title']}")
            st.video(video["url"])
            st.write("---")
else:
    st.error("No videos found. Try a different search term or category.")

# 6. Footer
st.sidebar.markdown("---")
st.sidebar.write("👨‍🏫 **Instructor:** Dr. Ravi")
st.sidebar.write("🧪 **For:** Lab Technicians & Students")
