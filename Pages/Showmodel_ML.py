import streamlit as st
import joblib
from gensim.models import Word2Vec
import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="My App", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    .navbar {
        background-color: #b4eeff;
        overflow: hidden;
        padding: 10px;
        text-align: center;
        border-radius: 15px;
    }
    .navbar a {
        display: inline-block;
        color: black;
        text-align: center;
        padding: 10px 20px;
        text-decoration: none;
        font-size: 18px;
        border-radius: 9px;
        border: 1.5px solid rgb(0, 197, 255);
    }
    .navbar a:hover {
        background-color: #00c5ff;
        color: white;
    }
    </style>
    
    <!-- HTML Navbar -->
    <div class="navbar">
        <a href="/" target="_self">🤖 Machine Learning</a>
        <a href="/NeuralNetwork" target="_self">Neural Network</a>
        <a href="/Showmodel_ML" target="_self">Machine Learrning Demo</a>
        <a href="/shownnmodel" target="_self">Neural Network Demo</a>
    </div>
    """,
    unsafe_allow_html=True
)

w2v_model = Word2Vec.load("word2vec.model")
nb_model = joblib.load("naive_bayes.pkl")
svm_model = joblib.load("svm.pkl")

try:
    X_test = joblib.load("X_test.pkl")
    y_test = joblib.load("y_test.pkl")
    nb_accuracy = accuracy_score(y_test, nb_model.predict(X_test))
    svm_accuracy = accuracy_score(y_test, svm_model.predict(X_test))
except FileNotFoundError:
    nb_accuracy, svm_accuracy = None, None

# Function to get sentence vector
def get_sentence_vector(sentence, w2v_model):
    words = sentence.split()
    word_vectors = [w2v_model.wv[word] for word in words if word in w2v_model.wv]
    
    if len(word_vectors) == 0:
        return np.zeros(w2v_model.vector_size)
    
    return np.mean(word_vectors, axis=0)

# Prediction function
def predict_sentiment(review):
    review_vec = get_sentence_vector(review, w2v_model).reshape(1, -1)
    
    start_nb = time.perf_counter()
    nb_pred = nb_model.predict(review_vec)[0]
    nb_time = time.perf_counter() - start_nb
    
    start_svm = time.perf_counter()
    svm_pred = svm_model.predict(review_vec)[0]
    svm_time = time.perf_counter() - start_svm
    
    return nb_pred, svm_pred, nb_time, svm_time

st.title("🔍 Sentiment Analysis with SVM & Naive Bayes")
st.write("ใส่ข้อความ Review แล้วดูว่าผลลัพธ์เป็น Positive, Negative หรือ Neutral")

review = st.text_area("📝 Add Reviews", "")

if st.button("🔮 Predict Sentiment"):
    if review.strip() == "":
        st.warning("⚠️ กรุณาใส่ข้อความรีวิวก่อนพยากรณ์")
    else:
        nb_result, svm_result, nb_time, svm_time = predict_sentiment(review)

        st.subheader("🎯 Result")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("📌 **Naive Bayes Model**")
            st.success(f"👉 ผลลัพธ์: {nb_result}")
            st.write(f"⏳ เวลาในการประมวลผล: {nb_time:.6f} วินาที")
        
        with col2:
            st.write("📌 **SVM Model**")
            st.info(f"👉 ผลลัพธ์: {svm_result}")
            st.write(f"⏳ เวลาในการประมวลผล: {svm_time:.6f} วินาที")
        
        st.subheader("📊 Performance Comparison")
        fig, ax = plt.subplots()
        model_names = ["Naive Bayes", "SVM"]
        times = [nb_time, svm_time]
        ax.bar(model_names, times, color=['blue', 'green'])
        ax.set_ylabel("Prediction Time (seconds)")
        ax.set_title("Comparison of Prediction Time")
        st.pyplot(fig)
        
        st.subheader("📈 Model Accuracy Comparison")
        if nb_accuracy is not None and svm_accuracy is not None:
            fig_acc, ax_acc = plt.subplots()
            accuracies = [nb_accuracy, svm_accuracy]
            ax_acc.bar(model_names, accuracies, color=['blue', 'green'])
            ax_acc.set_ylabel("Accuracy")
            ax_acc.set_title("Comparison of Model Accuracy")
            ax_acc.set_ylim([0, 1])
            st.pyplot(fig_acc)
        else:
            st.warning("⚠️ ไม่สามารถแสดงค่าความแม่นยำได้ เนื่องจากไม่มีชุดข้อมูลทดสอบ")