import streamlit as st
import pandas as pd
import joblib

# --- Page Configuration ---
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# --- Load Assets ---
# Using st.cache_resource so it only loads the models once and speeds up the app
@st.cache_resource
def load_assets():
    model = joblib.load("knn_heart_model.pkl")
    scaler = joblib.load("heart_scaler.pkl")
    expected_columns = joblib.load("heart_columns.pkl")
    return model, scaler, expected_columns

model, scaler, expected_columns = load_assets()

# --- UI Header ---
st.title("❤️ Heart Disease Prediction by Swapnil")
st.markdown("""
Welcome! Please provide your health metrics below. 
Our advanced K-Nearest Neighbors model will analyze your inputs to assess your risk of heart disease.
""")
st.divider()

# --- Input Form ---
st.subheader("🩺 Patient Information")

# Using columns to make the UI look organized and professional
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox(
        "Chest Pain Type", 
        ["ATA", "NAP", "TA", "ASY"], 
        help="ATA: Atypical Angina | NAP: Non-Anginal Pain | TA: Typical Angina | ASY: Asymptomatic"
    )
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol (mg/dL)", 0, 600, 200)

with col2:
    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL", 
        [0, 1], 
        format_func=lambda x: "Yes (1)" if x == 1 else "No (0)"
    )
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

st.divider()

# --- Predict Button ---
# Center the button by wrapping it in columns
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    predict_clicked = st.button("🔍 Predict Risk of Heart Disease", use_container_width=True)

if predict_clicked:
    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result with enhanced styling
    st.markdown("---")
    st.subheader("📝 Prediction Result")
    
    if prediction == 1:
        st.error("⚠️ **High Risk of Heart Disease Detected.** Please consult a healthcare professional.")
    else:
        st.success("✅ **Low Risk of Heart Disease!** Keep maintaining a healthy lifestyle.")
        st.balloons()