import streamlit as st

st.set_page_config(page_title="My App", layout="wide" ,initial_sidebar_state="collapsed")

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

st.title("🤖 Machine Learning")
st.write("การเตรียมข้อมูลสำหรับ Train Machine Learning ผมได้ทำการหาข้อมูลของ Dataset ในเว็บ kaggle.com โดยข้อมูลที่ใช้คือ Small Reviews.csv")
st.image("kaggle.png", caption="kaggle.com")
st.write("และหลังจากได้ Dataset ผมก็เลือกใช้ Macchine Learning เป็น SVM กับ Bayes ต่อไปนี้จะเป็นการ Train Model")
st.image("import.png")
st.write("ส่วนนี้จะเป็นการ Import File Dataset เข้ามาเพื่อ train")
st.image("Clean.png")
st.write("ส่วนนี้จะเป็นการ Clean ข้อมูลหลังจากเช็คข้อมูลแล้วว่ามีค่า Missing ที่ Name ได้ทำการแก้ค่า จาก NaN เป็น Unknow เพื่อให้ Dataset นั้นมีข้อมูลที่ครบถ้วน")
st.image("train1.png")
st.image("traim2.png")
st.write("ส่วนนี้จะเป็นการเริ่มเทรน Machine Learning และการแบ่งข้อมูล train และ test")
st.image("train3.png")
st.image("Result.png")
st.write("ส่วนสุดท้ายจะเป็นการเช็คผลลัพธ์ต่างๆที่ Train ไปเพื่อดูว่าระหว่าง SVM กับ Bayes อันไหนดีกว่ากัน")
