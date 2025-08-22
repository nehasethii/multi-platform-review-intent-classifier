# Multi-Platform Review Intent Classifier

### Table of Contents

* [Project Overview](#project-overview)
* [Key Features](#key-features)
* [Tech Stack & Tools](#tech-stack--tools)
* [Project Description](#project-description)
* [Unique Aspects](#unique-aspects)
* [Who Can Benefit](#who-can-benefit)
* [Current Progress](#currrent-progress)
* [Future Scope](#future-scope)
* [Quick Setup & Run](#quick-setup--run)
* [Contributions](#contributions)
* [Contact](#contact)

---

## Project Overview

This project classifies user reviews from multiple e-commerce platforms into different **intents**: Appreciation, Anger, Question, and Suggestion. It combines **Naive Bayes models** with **rule-based overrides** to improve accuracy, especially for tricky or ambiguous reviews.

Users can analyze reviews per brand, compare multiple brands, and submit feedback about the app.

---

## Key Features

1. **Intent Classification**

   * Input a single review or upload a CSV file containing multiple reviews.
   * Classifies reviews into one of four intents.
   * Displays a **table of classified reviews** and a **pie chart** of intent distribution.

2. **Brand Analytics**

   * View **pie charts** and statistics of reviews per brand.
   * Understand customer sentiment distribution quickly.

3. **Brand Comparison**

   * Compare multiple brands using **bar charts**.
   * Identify which brand is more positively perceived.

4. **Feedback Submission**

   * Users can submit feedback, suggestions, or report issues.
   * All feedback is stored for analytics and future improvements.

5. **Rule-Based Overrides**

   * Uses common intent indicators like question words (`what`, `how`, `when`) and sentiment words (`good`, `amazing`, `hate`) to automatically correct frequently misclassified reviews.

---

## Tech Stack & Tools

* **Backend & ML**: Python, Scikit-learn, Naive Bayes, SMOTE (imbalanced dataset handling)
* **Frontend**: Streamlit for interactive web pages
* **Data Handling**: Pandas, Numpy
* **Visualization**: Matplotlib, Seaborn
* **Persistence**: Joblib for saving models and vectorizers
* **Version Control & Deployment**: Git, GitHub

---

## Project Description

The Multi-Platform Review Intent Classifier allows brands and businesses to **understand the intention behind user reviews at scale**. Manual reading of each review is time-consuming; this app **automates the classification** and provides actionable insights.

* **Single review input** for quick analysis
* **Batch CSV upload** for bulk reviews
* **Visualization** through pie and bar charts
* **Feedback collection** for continuous improvement

---

## Unique Aspects

* Combines **machine learning** with **rule-based corrections** for higher accuracy
* Supports **multi-platform review analysis**
* Handles **imbalanced datasets** efficiently
* Interactive visualizations for **brand insights**

---

## Who Can Benefit

* E-commerce businesses analyzing customer reviews
* Product managers evaluating user sentiment
* Data analysts studying feedback patterns
* Academics and students exploring NLP-based intent classification

---

## Current Progress

* Amazon and Flipkart reviews are fully integrated and functional.
* Intent classifier works for mulitiple text reviews in different rows and CSV uploads.
* Brand analytics and comparison visualizations are implemented.
* Feedback collection and storage is operational.

---

## Future Scope

* Add more e-commerce platforms and brands
* Incorporate deep learning models (e.g., BERT) for better context understanding
* Provide trend analysis over time
* Enable recommendations for product improvements based on intent

---

## Quick Setup & Run

```bash
git clone https://github.com/nehasethii/multi-platform-review-intent-classifier.git
cd multi-platform-review-intent-classifier
pip install -r requirements.txt
streamlit run Home.py
```

---

## Contributions

Contributions are welcome! You can:

* Submit issues or bug reports
* Suggest enhancements or new features
* Add new platforms or brands

---

## Contact
Reach out via the contact page on the app or open an issue here on GitHub.
