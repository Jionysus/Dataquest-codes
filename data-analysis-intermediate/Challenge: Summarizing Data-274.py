## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[0:5])
print(recent_grads[0:5])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()
def cat_counts(df):
    cats = df['Major_category'].unique()
    counts = {}
    for cat in cats:
        major = df[df['Major_category'] == cat]
        total = major['Total'].sum()
        counts[cat] = total
    return counts

aa_cat_counts = cat_counts(all_ages)
rg_cat_counts = cat_counts(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage_jobs_sum = recent_grads['Low_wage_jobs'].sum()
recent_grads_sum = recent_grads['Total'].sum()
low_wage_proportion = low_wage_jobs_sum / recent_grads_sum
print(low_wage_proportion)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for m in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]
    rg_unemp_rate = recent_grads_row.iloc[0]['Unemployment_rate']
    aa_unemp_rate = all_ages_row.iloc[0]['Unemployment_rate']
    if rg_unemp_rate < aa_unemp_rate:
        rg_lower_count += 1

print(rg_lower_count)