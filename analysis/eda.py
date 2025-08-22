# analysis/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ================================
# Setup
# ================================
print("🚀 Starting EDA script...")

# Path to processed dataset
csv_path = "dataset/processed/combined_reviews.csv"

# Create figures folder if it doesn't exist
figures_dir = "figures"
os.makedirs(figures_dir, exist_ok=True)

# ================================
# Load dataset
# ================================
print("📂 Loading dataset...")
df = pd.read_csv(csv_path)

# Convert rating to numeric (safe conversion)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

print("✅ Dataset Loaded successfully!\n")
print("🔍 Data Preview:")
print(df.head(), "\n")

# ================================
# Basic info
# ================================
print("🧾 Dataset Info:")
print(df.info(), "\n")

print("📊 Dataset Summary:")
print(df.describe(include="all"), "\n")

# ================================
# Platform-level stats
# ================================
print("⚖️ Average rating by platform:")
print(df.groupby("platform")["rating"].mean(), "\n")

print("🧮 Number of reviews by platform:")
print(df["platform"].value_counts(), "\n")

# ================================
# Plot 1: Review Count per Platform
# ================================
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="platform", palette="viridis")
plt.title("Number of Reviews per Platform")
plt.savefig(os.path.join(figures_dir, "reviews_per_platform.png"))
plt.close()

# ================================
# Plot 2: Rating Distribution per Platform (Normalized)
# ================================
plt.figure(figsize=(8,5))
sns.histplot(data=df, x="rating", hue="platform", multiple="dodge", bins=5, stat="probability")
plt.title("Normalized Rating Distribution per Platform")
plt.savefig(os.path.join(figures_dir, "rating_distribution_normalized.png"))
plt.close()

# ================================
# Brand-level Comparison
# ================================
print("🏷️ Average rating by Brand & Platform:")
brand_platform_avg = df.groupby(["brand", "platform"])["rating"].mean().unstack()
print(brand_platform_avg.head(), "\n")

# Plot 3: Avg Rating per Brand (Amazon vs Flipkart side-by-side)
top_brands = df["brand"].value_counts().head(10).index
df_top = df[df["brand"].isin(top_brands)]

plt.figure(figsize=(12,6))
sns.barplot(data=df_top, x="brand", y="rating", hue="platform", ci=None, palette="Set2")
plt.title("Average Rating per Brand (Top 10 Brands)")
plt.xticks(rotation=45)
plt.savefig(os.path.join(figures_dir, "avg_rating_per_brand.png"))
plt.close()

# ================================
# Plot 4: Rating Distribution per Brand (Normalized)
# ================================
plt.figure(figsize=(12,6))
sns.histplot(data=df_top, x="rating", hue="platform", multiple="dodge", bins=5, stat="probability")
plt.title("Normalized Rating Distribution (Top 10 Brands)")
plt.savefig(os.path.join(figures_dir, "rating_distribution_per_brand.png"))
plt.close()

print(f"✅ EDA completed! Figures saved in: {figures_dir}/")
