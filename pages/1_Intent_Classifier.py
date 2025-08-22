import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
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
# ------------------------------
# Load model, vectorizer, label encoder
# ------------------------------
@st.cache_data
def load_model():
    model = joblib.load("models/saved/intent_classifier_nb_smote.pkl")
    vectorizer = joblib.load("models/saved/tfidf_vectorizer.pkl")
    label_encoder = joblib.load("models/saved/label_encoder.pkl")
    return model, vectorizer, label_encoder

model, vectorizer, label_encoder = load_model()

# ------------------------------
# Rule-based override
# ------------------------------
def rule_based_intent(text):
    text_lower = text.lower()
    if "?" in text or any(w in text_lower for w in ["tell me","how", "what", "when", "where", "why"]):
        return "Question"
    elif any(w in text_lower for w in ["fluctuates","not","hate", "dislike", "disappointed", "frustrated", "angry", "bad", "worst", "slow","damaged","crashing"]):
        return "Anger"
    elif any(w in text_lower for w in ["but","should", "could", "would", "improve", "feature", "better"]):
        return "Suggestion"
    elif any(w in text_lower for w in ["love", "amazing", "great", "nice", "happy", "liked", "beautiful", "excellent", "stunning"]):
        return "Appreciation"
    else:
        return None  # fallback to ML

# ------------------------------
# Streamlit page layout
# ------------------------------
st.title("📝 Multi-Platform Review Intent Classifier")
st.subheader("Classify reviews and visualize intent distribution")

# Input type selection
input_type = st.radio("Select input type:", ["Paste Text", "Upload CSV"])

reviews = []

if input_type == "Paste Text":
    input_text = st.text_area("Paste reviews here (one per line):")
    if input_text.strip():
        reviews = [r.strip() for r in input_text.strip().split("\n") if r.strip()]
else:  # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        try:
            df_csv = pd.read_csv(uploaded_file)
            if "review" not in df_csv.columns:
                st.error("CSV must contain a 'review' column")
            else:
                reviews = df_csv["review"].dropna().astype(str).tolist()
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

# Classification
if st.button("Classify Reviews"):
    if not reviews:
        st.warning("Please provide reviews based on the selected input type!")
    else:
        df = pd.DataFrame({"review": reviews})
        
        # Rule-based classification
        df["intent"] = df["review"].apply(lambda x: rule_based_intent(x))
        
        # ML fallback for rows where rule didn't apply
        mask = df["intent"].isnull()
        if mask.any():
            X_tfidf = vectorizer.transform(df.loc[mask, "review"])
            preds = model.predict(X_tfidf)
            df.loc[mask, "intent"] = label_encoder.inverse_transform(preds)
        
        # ------------------------------
        # Pie chart first
        # ------------------------------
        st.subheader("Review Intent Distribution")
        intent_counts = df["intent"].value_counts()
        fig, ax = plt.subplots(figsize=(6,4))  # reduced size
        ax.pie(intent_counts, labels=[f"{i} ({c})" for i,c in zip(intent_counts.index,intent_counts.values)],
               autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
        st.pyplot(fig)
        
        # ------------------------------
        # Table of results
        # ------------------------------
        st.subheader("Detailed Classification")
        st.dataframe(df)
