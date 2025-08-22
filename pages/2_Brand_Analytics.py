import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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

st.set_page_config(page_title="Brand Analytics", layout="wide")
st.title("📊 Brand Analytics")

@st.cache_data
def load_brand_data():
    return pd.read_csv("dataset/processed/combined_reviews_with_intent.csv")

df = load_brand_data()

brands = df["platform"].unique()
selected_brand = st.selectbox("Select a brand:", brands)

# Filter for selected brand
brand_df = df[df["platform"] == selected_brand]

# Count intents
intent_counts = brand_df["intent"].value_counts()
total = intent_counts.sum()

# Pie chart without labels on slices
fig, ax = plt.subplots(figsize=(6,6))
wedges, _ = ax.pie(
    intent_counts,
    labels=None,  # no labels on slices
    startangle=90
)

# Create legend with percentages
labels_with_pct = [
    f"{intent} ({count/total*100:.1f}%)" for intent, count in intent_counts.items()
]

ax.legend(
    wedges,
    labels_with_pct,
    title="Intent",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10
)

ax.set_title(f"{selected_brand} Review Intent Distribution", fontsize=12)
st.pyplot(fig)

# Show raw counts as a table below
st.subheader("Review Counts by Intent")
st.table(intent_counts)
