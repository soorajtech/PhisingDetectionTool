import joblib
from scraper import get_page_content
from feature_extractor import extract_features

def predict_phishing(url):
    html = get_page_content(url)
    features = extract_features(url, html)
    model = joblib.load("model/phishing_model.pkl")
    prediction = model.predict([features])[0]
    return "Phishing 🚨" if prediction == 1 else "Legitimate ✅"

if __name__ == "__main__":
    url_input = input("Enter URL to check: ")
    result = predict_phishing(url_input)
    print("Result:", result)