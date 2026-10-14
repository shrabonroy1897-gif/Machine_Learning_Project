# ============================================================
# AUTOMATED ML EXPERIMENT
# 5 Algorithms × 3 Test Sizes × 5 PCA Components = 75 JPGs
# ============================================================

# ============================================================
# UTF-8 FIX FOR WINDOWS
# ============================================================

import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


# ============================================================
# IMPORTS
# ============================================================

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

from sklearn.linear_model import (
    LogisticRegression,
    Lasso
)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

warnings.filterwarnings("ignore")


# ============================================================
# 1. PROJECT PATHS
# ============================================================

# Folder containing this Python file
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# Dataset folder
DATASET_FOLDER = os.path.join(
    BASE_DIR,
    "datasets"
)

# Output folder
OUTPUT_FOLDER = os.path.join(
    BASE_DIR,
    "75_ML_Results"
)

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


# ============================================================
# 2. SETTINGS
# ============================================================

# PCA values
PCA_COMPONENTS = [
    5,
    10,
    15,
    20,
    25
]

# Test sizes
TEST_SIZES = [
    0.2,
    0.4,
    0.6
]

# Number of algorithms
NUMBER_OF_ALGORITHMS = 5


# ============================================================
# 3. LOAD ALL THREE DATASETS
# ============================================================

print("=" * 70)
print("LOADING DATASETS")
print("=" * 70)


tuesday_file = os.path.join(
    DATASET_FOLDER,
    "Tuesday-WorkingHours.pcap_ISCX.csv"
)

wednesday_file = os.path.join(
    DATASET_FOLDER,
    "Wednesday-workingHours.pcap_ISCX.csv"
)

thursday_file = os.path.join(
    DATASET_FOLDER,
    "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)


# Check that files exist
for file_path in [
    tuesday_file,
    wednesday_file,
    thursday_file
]:

    if not os.path.exists(file_path):

        print("\nERROR: Dataset file not found:")
        print(file_path)

        sys.exit(1)


# Load datasets

df1 = pd.read_csv(
    tuesday_file,
    low_memory=True
)

df2 = pd.read_csv(
    wednesday_file,
    low_memory=True
)

df3 = pd.read_csv(
    thursday_file,
    low_memory=True
)


print(
    "Tuesday rows   :",
    len(df1)
)

print(
    "Wednesday rows :",
    len(df2)
)

print(
    "Thursday rows  :",
    len(df3)
)


# ============================================================
# 4. COMBINE DATASETS
# ============================================================

dataset = pd.concat(
    [
        df1,
        df2,
        df3
    ],
    ignore_index=True
)


print("\nCombined dataset shape:")
print(dataset.shape)


# ============================================================
# 5. CLEAN COLUMN NAMES
# ============================================================

dataset.columns = (
    dataset.columns
    .str.strip()
)


# ============================================================
# 6. SEPARATE X AND Y
# ============================================================

X = dataset.iloc[:, :-1]

y = dataset.iloc[:, -1]


# ============================================================
# 7. CONVERT X TO NUMERIC
# ============================================================

print("\nConverting features to numeric...")


X = X.apply(
    pd.to_numeric,
    errors="coerce"
)


# ============================================================
# 8. REPLACE INF WITH NaN
# ============================================================

X.replace(
    [
        np.inf,
        -np.inf
    ],
    np.nan,
    inplace=True
)


# ============================================================
# 9. IMPUTE MISSING VALUES
# ============================================================

print("Imputing missing values...")


imputer = SimpleImputer(
    missing_values=np.nan,
    strategy="mean"
)


X = imputer.fit_transform(
    X
)


# ============================================================
# 10. ENCODE TARGET
# ============================================================

print("Encoding target labels...")


labelencoder_y = LabelEncoder()


y = labelencoder_y.fit_transform(
    y
)


class_names = labelencoder_y.classes_


print("\nClasses:")


for i, name in enumerate(class_names):

    # Convert possible problematic values to safe text
    safe_name = str(name).encode(
        "utf-8",
        errors="replace"
    ).decode(
        "utf-8",
        errors="replace"
    )

    print(
        i,
        "=",
        safe_name
    )


# ============================================================
# 11. MAKE SURE DATA IS NUMERIC
# ============================================================

X = np.asarray(
    X,
    dtype=np.float64
)

y = np.asarray(
    y
)


# ============================================================
# 12. INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("DATA INFORMATION")
print("=" * 70)


print(
    "Total samples :",
    X.shape[0]
)


print(
    "Total features:",
    X.shape[1]
)


print(
    "Total classes :",
    len(class_names)
)


print(
    "\nPCA components:",
    PCA_COMPONENTS
)


print(
    "Test sizes:",
    TEST_SIZES
)


TOTAL_EXPERIMENTS = (
    len(PCA_COMPONENTS)
    * len(TEST_SIZES)
    * NUMBER_OF_ALGORITHMS
)


print(
    "\nTotal experiments:",
    TOTAL_EXPERIMENTS
)


# ============================================================
# 13. EXPERIMENT COUNTER
# ============================================================

experiment_number = 0

results = []


# ============================================================
# 14. MAIN AUTOMATION LOOP
# ===========================================