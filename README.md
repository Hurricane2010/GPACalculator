# 🎓 Smart GPA Calculator

A clean, real-time GPA calculator built with Streamlit — currently in active use by the college counselor at **Monterey High School**. Supports unweighted and weighted GPA calculations across all major course types.

---

## Overview

Students enter their courses, units, and grades and instantly see their unweighted and weighted GPA. The tool handles the full range of course types found in a typical high school schedule and allows counselors or students to customize weighting to match their school's specific policy.

**Live Demo:** *[[Demo](https://calcgpa.streamlit.app/)*

---

## Features

- **Unweighted and weighted GPA** calculated simultaneously in real time
- **Supports all major course types** — Regular, Honors, AP, IB, and Dual Enrollment
- **Plus/minus grading** — full A+ through F scale with accurate GPA point mapping
- **Configurable weights** — counselors or students can adjust the bonus weight for each course type via sliders, matching any school's specific weighting policy
- **Per-class unit support** — handles courses with different credit weights (0.5, 1.0, 1.5, etc.)
- **Clean, minimal UI** — designed to be simple enough for any student to use without instructions

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

**2. Install dependencies**
```bash
pip install streamlit
```

**3. Run the app**
```bash
streamlit run Home.py
```

Opens in your browser at `http://localhost:8501`.

---

## How to Use

1. Go to the **GPA Input Tables** tab
2. Expand the section for each course type you have (Honors, AP, IB, etc.)
3. Enter the number of classes, then fill in units and letter grade for each
4. Your **Unweighted GPA** and **Weighted GPA** update instantly at the bottom
5. To adjust weights for your school's policy, go to the **Modify Weights** tab and use the sliders

### Default weights

| Course Type | Bonus Weight |
|---|---|
| Regular | +0.0 |
| Honors | +0.5 |
| AP | +1.0 |
| IB | +1.0 |
| Dual Enrollment | +1.0 |

These can be changed at any time without restarting the app.

---

## Grade Scale

| Grade | GPA Points |
|---|---|
| A+ / A | 4.0 |
| A- | 3.7 |
| B+ | 3.3 |
| B | 3.0 |
| B- | 2.7 |
| C+ | 2.3 |
| C | 2.0 |
| C- | 1.7 |
| D+ | 1.3 |
| D | 1.0 |
| D- | 0.7 |
| F | 0.0 |

---

## Deployment

The app is deployed on Streamlit Community Cloud. See the deployment section below for instructions on hosting your own instance.

---

## License

MIT
