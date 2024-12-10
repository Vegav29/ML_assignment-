from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from io import BytesIO
import base64
from config import DATA_PATH_RAW
from pymongo import MongoClient  # MongoDB driver

app = Flask(__name__)

# MongoDB Atlas connection URI
MONGO_URI = "mongodb+srv://balajibj2003:v/ @tododb.wzmt0.mongodb.net/?retryWrites=true&w=majority&appName=tododb"
client = MongoClient(MONGO_URI)  # Connect to MongoDB
db = client['house_predictions']  # Use the database
collection = db['predictions']  # Use the predictions collection

# Load data
data_path = f"{DATA_PATH_RAW}/house.csv"
data = pd.read_csv(data_path)

# Handle missing values (replace with mean)
data.fillna(data.mean(), inplace=True)

# One-hot encode categorical data
data = pd.get_dummies(data, columns=['ocean_proximity'], drop_first=True)

# Split features and target
X = data.drop(columns=['median_house_value'])
y = data['median_house_value']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)

# Generate descriptive statistics
def get_summary(data):
    return data.describe().to_html(classes="table table-striped")

# Generate a visualization (returns a base64 string)
def create_plot(data, plot_type):
    plt.figure(figsize=(8, 6))
    
    if plot_type == "scatter":
        sns.scatterplot(x=data['median_income'], y=data['median_house_value'], alpha=0.7, color="orange")
        plt.title("Median Income vs Median House Value")
        plt.xlabel("Median Income")
        plt.ylabel("Median House Value")
    
    elif plot_type == "heatmap":
        correlation = data.corr()
        sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Feature Correlation Heatmap")
    
    elif plot_type == "boxplot":
        sns.boxplot(x=data['housing_median_age'], y=data['median_house_value'], palette="Set2")
        plt.title("Housing Median Age vs Median House Value")
        plt.xlabel("Housing Median Age")
        plt.ylabel("Median House Value")
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    
    return plot_data

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/descriptive")
def descriptive():
    summary = get_summary(data)
    missing = data.isnull().sum().to_dict()
    return render_template("des.html", summary=summary, missing=missing)

@app.route("/visualization")
def visualization():
    scatter_plot = create_plot(data, "scatter")
    heatmap = create_plot(data, "heatmap")
    boxplot = create_plot(data, "boxplot")
    return render_template("in.html", scatter_plot=scatter_plot, heatmap=heatmap, boxplot=boxplot)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None  # Initialize prediction to None
    if request.method == "POST":
        form_data = request.form.to_dict()
        
        # Convert the form data to float
        input_data = {key: float(value) for key, value in form_data.items()}
        
        # Convert the input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Ensure all model features are included (default to 0 if missing)
        for col in X.columns:
            if col not in input_df:
                input_df[col] = 0

        # Make the prediction
        prediction = rf.predict(input_df)[0]  # Use [0] to get the first prediction value

        # Save the input data and prediction to MongoDB
        record = {**input_data, "predicted_value": prediction}
        collection.insert_one(record)  # Insert the document into MongoDB

    return render_template("pred.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
