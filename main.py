import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from xgboost import XGBClassifier

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("dataset.csv")

# Convert Result into Numbers
mapping = {
    "Fail":0,
    "Pass":1,
    "Excellent":2
}

df["Result"] = df["Result"].map(mapping)

X = df.drop("Result",axis=1)
y = df["Result"]

# -----------------------------
# Split Dataset
# -----------------------------

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Models
# -----------------------------

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(),

    "Random Forest":
        RandomForestClassifier(),

    "KNN":
        KNeighborsClassifier(),

    "SVM":
        SVC(),

    "Naive Bayes":
        GaussianNB(),

    "XGBoost":
        XGBClassifier(
            eval_metric='mlogloss'
        )
}

accuracy = {}

best_model = None
best_accuracy = 0

print("\n==============================")
print(" Student Performance Prediction ")
print("==============================\n")

for name,model in models.items():

    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test,pred)

    accuracy[name] = acc

    print(name,"=",round(acc*100,2),"%")

    if acc > best_accuracy:

        best_accuracy = acc
        best_model = model

print("\n----------------------------")
print("Best Model Selected")
print("----------------------------")

for k,v in accuracy.items():

    if v==best_accuracy:
        print(k)

print("Accuracy =",round(best_accuracy*100,2),"%")
joblib.dump(best_model, "model.pkl")
print("\nBest model saved as model.pkl")

# -----------------------------
# Prediction
# -----------------------------

print("\nEnter Student Details\n")

study=int(input("Study Hours : "))
attendance=int(input("Attendance : "))
assignment=int(input("Assignment Marks : "))
internal=int(input("Internal Marks : "))

prediction=best_model.predict([[study,attendance,assignment,internal]])

reverse={
0:"Fail",
1:"Pass",
2:"Excellent"
}

print("\nPrediction :",reverse[prediction[0]])

# -----------------------------
# Accuracy Graph
# -----------------------------

plt.figure(figsize=(10,5))

plt.bar(
accuracy.keys(),
accuracy.values()
)

plt.xticks(rotation=25)

plt.ylabel("Accuracy")

plt.title("Algorithm Comparison")

plt.tight_layout()

plt.savefig("static/accuracy_graph.png")

plt.show()