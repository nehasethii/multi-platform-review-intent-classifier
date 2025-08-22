import pandas as pd

# Force all columns to be strings to avoid mixed-type issues
dtype_all = str

# Try reading with encoding='utf-8' first; if fails, use 'latin1'
try:
    amazon = pd.read_csv("dataset/raw/amazon_review.csv", dtype=dtype_all, low_memory=False)
except UnicodeDecodeError:
    amazon = pd.read_csv("dataset/raw/amazon_review.csv", dtype=dtype_all, encoding='latin1', low_memory=False)

try:
    flipkart = pd.read_csv("dataset/raw/flipkart_review.csv", dtype=dtype_all, low_memory=False)
except UnicodeDecodeError:
    flipkart = pd.read_csv("dataset/raw/flipkart_review.csv", dtype=dtype_all, encoding='latin1', low_memory=False)

# Quick info
print("Amazon Dataset:")
print(amazon.info())
print(amazon.head())

print("\nFlipkart Dataset:")
print(flipkart.info())
print(flipkart.head())
