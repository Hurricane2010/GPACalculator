import streamlit as st

# Set the page layout
st.set_page_config(page_title="GPA Calculator", layout="centered")

# Add custom styling
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

# Title and description
st.title("Smart GPA Calculator")
st.markdown("Easily calculate your **unweighted** and **weighted** GPA with support for **IB**, **AP**, **Honors**, **Dual Enrollment**, and **Regular** classes.")

# GPA mapping (including GPA ranges)
grade_to_gpa = {
    "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, 
    "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0
}

# Sliders for course weight adjustments
with st.expander("Course Weights"):
    course_weights = {
        "Regular": st.slider("Regular Class Weight", 0.0, 1.0, 0.0, step=0.1),
        "Honors": st.slider("Honors Class Weight", 0.0, 1.0, 0.5, step=0.1),
        "AP": st.slider("AP Class Weight", 0.0, 1.0, 1.0, step=0.1),
        "IB": st.slider("IB Class Weight", 0.0, 1.0, 1.0, step=0.1),
        "Dual Enrollment": st.slider("Dual Enrollment Class Weight", 0.0, 1.0, 1.0, step=0.1)
    }

# Input number of courses for each category
with st.expander("Class Inputs"):
    num_honors = st.number_input("Number of Honors Classes", 0, 100, 0, help="Enter the number of Honors classes you are taking.")
    num_ap = st.number_input("Number of AP Classes", 0, 100, 0, help="Enter the number of AP classes you are taking.")
    num_ib = st.number_input("Number of IB Classes", 0, 100, 0, help="Enter the number of IB classes you are taking.")
    num_dual_enrollment = st.number_input("Number of Dual Enrollment Classes", 0, 100, 0, help="Enter the number of Dual Enrollment classes you are taking.")
    num_regular = st.number_input("Number of Regular Classes", 0, 100, 0, help="Enter the number of Regular classes you are taking.")

# Function to calculate GPA for each class type
def calculate_gpa(course_type, num_classes):
    if num_classes > 0:
        # Autofill with As
        default_grades = " ".join(["A"] * num_classes)

        # Limit the input text box to double the number of classes in characters
        max_characters = num_classes * 3  # Each grade and space (e.g., A, B+, C-)

        grades_input = st.text_input(f"Enter grades for {course_type} Classes (space separated)", 
                                     value=default_grades, max_chars=max_characters, key=f"{course_type}_grades",
                                     help="Enter your grades for the classes, separated by spaces. Use GPA ranges like 'A-', 'B+', 'C-', etc.")

        # Parse grades from the input text box
        grades = grades_input.strip().split()
        
        # Ensure the correct number of grades are provided
        if len(grades) != num_classes:
            st.warning(f"Please provide exactly {num_classes} grades for {course_type}.")
            return 0, 0, 0  # Invalid data

        total_unweighted = 0
        total_weighted = 0
        for grade in grades:
            base_gpa = grade_to_gpa.get(grade, 0)  # Default to 0 if invalid grade
            weight = course_weights[course_type]
            total_unweighted += base_gpa
            total_weighted += (base_gpa + weight)
        return total_unweighted, total_weighted, num_classes
    else:
        return 0, 0, 0

# Tab layout for displaying the results
tabs = st.tabs(["Honors & AP", "IB & Dual Enrollment", "Regular Classes"])

# Honors & AP GPA calculation
with tabs[0]:
    st.markdown("### Honors & AP Classes")
    unweighted, weighted, num_classes = calculate_gpa("Honors", num_honors)
    total_unweighted = unweighted
    total_weighted = weighted
    total_classes = num_classes

    unweighted, weighted, num_classes = calculate_gpa("AP", num_ap)
    total_unweighted += unweighted
    total_weighted += weighted
    total_classes += num_classes

# IB & Dual Enrollment GPA calculation
with tabs[1]:
    st.markdown("### IB & Dual Enrollment Classes")
    unweighted, weighted, num_classes = calculate_gpa("IB", num_ib)
    total_unweighted += unweighted
    total_weighted += weighted
    total_classes += num_classes

    unweighted, weighted, num_classes = calculate_gpa("Dual Enrollment", num_dual_enrollment)
    total_unweighted += unweighted
    total_weighted += weighted
    total_classes += num_classes

# Regular classes GPA calculation
with tabs[2]:
    st.markdown("### Regular Classes")
    unweighted, weighted, num_classes = calculate_gpa("Regular", num_regular)
    total_unweighted += unweighted
    total_weighted += weighted
    total_classes += num_classes

# Final GPA calculation
if total_classes > 0:
    unweighted_gpa = total_unweighted / total_classes
    weighted_gpa = total_weighted / total_classes

    st.markdown("---")
    st.subheader("🎓 Your Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Unweighted GPA", f"{unweighted_gpa:.2f}")
    with col2:
        st.metric("Weighted GPA", f"{weighted_gpa:.2f}")