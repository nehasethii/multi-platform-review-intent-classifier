# models/train_intent_nb_smote.py

import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib

# ------------------------------
# 1. Load dataset
# ------------------------------
data_path = "dataset/processed/combined_reviews_with_intent.csv"

df = pd.read_csv(
    data_path,
    dtype={"platform": str, "brand": str, "product_name": str,
           "review": str, "summary": str, "intent": str},
    low_memory=False
)

# Fill missing reviews/summaries
df["review"] = df["review"].fillna("")
df["summary"] = df["summary"].fillna("")

# Combine review + summary for features
df["text"] = df["review"] + " " + df["summary"]

# Keep only rows with non-empty intent
df = df[df["intent"].notna() & (df["intent"].str.strip() != "")].copy()

# ------------------------------
# 2. Encode labels
# ------------------------------
le = LabelEncoder()
df["intent_label"] = le.fit_transform(df["intent"])
classes = le.classes_

# ------------------------------
# 3. Train-test split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df["text"].values,
    df["intent_label"].values,
    test_size=0.2,
    random_state=42,
    stratify=df["intent_label"].values
)

# ------------------------------
# 4. TF-IDF Vectorization
# ------------------------------
vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# ------------------------------
# 5. Oversample minority classes with SMOTE
# ------------------------------
print("🚀 Oversampling minority classes with SMOTE...")
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train_tfidf, y_train)

# ------------------------------
# 6. Train Multinomial Naive Bayes
# ------------------------------
print("🚀 Training Multinomial Naive Bayes classifier...")
model = MultinomialNB()
model.fit(X_train_res, y_train_res)

# ------------------------------
# 7. Evaluation
# ------------------------------
y_pred = model.predict(X_test_tfidf)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=classes))

# ------------------------------
# 8. Save model, vectorizer, and LabelEncoder
# ------------------------------
os.makedirs("models/saved", exist_ok=True)

joblib.dump(model, "models/saved/intent_classifier_nb_smote.pkl")
joblib.dump(vectorizer, "models/saved/tfidf_vectorizer.pkl")
joblib.dump(le, "models/saved/label_encoder.pkl")

print("\n✅ Model saved: models/saved/intent_classifier_nb_smote.pkl")
print("✅ Vectorizer saved: models/saved/tfidf_vectorizer.pkl")
print("✅ LabelEncoder saved: models/saved/label_encoder.pkl")
