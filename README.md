# Flask Housing Price Prediction App

## Overview
This Flask application predicts house prices based on user input using a pre-trained Random Forest Regressor model. The app also provides descriptive statistics and visualizations of the dataset and integrates with MongoDB Atlas to store predictions and input data.

---

## Features

### Descriptive Statistics
- Display key statistics of the dataset.
- Identify missing values in the data.

### Data Visualizations
- **Scatter plot**: Median Income vs. Median House Value.
- **Heatmap**: Feature Correlation.
- **Boxplot**: Housing Median Age vs. Median House Value.

### Price Prediction
- Predict the median house value based on user inputs.
- Store input data and predictions in MongoDB Atlas.

### Database Integration
- MongoDB Atlas is used to store and manage prediction data.

---

## Prerequisites

### Software Requirements
- Python 3.8 or higher
- MongoDB Atlas account

### Libraries and Frameworks
The following Python libraries are used in this project:
- Flask
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- PyMongo

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
$ git clone <repository_url>
$ cd <repository_folder>
```

### Step 2: Install Dependencies
Use pip to install the required dependencies:
```bash
$ pip install -r requirements.txt
```

### Step 3: Configure MongoDB Atlas
1. Create a cluster on MongoDB Atlas.
2. Get your MongoDB URI (Connection String) and replace it in the `MONGO_URI` variable in the `app.py` file:
   ```python
   MONGO_URI = "<your_mongo_uri>"
   ```

### Step 4: Prepare Dataset
1. Place the dataset (`house.csv`) in the appropriate directory specified by `DATA_PATH_RAW` in the configuration.
2. Ensure the dataset contains the following columns:
   - `median_house_value` (Target)
   - `median_income`, `housing_median_age`, etc.

### Step 5: Run the Application
```bash
$ python app.py
```
The application will run on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) by default.

---

## Application Endpoints

### 1. Home Page
- **URL**: `/`
- **Description**: Displays the base page of the application.

### 2. Descriptive Statistics
- **URL**: `/descriptive`
- **Description**: Provides a summary of the dataset and missing value details.

### 3. Data Visualizations
- **URL**: `/visualization`
- **Description**: Renders scatter plots, heatmaps, and boxplots for data insights.

### 4. Price Prediction
- **URL**: `/predict`
- **Methods**: `GET`, `POST`
- **Description**: Predicts the house price based on user input and saves the data to MongoDB.

---

## Files and Directories

- **`app.py`**: Main Flask application file.
- **`config.py`**: Configuration file for dataset paths and other constants.
- **`requirements.txt`**: Contains all dependencies required for the project.
- **`templates/`**: HTML files for rendering web pages.
  - `base.html`: Home page template.
  - `des.html`: Descriptive statistics template.
  - `in.html`: Visualization template.
  - `pred.html`: Prediction page template.
- **`static/`**: Static assets like CSS, JS, and images.

---

## MongoDB Integration

### MongoDB Atlas
1. Ensure MongoDB Atlas IP access is configured to allow connections from your IP.
2. Handle large datasets efficiently to avoid memory issues.

---

## Screenshots

### Home Page
![Home Page](path/to/homepage_screenshot.png)

### Descriptive Statistics
![Descriptive Statistics]![image](https://github.com/user-attachments/assets/cf1dd6dd-c42c-4d3f-8b4a-859591efc7d7)


### Visualizations page
![image](https://github.com/user-attachments/assets/cedfbfef-188c-4731-8665-1dd07ca598bd)
![image](https://github.com/user-attachments/assets/c315c023-478c-42ed-854d-acf0be11f63b)



### Prediction Page
![Prediction Page]![image](https://github.com/user-attachments/assets/d7ba3470-3593-4e4e-9a56-e466ab3d45e9)

![image](https://github.com/user-attachments/assets/bbcec1ec-8d98-4954-9ea2-31e3b2686d39)
##Mongo db collection
![image](https://github.com/user-attachments/assets/d68a3adf-70f8-4e54-9230-7cea42564fcd)

---

## License
This project is licensed under the MIT License.
