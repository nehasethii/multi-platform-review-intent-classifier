import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

st.set_page_config(page_title="Brand Comparison", layout="wide")
st.title("📊 Brand Comparison")

@st.cache_data
def load_brand_comparison_data():
    return pd.read_csv("dataset/processed/combined_reviews_with_intent.csv")

df = load_brand_comparison_data()

# Sidebar to select multiple brands
brands = df["platform"].unique()
selected_brands = st.multiselect("Select brands to compare:", brands, default=list(brands)[:2])

if selected_brands:
    comp_df = df[df["platform"].isin(selected_brands)]
    
    # Compute intent distribution per brand
    comparison = comp_df.groupby(["platform", "intent"]).size().unstack(fill_value=0)
    
    # Normalize to percentages per brand
    comparison_pct = comparison.div(comparison.sum(axis=1), axis=0) * 100
    
    # Plotting
    intents = comparison_pct.columns.tolist()
    x = np.arange(len(intents))
    width = 0.8 / len(selected_brands)  # width of each bar
    
    fig, ax = plt.subplots(figsize=(12,6))
    
    # Plot each brand
    for i, brand in enumerate(selected_brands):
        ax.bar(x + i*width, comparison_pct.loc[brand], width, label=brand)
        # Add percentage labels on top
        for j, val in enumerate(comparison_pct.loc[brand]):
            ax.text(x[j] + i*width, val + 0.5, f"{val:.1f}%", ha='center', va='bottom', fontsize=8)
    
    ax.set_xticks(x + width*(len(selected_brands)-1)/2)
    ax.set_xticklabels(intents, rotation=45, ha="right")
    ax.set_ylabel("Percentage of Reviews")
    ax.set_title("Intent Distribution Comparison Across Brands")
    ax.legend(title="Platform")
    
    st.pyplot(fig)
