#  Heart Disease Risk Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://heart-disease-predictor-dbwv9c5mxelzvduuq3xode.streamlit.app/)

An end-to-end Machine Learning web application designed to predict the risk of cardiovascular disease based on a patient's clinical and demographic data. 

##  Project Overview
Heart disease is a leading cause of mortality globally. This project leverages a **K-Nearest Neighbors (KNN)** classification model to provide a quick, real-time risk assessment. The model was trained on a comprehensive heart disease dataset and deployed via a responsive **Streamlit** user interface.

##  Live Demo
**Test the live application here:** [Heart Disease Predictor](https://heart-disease-predictor-dbwv9c5mxelzvduuq3xode.streamlit.app/)

##  Technology Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn (KNN Classifier, StandardScaler)
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn (in Jupyter Notebook)
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Community Cloud

##  Project Structure
* `HeartdiseaseFinal.ipynb`: Jupyter notebook containing Exploratory Data Analysis (EDA), model training, and evaluation.
* `app.py`: The Streamlit web application script.
* `*.pkl`: Serialized joblib files containing the trained KNN model, data scaler, and expected column structures.
* `requirements.txt`: Dependencies required for deployment.

##  How to Run Locally
To run this project on your local machine, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/swapnilpatil3/Heart-Disease-Predictor.git
   cd Heart-Disease-Predictor

Install dependencies
bash


pip install -r requirements.txt
Run the Streamlit app
bash


python -m streamlit run app.py
👨‍💻 Author
Swapnil Patil



4. Once you paste it, click the green **"Commit changes..."** button at the top right of the screen.
That is the absolute foolproof way to get it perfectly updated on your GitHub! Let me know when you've pasted it!
