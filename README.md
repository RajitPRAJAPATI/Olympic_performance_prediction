# 🏅 Olympic Medal Prediction - Machine Learning Classification

## 📖 Project Overview
This project focuses on a multi-class classification problem to predict whether an Olympic athlete won a medal (and which one) based on various features like age, sex, height, weight, team, and event.

The dataset contains highly imbalanced classes, with the vast majority of athletes not winning a medal. This project compares five different algorithms to identify the best approach for this specific challenge.

## 📂 Dataset
* **File Name:** `olympics_final_final.csv`
* **Target Variable:** `Medal_Won`
    * `0`: No Medal (Majority Class)
    * `1, 2, 3`: Medal Winners (Minority Classes)
* **Features:** `Sex`, `Age`, `Height`, `Weight`, `Team`, `Event`

## 🛠️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/olympic-medal-prediction.git](https://github.com/your-username/olympic-medal-prediction.git)
    cd olympic-medal-prediction
    ```

2.  **Install dependencies:**
    Ensure you have Python installed. Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

3.  **Run the script:**
    ```bash
    python medal_prediction.py
    ```

## 🧠 Algorithms & Model Performance

The project evaluates the following algorithms. Note that due to class imbalance, **Accuracy** is often misleading. **Macro-Average F1-Score** is a better indicator of performance on the minority classes (actual medal winners).

| Algorithm | Model Type | Accuracy | F1-Score (Macro) | Key Observation |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | Ensemble Classification | **85.87%** | **0.36** | Best performer; captured some minority class patterns. |
| **Logistic Regression** | Linear Classification | 85.69% | 0.23 | High accuracy but failed to predict medal winners (Recall ≈ 0). |
| **Naive Bayes** | Probabilistic Classification | 85.56% | 0.23 | Failed to predict medal winners (Recall ≈ 0). |
| **Decision Tree** | Tree-based Classification | 79.35% | 0.38 | Balanced performance but lower overall accuracy. |
| **Linear Regression** | Regression | N/A | N/A | **Failed**: R² score of 0.02. Inappropriate for classification. |

## 🔑 Key Insights & Interview Concepts

### 1. The Accuracy Trap
* **Observation:** Most models achieved ~85% accuracy.
* **Reality:** This matches the percentage of athletes who *didn't* win a medal. Models like Logistic Regression simply predicted "No Medal" for everyone.
* **Takeaway:** Always use Precision, Recall, or F1-Score for imbalanced datasets.

### 2. Random Forest Superiority
* **Why it won:** As an ensemble method, Random Forest creates multiple decision trees and aggregates their results. This helps it capture non-linear relationships and handle the complex boundaries between "Medal" and "No Medal" better than linear models.

### 3. Why Linear Regression Failed
* **Reason:** Linear Regression predicts a continuous number (e.g., 0.45, 1.2), assuming a linear relationship. Classification targets are categories (0, 1, 2, 3). The model could not map the features to these discrete categories effectively.

## 🚀 Future Improvements
* **Resampling:** Apply SMOTE (Oversampling) to increase the number of medal-winning samples in the training data.
* **Class Weights:** Adjust algorithm parameters (e.g., `class_weight='balanced'`) to penalize misclassifying medal winners more heavily.
* **Feature Engineering:** Create new features, such as Body Mass Index (BMI) or historical team performance metrics.

## 📝 License
This project is open-source and available for educational purposes.
