import pandas as pd

def load_brand_data(brand):
    df = pd.read_csv("dataset/processed/combined_reviews_with_intent.csv")
    df = df[df['platform'].str.lower() == brand.lower()]
    return df['intent'].value_counts().reset_index().rename(columns={'index':'intent','intent':'count'})

def load_brand_comparison_data(brands):
    df = pd.read_csv("dataset/processed/combined_reviews_with_intent.csv")
    df = df[df['platform'].str.lower().isin([b.lower() for b in brands])]
    return df.groupby(['platform','intent']).size().reset_index(name='count')
