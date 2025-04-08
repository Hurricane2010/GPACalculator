import streamlit as st

st.set_page_config(page_title="Semester GPA", layout="centered")

st.title("📖 Semester GPA Calculator")
# rest of your GPA logic here
import streamlit as st

st.set_page_config(page_title="GPA Calculator", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f9f9fb;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .stSelectbox>div>div {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Smart GPA Calculator")
st.markdown("Easily calculate your **unweighted** and **weighted** GPA with support for **IB**, **AP**, **Honors**, and **Dual Enrollment** classes.")

# GPA mapping
grade_to_gpa = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

course_weights = {
    "Regular": 0.0,
    "Honors": 0.5,
    "AP": 1.0,
    "IB": 1.0,
    "Dual Enrollment": 1.0
}

num_courses = st.slider("📚 How many classes are you taking?", 1, 12, 6)

total_unweighted = 0
total_weighted = 0

st.markdown("---")

for i in range(num_courses):
    with st.expander(f"➕ Class {i+1}"):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            name = st.text_input(f"Course Name", key=f"name_{i}")
        with col2:
            grade = st.selectbox("Grade", ["A", "B", "C", "D", "F"], key=f"grade_{i}")
        with col3:
            course_type = st.selectbox("Course Type", ["Regular", "Honors", "AP", "IB", "Dual Enrollment"], key=f"type_{i}")

        base_gpa = grade_to_gpa[grade]
        weight = course_weights[course_type]
        total_unweighted += base_gpa
        total_weighted += base_gpa + weight

# Final calculation
if num_courses > 0:
    unweighted_gpa = total_unweighted / num_courses
    weighted_gpa = total_weighted / num_courses

    st.markdown("---")
    st.subheader("🎓 Your Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Unweighted GPA", f"{unweighted_gpa:.2f}")
    with col2:
        st.metric("Weighted GPA", f"{weighted_gpa:.2f}")

    st.success("Done! You can update any input above to recalculate in real time.")

