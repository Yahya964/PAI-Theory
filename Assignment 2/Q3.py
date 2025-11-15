import pandas as pd

print("Yahya Shamim")
print("24k-0020")

#Load and Inspect
df = pd.read_csv("Titanic-Dataset.csv")
report_lines = []
total_rows = len(df)
for col in df.columns:
    dtype = df[col].dtype
    missing = df[col].isna().sum()
    percent = round((missing / total_rows) * 100, 2)
    line = f"Column: {col} | Data Type: {dtype} | Missing Values: {missing} | Missing %: {percent}%"
    report_lines.append(line)
with open("inspect_report.txt", "w") as f:
    f.write("\n".join(report_lines))
#Handle Missing Data(Imputation)
df["Age"] = df["Age"].fillna(
    df.groupby(["Pclass", "Sex"])["Age"].transform("median")
)
embarked_mode = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(embarked_mode)
df = df.drop(columns=["Cabin"])
#Feature Engineering
df["FamilySize"] = df["SibSp"] + df["Parch"]
df["IsAlone"] = (df["FamilySize"] == 0).astype(int)
#Type Conversion
df["Age"] = df["Age"].astype("int64")
#Save Clean Data
df.to_csv("titanic_cleaned.csv", index=False)
print("Data cleaning completed successfully. Output saved as titanic_cleaned.csv.")


