import pandas as pd
import os

# ------------------------------
# Helper: load CSV with fallback encodings
# ------------------------------
def load_with_fallback(path):
    encodings = ["utf-8-sig", "latin1", "cp1252"]
    for enc in encodings:
        try:
            print(f"   ➡️ Trying encoding: {enc}")
            return pd.read_csv(path, encoding=enc, on_bad_lines="skip", low_memory=False)
        except Exception as e:
            print(f"   ❌ Failed with {enc}, trying next...")
    # Final fallback: force utf-8 and replace bad chars
    return pd.read_csv(path, encoding="utf-8", errors="replace", on_bad_lines="skip", low_memory=False)

# ------------------------------
# 1. Load Amazon dataset
# ------------------------------
print("📂 Loading Amazon dataset...")
amazon = load_with_fallback("dataset/raw/amazon_review.csv")
amazon_df = pd.DataFrame({
    "platform": "Amazon",
    "brand": amazon.get("brand", None),
    "product_name": amazon.get("name", None),
    "rating": amazon.get("reviews.rating", None),
    "review": amazon.get("reviews.text", None),
    "summary": amazon.get("reviews.title", None)
})

# ------------------------------
# 2. Load Flipkart dataset
# ------------------------------
print("📂 Loading Flipkart dataset...")
flipkart = load_with_fallback("dataset/raw/flipkart_review.csv")
flipkart_df = pd.DataFrame({
    "platform": "Flipkart",
    "brand": None,   # Flipkart doesn’t have brand, keeping placeholder
    "product_name": flipkart.get("Product_name", None),
    "rating": flipkart.get("Rate", None),
    "review": flipkart.get("Review", None),
    "summary": flipkart.get("Summary", None)
})

# ------------------------------
# 3. Merge datasets
# ------------------------------
df_all = pd.concat([amazon_df, flipkart_df], ignore_index=True)

# ------------------------------
# 4. Save processed dataset
# ------------------------------
output_dir = "dataset/processed"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "combined_reviews.csv")
df_all.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ Processed dataset saved: {output_path}")
print("Amazon rows:", len(amazon_df))
print("Flipkart rows:", len(flipkart_df))
print("Combined rows:", len(df_all))
print(df_all.info())
print(df_all.sample(5))
