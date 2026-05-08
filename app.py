from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Clean function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    news = request.form['news']
    cleaned = clean_text(news)
    vector = vectorizer.transform([cleaned])
    pred = model.predict(vector)[0]

    result = "Fake News ❌" if pred == 0 else "Real News ✅"

    # Send the original text back so it stays visible after analysis.
    return render_template("index.html", prediction_text=result, news_text=news)

if __name__ == "__main__":
    app.run(debug=True)
