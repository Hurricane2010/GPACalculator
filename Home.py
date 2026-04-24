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
    .stExpander > div > div {
        padding: 0;
    }
    .stExpanderHeader {
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Smart GPA Calculator")
st.markdown("Easily calculate your **unweighted** and **weighted** GPA with support for **IB**, **AP**, **Honors**, **Dual Enrollment**, and **Regular** classes.")

# GPA mapping for plus/minus grading
grade_to_gpa = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0
}

course_weights = {
    "Regular": 0.0,
    "Honors": 0.5,
    "AP": 1.0,
    "IB": 1.0,
    "Dual Enrollment": 1.0
}

class_types = ["Honors", "AP", "IB", "Dual Enrollment", "Regular"]

st.markdown("---")

total_weighted_points = 0
total_unweighted_points = 0
total_units = 0

tabs = st.tabs(["📘 GPA Input Tables", "⚙️ Modify Weights"])

with tabs[0]:
    for class_type in class_types:
        with st.expander(f"{class_type} Classes"):
            num_courses = st.number_input(f"Number of {class_type} Classes", min_value=0, max_value=100, value=0, key=f"{class_type}_num")

            for i in range(num_courses):
                cols = st.columns([2, 2])
                with cols[0]:
                    units = st.number_input(f"Units for Class {i+1}", min_value=0.0, value=1.0, step=0.5, key=f"{class_type}_unit_{i}")
                with cols[1]:
                    grade = st.text_input(f"Grade for Class {i+1}", value="A", key=f"{class_type}_grade_{i}").strip().upper()

                if grade in grade_to_gpa:
                    base_gpa = grade_to_gpa[grade]
                    weight = course_weights[class_type]
                    total_unweighted_points += base_gpa * units
                    total_weighted_points += (base_gpa + weight) * units
                    total_units += units
                else:
                    st.warning(f"Grade '{grade}' is not recognized and will be ignored for Class {i+1}.")

with tabs[1]:
    st.subheader("Modify Course Weights")
    for class_type in class_types:
        new_weight = st.slider(
            f"Weight for {class_type} Classes",
            min_value=0.0,
            max_value=2.0,
            value=course_weights[class_type],
            step=0.1,
            key=f"weight_{class_type}"
        )
        course_weights[class_type] = new_weight

st.markdown("---")

if total_units > 0:
    unweighted_gpa = total_unweighted_points / total_units
    weighted_gpa = total_weighted_points / total_units

    st.subheader("🎓 Your Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Unweighted GPA", f"{unweighted_gpa:.2f}")
    with col2:
        st.metric("Weighted GPA", f"{weighted_gpa:.2f}")

    st.success("Done! You can update any input above to recalculate in real time.")
else:
    st.info("Please enter at least one valid class to see your GPA.")
