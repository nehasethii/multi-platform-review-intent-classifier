import pandas as pd
import os

# ------------------------------
# 1. Load dataset
# ------------------------------
file_path = "dataset/processed/combined_reviews.csv"
df = pd.read_csv(file_path, low_memory=False)

# ------------------------------
# 2. Ensure 'intent' column exists
# ------------------------------
if "intent" not in df.columns:
    df["intent"] = ""

# ------------------------------
# 3. Define a simple rule-based intent mapper
# ------------------------------
def map_intent(text):
    if not isinstance(text, str) or text.strip() == "":
        return "Unknown"
    
    text_lower = text.lower()

    # Keywords for each intent
    if any(k in text_lower for k in ["love", "great", "awesome", "perfect", "good", "amazing"]):
        return "Appreciation"
    elif any(k in text_lower for k in ["bad", "worst", "disappointed", "poor", "hate"]):
        return "Anger"
    elif any(k in text_lower for k in ["how", "what", "why", "does", "is it", "?"]):
        return "Question"
    elif any(k in text_lower for k in ["should", "could", "suggest", "recommend", "please"]):
        return "Suggestion"
    else:
        return "Unknown"

# ------------------------------
# 4. Apply mapping on reviews
# ------------------------------
df["intent"] = df["review"].fillna("") + " " + df["summary"].fillna("")
df["intent"] = df["intent"].apply(map_intent)

# ------------------------------
# 5. Save updated CSV
# ------------------------------
output_dir = "dataset/processed"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "combined_reviews_with_intent.csv")
df.to_csv(output_path, index=False)

print(f"✅ Intent column updated and saved: {output_path}")
print(df["intent"].value_counts())
