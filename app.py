from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

labels = {
    0: "Fail ❌",
    1: "Pass ✅",
    2: "Excellent 🌟"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    study = float(request.form["study"])
    attendance = float(request.form["attendance"])
    assignment = float(request.form["assignment"])
    internal = float(request.form["internal"])

    data = pd.DataFrame([{
        "StudyHours": study,
        "Attendance": attendance,
        "AssignmentMarks": assignment,
        "InternalMarks": internal
    }])

    prediction = model.predict(data)[0]

    return render_template(
        "result.html",
        prediction=labels[int(prediction)]
    )

if __name__ == "__main__":
    app.run(debug=True)