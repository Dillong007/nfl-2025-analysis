import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

df1 = pd.read_csv(r"C:\Users\Dan\Desktop\Pro Development\Portfolio2.0\OLSfootball\data\Defense")
df2 = pd.read_csv(r"C:\Users\Dan\Desktop\Pro Development\Portfolio2.0\OLSfootball\data\Offense")

#Testing

#print(df1.head())
#print(df2.head())
#print(df2[["Y/P","Tm"]])



merged_table = pd.merge(df2, df1, on = "Tm")

merged_table["Point_Diff"] =(merged_table["PF"] - merged_table["PA"])

#print(merged_table[["Tm","Point_Diff"]])

merged_table = merged_table[
[
"Tm","Point_Diff", "Off_Yards_Per_Play", "Off_Net_Yards_Per_Attempt", "Off_Rush_Yards_Per_Attempt", "Off_Turnovers", "Off_Scoring_Percentage", "Off_Turnover_Percentage", "Off_Expected_Points", "Def_Yards_Per_Play_Allowed",
"Def_Net_Yards_Per_Attempt_Allowed","Def_Rush_Yards_Per_Attempt_Allowed","Def_Turnovers_Forced","Def_Scoring_Percentage_Allowed","Def_Turnover_Percentage_Forced","Def_Expected_Points_Allowed"
]
]


corr_with_point_diff = merged_table.drop(columns=["Tm"]).corr()["Point_Diff"].sort_values(ascending=False)
print(corr_with_point_diff)

y = merged_table["Point_Diff"]
pre_predictors = [
    "Off_Yards_Per_Play",
    "Off_Net_Yards_Per_Attempt",
    "Off_Rush_Yards_Per_Attempt",
    "Off_Turnovers",
    "Off_Scoring_Percentage",
    "Off_Turnover_Percentage",
    "Off_Expected_Points",
    "Def_Yards_Per_Play_Allowed",
    "Def_Net_Yards_Per_Attempt_Allowed",
    "Def_Rush_Yards_Per_Attempt_Allowed",
    "Def_Turnovers_Forced",
    "Def_Scoring_Percentage_Allowed",
    "Def_Turnover_Percentage_Forced",
    "Def_Expected_Points_Allowed",
]
predictors = ["Off_Expected_Points","Def_Scoring_Percentage_Allowed",]

X = merged_table[predictors]


X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())


X_no_const = merged_table[predictors]
vif_data = pd.DataFrame()
vif_data["Variable"] = X_no_const.columns
vif_data["VIF"] = [
    variance_inflation_factor(X_no_const.values, i)
    for i in range(X_no_const.shape[1])
]
print(vif_data.sort_values("VIF", ascending=False))