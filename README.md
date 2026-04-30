# 🌍 Climate Data Analysis for COP32

## 📌 Project Overview

This project analyzes climate data from five African countries (Ethiopia, Kenya, Benin, Togo, and Sierra Leone) to identify climate trends, variability, and vulnerability. The goal is to produce data-driven insights that support Ethiopia’s position in COP32 climate discussions.

---

## 🎯 Objectives

* Clean and preprocess raw NASA climate datasets
* Perform Exploratory Data Analysis (EDA) for each country
* Compare climate patterns across countries
* Identify extreme weather events (heat and drought)
* Rank countries based on climate vulnerability
* Build an optional interactive dashboard using Streamlit

---

## 📂 Project Structure

climate-project/
│
├── data/ (ignored in GitHub)
├── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
│
├── app/
│   ├── main.py
│   └── utils.py
│
├── .github/workflows/ci.yml
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone <your-repo-link>
cd climate-project

### 2. Create virtual environment

python -m venv eldana
.\eldana\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

---

# 🔷 Task 1: Project Setup

### Steps Performed

* Initialized Git repository and pushed to GitHub
* Created and activated a virtual environment
* Installed required libraries (pandas, numpy, matplotlib, seaborn, scipy)
* Created `.gitignore` and excluded:

  * data/ folder
  * virtual environment
* Created `requirements.txt`
* Set up GitHub Actions CI workflow
* Organized project folder structure

---

# 🔷 Task 2: Data Profiling, Cleaning & EDA

## 1. Data Loading & Preparation

* Loaded CSV files using pandas
* Added a `Country` column for each dataset

## 2. Date Conversion

* Converted YEAR and DOY into a datetime column
* Extracted Month for seasonal analysis

## 3. Data Cleaning

* Replaced `-999` with NaN (NASA missing value indicator)
* Removed duplicate rows
* Checked missing values per column

## 4. Data Quality Analysis

* Generated summary statistics using `describe()`
* Calculated percentage of missing values
* Identified columns with more than 5% missing data

## 5. Outlier Detection

* Used Z-score to detect extreme values
* Flagged rows where |Z| > 3

## 6. Handling Missing Data

* Applied forward-fill for weather variables
* Dropped rows with more than 30% missing values

## 7. Exploratory Data Analysis (EDA)

* Time series plots for temperature (T2M)
* Rainfall (PRECTOTCORR) analysis
* Correlation heatmaps
* Scatter plots (temperature vs humidity, etc.)
* Distribution analysis (histograms and bubble charts)

## 8. Output

* Exported cleaned datasets:
  data/<country>_clean.csv

---

# 🔷 Task 3: Cross-Country Comparison

## 1. Data Integration

* Loaded all cleaned datasets
* Combined them into one DataFrame

## 2. Temperature Trend Comparison

* Plotted monthly average temperature for all countries
* Created summary table (mean, median, std)

## 3. Precipitation Comparison

* Created boxplots for rainfall distribution
* Generated summary statistics table

## 4. Extreme Event Analysis

* Counted extreme heat days (T2M_MAX > 35°C)
* Counted dry days (rainfall < 1 mm)
* Visualized results using bar charts

## 5. Statistical Testing

* Performed one-way ANOVA on temperature values
* Interpreted p-values to assess significance

## 6. Climate Vulnerability Ranking

* Ranked countries based on:

  * Temperature trends
  * Rainfall variability
  * Extreme heat and drought frequency

---

# 📢 Key Insights for COP32

* Some countries show significantly higher warming trends, indicating increased climate risk
* Rainfall variability differs greatly across countries, with some experiencing unstable precipitation patterns
* High frequency of extreme heat and dry days indicates severe climate stress
* Ethiopia shows moderate trends but increasing variability, suggesting emerging vulnerability
* Countries with extreme drought and heat patterns should be prioritized for climate finance

---

# 🔷 Bonus: Streamlit Dashboard

## Features Implemented

* Country multi-select filter
* Year range slider
* Temperature trend line chart
* Rainfall distribution boxplot

## Run Locally

streamlit run app/main.py

---

# 🚀 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Streamlit
* Git & GitHub Actions

---

# 🧠 Full Workflow Summary (Task 1 → Task 3)

## Task 1

* Set up project environment and GitHub repository
* Configured CI/CD pipeline
* Prepared project structure

## Task 2

* Loaded and cleaned climate datasets
* Converted date fields and handled missing values
* Detected and handled outliers
* Performed exploratory data analysis
* Generated insights and saved cleaned datasets

## Task 3

* Combined all country datasets
* Compared temperature and rainfall patterns
* Analyzed extreme weather events
* Conducted statistical testing
* Created a vulnerability ranking
* Generated insights for climate policy (COP32)

---

# 👩‍💻 Author

Eldana Derese
Data Science Student (ALX)
Addis Ababa University
