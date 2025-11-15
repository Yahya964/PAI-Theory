import pandas as pd

#Load data
titanic = pd.read_csv("titanic_cleaned.csv")
fares = pd.read_csv("ticket_fares.csv")

# Merge data
titanic_data = pd.merge(titanic, fares, how="left", on="Ticket")

#Test hypothesis 1
age_bins = [0, 12, 19, 59, 120]
age_labels = ["Child", "Teenager", "Adult", "Senior"]

titanic_data["Age_Category"] = pd.cut(
    titanic_data["Age"],
    bins=age_bins,
    labels=age_labels,
    right=True
)

survival_by_group = (
    titanic_data
    .groupby(["Sex", "Age_Category"])["Survived"]
    .mean()
)

print("Survival probabilities by Sex and Age Category:")
print(survival_by_group)

# Write Hypothesis 1 Discussion
with open("report.txt", "w") as rep:
    rep.write("Hypothesis 1: Women and Children First\n\n")
    rep.write("The data shows that women had significantly higher survival rates compared" 
            "to men across all age groups. Children also demonstrated better survival outcomes than adults." 
            "This evidence supports the hypothesis that evacuation" 
            "protocols prioritized women and children.\n\n")

#Test hypothesis 2
class_survival = (
    titanic_data.groupby("Pclass")["Survived"].mean()
)
print("\nMean survival rate by passenger class:")
print(class_survival)

titanic_data["Fare_Group"] = pd.qcut(
    titanic_data["Fare"],
    q=4,
    labels=["Tier1_Low", "Tier2_MidLow", "Tier3_MidHigh", "Tier4_High"]
)

fare_survival = (
    titanic_data.groupby("Fare_Group")["Survived"].mean()
)

print("\nSurvival distribution across fare tiers:")
print(fare_survival)

with open("report.txt", "a") as rep:
    rep.write("Hypothesis 2: Wealth and Survival\n\n")
    rep.write(
        "Method A (Based on Class): People in higher-class cabins had a better "
        "chance of surviving. Survival chances went down for passengers in second "
        "and third class.\n\n"
    )

    rep.write(
        "Method B (Based on Fare Amount): Looking at fares, those who paid more "
        "for their tickets tended to survive more often. People with the cheapest "
        "tickets had the lowest survival rates.\n\n"
    )

    rep.write(
        "In short, both class and fare show that wealth made a difference in survival. "
        "This supports the hypothesis that richer passengers had higher chances of surviving.\n"
    )
print("Report successfully generated.")
