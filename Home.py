import streamlit as st

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

st.set_page_config(page_title="Multi-Platform Review Intent Classifier", layout="wide")

st.title("📊 Multi-Platform Review Intent Classifier")
st.markdown("""
Welcome to our project! 🚀  
This app classifies customer reviews into **intents** (Appreciation, Question, Suggestion, Anger).  

### Features:
- 📝 **Intent Classifier** → Classify a given review into intent categories  
- 🛒 **Brand Analytics** → Visualize review distribution for a single brand  
- ⚖️ **Brand Comparison** → Compare multiple brands on review intent distribution  
- 💡 **Feedback** → Share your thoughts and improvements  
""")
