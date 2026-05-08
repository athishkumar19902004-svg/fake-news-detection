# 📰 Fake News Detection System

## 📌 Project Overview

The **Fake News Detection System** is a Machine Learning and Natural Language Processing (NLP) based web application that classifies news articles as **Fake News** or **Real News**.

This project uses:

* Python
* Machine Learning
* Natural Language Processing (NLP)
* Flask
* HTML & CSS

The system preprocesses textual news data, extracts important features using TF-IDF, trains machine learning models, and predicts whether the news is fake or real.

---

# 🚀 Features

* Data preprocessing and cleaning
* NLP text processing
* Feature extraction using TF-IDF
* Multiple ML algorithms:

  * Naive Bayes
  * Logistic Regression
  * Random Forest
* Trained model saved using `.pkl`
* Flask backend
* Responsive frontend using HTML & CSS
* Fake/Real news prediction

---

# 🛠 Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Handling        |
| Scikit-learn | Machine Learning     |
| Flask        | Backend Framework    |
| HTML/CSS     | Frontend Design      |
| Pickle       | Model Saving         |
| TF-IDF       | Feature Extraction   |

---

# 📂 Project Structure

```text
fake_news_app/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── nlp_processed_dataset.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# 📊 Dataset

Dataset used:

* Fake.csv
* True.csv

The dataset contains:

* News title
* News text/content
* Labels:

  * `0` → Fake News
  * `1` → Real News

---

# ⚙️ Steps Performed

## 1. Data Collection

* Kaggle Dataset
* CSV files

## 2. Data Preprocessing

* Handle missing values
* Remove duplicates
* Convert labels

## 3. Text Cleaning (NLP)

* Convert text to lowercase
* Remove punctuation
* Remove stopwords
* Tokenization
* Lemmatization

## 4. Feature Extraction

* Bag of Words (BoW)
* TF-IDF

## 5. Model Selection

Applied:

* Naive Bayes
* Logistic Regression
* Random Forest

## 6. Model Training

* 80% Training Data
* 20% Testing Data

## 7. Prediction

* Input: News article
* Output: Fake or Real

---

# ▶️ How to Run the Project

## Step 1: Install Required Libraries

```bash
pip install flask pandas scikit-learn
```

---

## Step 2: Run Flask Application

```bash
python app.py
```

---

## Step 3: Open Browser

```text
http://127.0.0.1:5000/
```

---

# 🧠 Machine Learning Model

The project uses **Logistic Regression** as the final prediction model because it provides:

* High accuracy
* Fast execution
* Better performance for text classification

---

# 💾 Model Files

| File           | Description       |
| -------------- | ----------------- |
| model.pkl      | Trained ML model  |
| vectorizer.pkl | TF-IDF vectorizer |

---

# 📸 Output

The user enters a news article in the web interface, and the system predicts:

* ✅ Real News
* ❌ Fake News

---

# 🎯 Future Enhancements

* Deep Learning (LSTM/BERT)
* Live News API Integration
* User Authentication
* Deployment on Cloud
* Improved UI Design

---

# 👨‍💻 Author

**Your Name**

---

# 📄 License

This project is developed for educational and academic purp

