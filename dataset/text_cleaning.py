import pandas as pd
import os
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ------------------------------
# 1. Setup NLTK resources
# ------------------------------
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ------------------------------
# 2. Text Cleaning Function
# ------------------------------
def clean_text(text):
    if pd.isna(text):
        return ""

    # Lowercase
    text = text.lower()

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", " ", text)

    # Remove numbers
    text = re.sub(r"\d+", " ", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove emojis & non-ASCII characters
    text = text.encode("ascii", "ignore").decode()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Remove stopwords & lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words]

    return " ".join(tokens)

# ------------------------------
# 3. Load Processed Dataset
# ------------------------------
input_path = "dataset/processed/combined_reviews.csv"
output_dir = "dataset/processed"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "clean_reviews.csv")

print("📂 Loading dataset...")
df = pd.read_csv(input_path)

# ------------------------------
# 4. Apply Cleaning
# ------------------------------
print("✨ Cleaning text data...")
df["clean_review"] = df["review"].astype(str).apply(clean_text)

# ------------------------------
# 5. Save Cleaned Dataset
# ------------------------------
df.to_csv(output_path, index=False)

print(f"✅ Cleaned dataset saved: {output_path}")
print(df[["review", "clean_review"]].sample(5))
