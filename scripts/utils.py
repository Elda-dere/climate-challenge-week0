import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# LOAD & PREPROCESS
# ----------------------------
def load_and_parse(filepath, country):
    df = pd.read_csv(filepath)

    # Add country column
    df["Country"] = country

    # Replace sentinel values
    df.replace(-999, np.nan, inplace=True)

    # Create datetime
    df["Date"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")

    # Extract month
    df["Month"] = df["Date"].dt.month

    return df


# ----------------------------
# CLEANING & SUMMARY
# ----------------------------
def clean_data(df):
    # duplicates
    dup_count = df.duplicated().sum()
    df = df.drop_duplicates()

    # missing values
    missing = df.isna().sum()
    missing_pct = (missing / len(df)) * 100

    return df, dup_count, missing, missing_pct


def describe_data(df):
    return df.describe()


# ----------------------------
# OUTLIERS
# ----------------------------
def detect_outliers(df):
    cols = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR", "RH2M", "WS2M", "WS2M_MAX"]

    z_scores = df[cols].apply(zscore, nan_policy='omit')
    outliers = (np.abs(z_scores) > 3)

    return outliers, outliers.sum()


def handle_outliers(df):
    # cap instead of drop (safer for climate data)
    cols = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR", "RH2M", "WS2M", "WS2M_MAX"]

    for col in cols:
        upper = df[col].mean() + 3 * df[col].std()
        lower = df[col].mean() - 3 * df[col].std()

        df[col] = np.clip(df[col], lower, upper)

    return df


# ----------------------------
# MISSING VALUES
# ----------------------------
def handle_missing(df):
    # drop rows with >30% missing
    threshold = int(df.shape[1] * 0.3)
    df = df.dropna(thresh=df.shape[1] - threshold)

    # forward fill weather data
    df.fillna(method="ffill", inplace=True)

    return df


# ----------------------------
# EXPORT
# ----------------------------
def export_clean(df, country):
    path = f"../data/{country}_clean.csv"
    df.to_csv(path, index=False)
    return path


# ----------------------------
# TIME SERIES
# ----------------------------
def plot_temperature(df):
    monthly_temp = df.groupby("Month")["T2M"].mean()

    plt.figure()
    monthly_temp.plot(marker='o')
    plt.title("Monthly Avg Temperature")
    plt.xlabel("Month")
    plt.ylabel("T2M")
    plt.show()

    print("Warmest month:", monthly_temp.idxmax())
    print("Coolest month:", monthly_temp.idxmin())


def plot_precipitation(df):
    monthly_rain = df.groupby("Month")["PRECTOTCORR"].sum()

    plt.figure()
    monthly_rain.plot(kind="bar")
    plt.title("Monthly Rainfall")
    plt.xlabel("Month")
    plt.ylabel("PRECTOTCORR")
    plt.show()


# ----------------------------
# CORRELATION
# ----------------------------
def plot_correlation(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=False, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()


def scatter_plots(df):
    plt.figure()
    sns.scatterplot(x="T2M", y="RH2M", data=df)
    plt.show()

    df["T2M_RANGE"] = df["T2M_MAX"] - df["T2M_MIN"]

    plt.figure()
    sns.scatterplot(x="T2M_RANGE", y="WS2M", data=df)
    plt.show()


# ----------------------------
# DISTRIBUTION
# ----------------------------
def plot_distribution(df):
    plt.figure()
    sns.histplot(df["PRECTOTCORR"], bins=50, log_scale=True)
    plt.title("Rainfall Distribution")
    plt.show()


def bubble_chart(df):
    plt.figure()
    plt.scatter(df["T2M"], df["RH2M"], s=df["PRECTOTCORR"]*2, alpha=0.5)
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.title("Bubble Chart")
    plt.show()
