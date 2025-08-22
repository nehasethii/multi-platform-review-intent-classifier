import joblib
import numpy as np

model = joblib.load("models/saved/intent_classifier_nb_smote.pkl")
vectorizer = joblib.load("models/saved/tfidf_vectorizer.pkl")
le = joblib.load("models/saved/label_encoder.pkl")

def predict_intent(text):
    X = vectorizer.transform([text])
    pred = model.predict(X)
    return le.inverse_transform(pred)[0]
