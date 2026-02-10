# Data Quality Validator App

An end-to-end Python application designed to automate the **Data Auditing and Cleaning** process. This tool allows users to upload datasets and instantly receive a health report, identify outliers, and perform automated cleaning.

##  Overview
Before any Machine Learning model can be built, the data must be "clean." This app identifies common data "diseases" such as missing values, duplicate records, and statistical outliers using Z-score analysis.

##  Key Features
- **Interactive Data Explorer:** Browse your dataset with high-performance tables.
- **Automated Quality Audit:** Detects missing values and duplicates instantly.
- **Statistical Outlier Detection:** Identifies "weird" data points using Z-score calculation (Z > 3).
- **Advanced Visualizations:** 
    - **Missing Value Heatmap:** Visualizes the density of missing information.
    - **Correlation Matrix:** Professionally formatted heatmap to see relationships between variables.
    - **Distribution Plots:** Interactive Plotly histograms to understand data skewness.
- **Automated Data Cleaning:** One-click fixes for removing duplicates and filling missing values.

##  Included Datasets (for Testing)
I have included a `data/` folder with two specific datasets to demonstrate the validator's power:
1. `loan_approval_data.csv`: A complex dataset involving financial metrics, perfect for testing Correlation and Outlier detection.
2. `sample_data.csv`: A smaller dataset with intentional errors to test cleaning and missing value detection.

##  Technology Stack
- **Frontend:** Streamlit
- **Data Engine:** Pandas & Numpy
- **Visualization:** Seaborn, Matplotlib, and Plotly
- **Environment:** Python 3.9+

##  Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone (https://github.com/sailakshmipattysapu/Data_quality_validator.git)
   cd Data-Quality-Validator

2. **Set Up a Virtual Environment**
**Windows:**
      python -m venv venv
      .\venv\Scripts\activate
**Mac/Linux:**
      python -m venv venv
      source venv/bin/activate
3. **Install Dependencies**
      pip install -r requirements.txt
4. **Run the App**
     streamlit run app.py
**How To Use**
**Upload:** Use the sidebar to upload either loan_approval_data.csv or sample_data.csv from the included data/ folder.
**Inspect:** View the Quality Analysis tab to see the "Health Report" of your file.
**Visualize:** Navigate to Visual Charts to identify patterns in missing data and feature relationships.
**Clean:** Go to the Data Cleaning tab to apply fixes and download your processed, high-quality dataset.
