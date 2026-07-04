import random
import pandas as pd

rows = []

for i in range(300):

    study = random.randint(1,10)
    attendance = random.randint(50,100)
    assignment = random.randint(5,25)
    internal = random.randint(10,50)

    score = (
        study*4 +
        attendance*0.4 +
        assignment*1.5 +
        internal
    )

    if score >= 95:
        result = "Excellent"

    elif score >= 70:
        result = "Pass"

    else:
        result = "Fail"

    rows.append([
        study,
        attendance,
        assignment,
        internal,
        result
    ])

df = pd.DataFrame(rows,
columns=[
    "StudyHours",
    "Attendance",
    "AssignmentMarks",
    "InternalMarks",
    "Result"
])

df.to_csv("dataset.csv",index=False)

print("Dataset Generated Successfully")