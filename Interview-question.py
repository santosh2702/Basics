Department    Category    Expenditure   HR            Power        100 HR            Power        150 Infra         Manpower     200 HR            Manpower     100 Infra         Power        50 Infra         Power        150 Infra         Manpower     20 calculate the expediture on the basis department and category in python


import pandas as pd

# Input data
data = {
    "Department": ["HR", "HR", "Infra", "HR", "Infra", "Infra", "Infra"],
    "Category": ["Power", "Power", "Manpower", "Manpower", "Power", "Power", "Manpower"],
    "Expenditure": [100, 150, 200, 100, 50, 150, 20]
}

# Create DataFrame
df = pd.DataFrame(data)

# Group by Department and Category and calculate total expenditure
result = df.groupby(["Department", "Category"])["Expenditure"].sum().reset_index()

# Display result
print(result)
