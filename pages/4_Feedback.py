import streamlit as st
import pandas as pd
import os

st.markdown(
    """
    <style>
    /* Background image */
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/technology-hitech-3d-background-3d-illustration-futuristic-backdrop_262243-1785.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Optional overlay to make text more readable */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-color: rgba(0,0,0,0.3);  /* Dark overlay: adjust 0.1-0.5 */
        z-index: -1;
    }

    /* Text color */
    .stApp, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp p {
        color: #ffffff;  /* White text */
        text-shadow: 1px 1px 2px black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📝 Project Feedback")

st.markdown("""
Share your feedback about this project. Your suggestions help improve the intent classifier and analytics features.
""")

# --- Feedback Form ---
with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Email (optional)")
    feedback = st.text_area("Your Feedback / Suggestions", height=150)
    submit = st.form_submit_button("Submit Feedback")

# --- Handle Submission ---
feedback_file = "data/feedback.csv"
if submit:
    if feedback.strip() == "":
        st.warning("Please write your feedback before submitting.")
    else:
        new_entry = pd.DataFrame({
            "name": [name],
            "email": [email],
            "feedback": [feedback]
        })

        # Ensure data folder exists
        if not os.path.exists("data"):
            os.makedirs("data")
        
        # Append to CSV or create new
        if os.path.exists(feedback_file):
            new_entry.to_csv(feedback_file, mode="a", header=False, index=False)
        else:
            new_entry.to_csv(feedback_file, index=False)

        st.success("✅ Thank you! Your feedback has been submitted.")

# --- Show All Feedbacks ---
st.markdown("---")
st.subheader("What other users are saying:")

if os.path.exists(feedback_file):
    all_feedbacks = pd.read_csv(feedback_file)
    if not all_feedbacks.empty:
        st.dataframe(all_feedbacks)
    else:
        st.info("No feedback submitted yet.")
else:
    st.info("No feedback submitted yet.")
