import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(page_title="Student Performance AI", layout="wide")

# =============================
# CUSTOM STYLE (DARK THEME)
# =============================
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.stMetric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# =============================
# LOAD MODEL
# =============================
model = joblib.load("models/model.pkl")

# =============================
# HEADER
# =============================
st.title("🎓 Student Performance AI System")
st.markdown("### Smart Prediction • Insights • Analytics")

# =============================
# SIDEBAR INPUT
# =============================
st.sidebar.header("📊 Enter Student Details")

study_hours = st.sidebar.slider("Study Hours", 1, 10, 5)
attendance = st.sidebar.slider("Attendance (%)", 50, 100, 75)
previous_marks = st.sidebar.slider("Previous Marks", 40, 100, 60)
sleep_hours = st.sidebar.slider("Sleep Hours", 4, 10, 7)

# =============================
# MAIN LAYOUT
# =============================
col1, col2, col3 = st.columns(3)

# =============================
# PREDICTION
# =============================
if st.sidebar.button("🚀 Predict Now"):

    data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_marks": [previous_marks],
        "sleep_hours": [sleep_hours]
    })

    score = model.predict(data)[0]

    # =============================
    # KPI CARDS
    # =============================
    with col1:
        st.metric("📊 Predicted Score", f"{score:.2f}")

    with col2:
        if score > 75:
            st.metric("🏆 Performance", "Excellent")
        elif score > 50:
            st.metric("⚠️ Performance", "Average")
        else:
            st.metric("❗ Performance", "Needs Improvement")

    with col3:
        st.metric("📈 Efficiency", f"{(score/100)*100:.0f}%")

    st.markdown("---")

    # =============================
    # PROGRESS BAR
    # =============================
    st.subheader("📊 Performance Level")
    st.progress(min(int(score), 100))

    # =============================
    # INSIGHTS
    # =============================
    st.subheader("🧠 Insights")

    if study_hours < 4:
        st.warning("👉 Increase study hours for better performance")
    if attendance < 70:
        st.warning("👉 Improve attendance")
    if sleep_hours < 6:
        st.warning("👉 Get proper sleep for better focus")

    if score > 75:
        st.success("🎉 Student is performing very well!")
    elif score > 50:
        st.info("👍 Decent performance, can improve further")
    else:
        st.error("⚠️ Immediate improvement needed!")

    # =============================
    # CHART
    # =============================
    st.subheader("📈 Input Analysis")

    features = ["Study", "Attendance", "Previous", "Sleep"]
    values = [study_hours, attendance/10, previous_marks/10, sleep_hours]

    plt.figure()
    plt.bar(features, values)
    plt.title("Student Input Overview")
    st.pyplot(plt)

# =============================
# FOOTER
# =============================
st.markdown("---")
st.markdown("🚀 Built with Machine Learning • Streamlit • Python")