# Automated Machine Learning Experiment

## Overview

This project automates **75 machine-learning experiments** by combining:

- **5 algorithms**
- **3 train/test split sizes**
- **5 PCA component settings**

The program trains each model, calculates evaluation metrics, generates a JPG report for every experiment, and saves all results to a CSV file.

The experiment configuration is:

- PCA components: `5, 10, 15, 20, 25`
- Test sizes: `20%, 40%, 60%`
- Algorithms:
  1. Logistic Regression
  2. AdaBoost
  3. Lasso Regression
  4. Gaussian Naive Bayes
  5. Quadratic Discriminant Analysis

**Total experiments: 5 × 3 × 5 = 75**

The implementation follows the preprocessing, PCA, model-training, metric-generation, and result-saving workflow in `project.py`. fileciteturn0file0L1-L3

---

## Project Structure

```text
project/
│
├── project.py
├── Tuesday-WorkingHours.pcap_ISCX.csv
├── Wednesday-workingHours.pcap_ISCX.csv
├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
│
└── 75_ML_Results/
    ├── 01_Logistic_Regression_Test_20_PCA_5.jpg
    ├── ...
    ├── 75_....jpg
    └── ALL_75_RESULTS.csv
```

The script reads the three PCAP-ISCX CSV datasets and combines them into one dataset. fileciteturn0file0L55-L92

---

## Requirements

Python 3.x with the following libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### Main libraries used

- **NumPy** — numerical operations
- **Pandas** — dataset loading and manipulation
- **Matplotlib** — result visualization
- **Seaborn** — confusion-matrix heatmaps
- **Scikit-learn** — preprocessing, PCA, machine-learning algorithms, and evaluation metrics

---

## Input Datasets

The program expects these files in the same directory as `project.py`:

```text
Tuesday-WorkingHours.pcap_ISCX.csv
Wednesday-workingHours.pcap_ISCX.csv
Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
```

The three datasets are loaded with Pandas and concatenated into a single dataset. fileciteturn0file0L56-L92

---

## Data Preprocessing

The following preprocessing steps are performed:

### 1. Clean column names

Whitespace is removed from column names.

### 2. Separate features and target

The script treats:

- all columns except the last column as `X`
- the last column as `y`

### 3. Convert features to numeric

Non-numeric values are converted to `NaN`.

### 4. Replace infinite values

Both positive and negative infinity are replaced with `NaN`.

### 5. Handle missing values

Missing values are replaced using `SimpleImputer` with the **mean** strategy.

### 6. Encode target labels

`LabelEncoder` converts the target classes into numerical labels.

These steps are implemented in the preprocessing section of the script. fileciteturn0file0L96-L169

---

## PCA

Principal Component Analysis (PCA) is applied to reduce the feature dimensions.

The experiment uses:

```python
PCA_COMPONENTS = [5, 10, 15, 20, 25]
```

PCA is fitted only on the training data and then used to transform the test data. fileciteturn0file0L43-L50 fileciteturn0file0L248-L263

This helps ensure that information from the test set is not used when fitting PCA.

---

## Train/Test Splits

Three different test-set sizes are evaluated:

```python
TEST_SIZES = [0.2, 0.4, 0.6]
```

This corresponds to:

| Test Size | Training Data | Test Data |
|---:|---:|---:|
| 0.2 | 80% | 20% |
| 0.4 | 60% | 40% |
| 0.6 | 40% | 60% |

The split uses `random_state=0` and stratified sampling. fileciteturn0file0L43-L48 fileciteturn0file0L209-L229

---

## Machine Learning Algorithms

### 1. Logistic Regression

A classification model configured with:

```python
LogisticRegression(
    random_state=0,
    max_iter=1000
)
```

### 2. AdaBoost

```python
AdaBoostClassifier()
```

### 3. Lasso Regression

```python
Lasso(alpha=0.1)
```

The script treats this model as a regression model and converts its continuous predictions into class labels by rounding and clipping them to the valid class range.

### 4. Gaussian Naive Bayes

```python
GaussianNB()
```

### 5. Quadratic Discriminant Analysis

```python
QuadraticDiscriminantAnalysis(
    solver="eigen",
    shrinkage="auto"
)
```

These five algorithms are defined in the experiment loop. fileciteturn0file0L267-L307

---

## Evaluation Metrics

Every experiment calculates:

- Accuracy
- Weighted Precision
- Weighted Recall
- Weighted F1 Score
- Confusion Matrix
- Classification Report

The metrics are calculated using Scikit-learn. fileciteturn0file0L384-L443

### Accuracy

Measures the proportion of predictions that are correct.

### Precision

Measures how many predicted samples are actually correct.

### Recall

Measures how many actual samples are correctly identified.

### F1 Score

Combines precision and recall into a single metric.

### Confusion Matrix

Shows the relationship between actual and predicted classes.

---

## Generated Results

For every experiment, the program creates a JPG containing:

1. Confusion Matrix
2. Algorithm and experiment settings
3. Accuracy
4. Precision
5. Recall
6. F1 Score
7. Classification Report

The generated files are saved inside:

```text
75_ML_Results/
```

The filename contains the experiment number, algorithm, test size, and PCA component count. fileciteturn0file0L509-L526

Example:

```text
01_Logistic_Regression_Test_20_PCA_5.jpg
```

---

## CSV Results

After all experiments are completed, the program creates:

```text
75_ML_Results/ALL_75_RESULTS.csv
```

The CSV stores:

```text
Experiment
Algorithm
Test Size
PCA Components
Accuracy
Precision
Recall
F1 Score
```

This makes it easier to compare all 75 experiments in a spreadsheet or data-analysis tool. fileciteturn0file0L732-L749

---

## How to Run

### 1. Clone/download the project

Place `project.py` and all three CSV datasets in the same folder.

### 2. Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

### 3. Run the program

```bash
python project.py
```

### 4. Wait for all experiments

The program will display progress such as:

```text
EXPERIMENT 1/75
EXPERIMENT 2/75
...
EXPERIMENT 75/75
```

### 5. Check the output

After completion, open:

```text
75_ML_Results/
```

You should find the generated JPG reports and:

```text
ALL_75_RESULTS.csv
```

The script also prints the number of generated JPG files and the output paths when it finishes. fileciteturn0file0L753-L800

---

## Experiment Design

The complete experiment matrix is:

```text
5 Algorithms
        ×
3 Test Sizes
        ×
5 PCA Settings
        =
75 Experiments
```

Each combination produces one experiment result and one JPG visualization.

---

## Output Example

A generated report contains information similar to:

```text
Algorithm:
Logistic Regression

Test Size:
0.2

PCA Components:
5

Accuracy:
0.xxxx

Precision:
0.xxxx

Recall:
0.xxxx

F1 Score:
0.xxxx
```

along with the confusion matrix and classification report.

---

## Notes

- The input CSV files must be available in the project directory.
- The script automatically creates the `75_ML_Results` directory if it does not already exist.
- PCA is fitted using the training set and then applied to the test set.
- The experiment uses `random_state=0` for reproducibility of the train/test split.
- Lasso is a regression model in this implementation; its continuous predictions are rounded and clipped before classification metrics are calculated. fileciteturn0file0L351-L381

---

## Author

**Machine Learning Experiment Project**

Automated comparison of multiple machine-learning algorithms across different test-set sizes and PCA dimensionality settings.
