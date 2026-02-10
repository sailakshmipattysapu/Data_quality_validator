 Data Quality Validator
An automated tool designed to perform comprehensive�Data Auditing, Visualization, and Cleaning. This application helps Data Scientists and Analysts ensure their datasets are "ML-Ready" by identifying missing values, duplicates, and statistical outliers before the modeling phase.

 Key Features
*  Automated Audit:�Instantly detects missing values, duplicate rows, and data type inconsistencies.
*  Advanced Visualizations:
o Missing Value Heatmap:�Identify gaps in your data visually.
o Correlation Matrix:�Professionally formatted heatmap with optimized font sizing and decimal control.
o Distribution Analysis:�Interactive Plotly histograms to explore data skewness.
*  Outlier Detection:�Mathematically identifies "weird" data points using Z-Score Analysis (Z > 3).
*  Geospatial Mapping:�Automatically detects and plots Latitude and Longitude data.
*  Data Cleaning:�One-click fixes to remove duplicates, fill missing values with averages, and download the cleaned CSV.

 Included Datasets
This repository includes a�data/�folder with two specific datasets to demonstrate the tool's capabilities:
1. loan_approval_data.csv: A complex, real-world financial dataset used to test feature correlation and outlier detection in high-dimensional data.
2. sample_data.csv: A specialized dataset containing intentional errors (duplicates and nulls) designed to verify the validator's cleaning functions.

 Technology Stack
* Frontend:�Streamlit
* Data Processing:�Pandas,�NumPy
* Visualizations:�Seaborn,�Matplotlib,�Plotly

 Installation & Setup
Follow these steps to run the application locally:
1. Clone the Repository
codeBash
git clone https://github.com/sailakshmipattysapu/Data_quality_validator.git
cd Data-Quality-Validator
2. Set Up a Virtual Environment
Windows:
codeBash
python -m venv venv
.\venv\Scripts\activate
Mac/Linux:
codeBash
python -m venv venv
source venv/bin/activate
3. Install Dependencies
codeBash
pip install -r requirements.txt
4. Run the App
codeBash
streamlit run app.py

 How To Use
1. Upload:�Use the sidebar to upload either�loan_approval_data.csv�or�sample_data.csv�from the included�data/�folder.
2. Inspect:�View the�Quality Analysis�tab to see the "Health Report" of your file.
3. Visualize:�Navigate to�Visual Charts�to identify patterns in missing data and feature relationships.
4. Clean:�Go to the�Data Cleaning�tab to apply fixes and download your processed, high-quality dataset.

 License
Distributed under the MIT License. See�LICENSE�for more information.

