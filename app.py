import streamlit as st
import pickle
import numpy as np

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Medical Insurance Prediction",
    page_icon="🏥",
    layout="wide",
)

# -------------------------------------------------------
# Custom CSS
# -------------------------------------------------------
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(to right,#0f172a,#1e293b,#334155);
}

/* Main Title */
.title{
    text-align:center;
    color:white;
    font-size:45px;
    font-weight:bold;
    margin-bottom:5px;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:35px;
}

/* Card */
[data-testid="stVerticalBlock"]{
    border-radius:18px;
}

/* Input Labels */
label{
    color:white !important;
    font-weight:bold;
}

/* Button */
div.stButton > button{
    width:100%;
    background:#22c55e;
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:20px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:#16a34a;
}

/* Metric Card */
.metric{
    background:#1e293b;
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    box-shadow:0px 0px 20px rgba(255,255,255,.15);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Load Model
# -------------------------------------------------------
model = pickle.load(open("D:/data_science_repo/Medical_price_Prediciton/model.pkl", "rb"))

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.markdown("<div class='title'>🏥 Medical Insurance Cost Prediction Dashboard</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Predict Medical Insurance Charges using Machine Learning</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# Layout
# -------------------------------------------------------
left, right = st.columns([2,1])

with left:

    st.subheader("📝 Enter Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=25
        )

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=25.0,
            step=0.1
        )

        children = st.selectbox(
            "Children",
            [0,1,2,3,4,5]
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        smoker = st.selectbox(
            "Smoker",
            ["Yes","No"]
        )

        region = st.selectbox(
            "Region",
            ["southwest","southeast","northwest","northeast"]
        )

    gender = 1 if gender=="Male" else 0
    smoker = 1 if smoker=="Yes" else 0

    region_dict={
        "southwest":0,
        "southeast":1,
        "northwest":2,
        "northeast":3
    }

    region=region_dict[region]

    input_data=np.array([[age,gender,bmi,children,smoker,region]],dtype=float)

    if st.button("🔍 Predict Insurance Cost"):

        prediction=model.predict(input_data)

        st.success(f"### 💰 Estimated Insurance Cost: **${prediction[0]:,.2f}**")

with right:

    st.markdown("""
    <div class='metric'>
    <h2>📊 Model Information</h2>
    <hr>
    <h4>Algorithm</h4>
    <p>Machine Learning Regression</p>

    <h4>Features Used</h4>

    ✔ Age<br>
    ✔ Gender<br>
    ✔ BMI<br>
    ✔ Children<br>
    ✔ Smoker<br>
    ✔ Region

    <br><br>

    <h4>Prediction</h4>

    Insurance Charges
    </div>
    """,unsafe_allow_html=True)

st.divider()

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Model", "Regression")

with col2:
    st.metric("Features", "6")

with col3:
    st.metric("Prediction", "Charges")

with col4:
    st.metric("Status", "Ready ✅")

st.divider()

st.info("💡 Insurance charges are estimated based on the customer information entered above.")