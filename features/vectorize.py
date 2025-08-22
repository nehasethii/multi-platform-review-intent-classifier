import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# ------------------------------
# 1. Paths
# ------------------------------
input_path = "dataset/processed/clean_reviews.csv"
output_dir = "features"
os.makedirs(output_dir, exist_ok=True)

# ------------------------------
# 2. Load Cleaned Dataset
# ------------------------------
print("📂 Loading cleaned dataset...")
df = pd.read_csv(input_path)

# ------------------------------
# 3. TF-IDF Vectorization
# ------------------------------
print("✨ Applying TF-IDF vectorization...")

tfidf = TfidfVectorizer(
    max_features=5000,   # limit vocab size for efficiency
    ngram_range=(1,2),   # unigrams + bigrams
    min_df=5,            # word must appear in at least 5 docs
    max_df=0.8           # ignore words too frequent
)

X = tfidf.fit_transform(df["clean_review"].astype(str))

# ------------------------------
# 4. Save Vectorized Data
# ------------------------------
# Save features as .pkl (sparse matrix is big, better in binary)
vectorized_path = os.path.join(output_dir, "tfidf_features.pkl")
with open(vectorized_path, "wb") as f:
    pickle.dump(X, f)

# Save vectorizer for later use (important for inference)
vectorizer_path = os.path.join(output_dir, "tfidf_vectorizer.pkl")
with open(vectorizer_path, "wb") as f:
    pickle.dump(tfidf, f)

print(f"✅ TF-IDF features saved: {vectorized_path}")
print(f"✅ Vectorizer saved: {vectorizer_path}")
print("🔍 Shape of feature matrix:", X.shape)
