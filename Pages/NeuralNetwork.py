import streamlit as st

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

st.title("Neural Network")