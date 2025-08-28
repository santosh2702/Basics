Pandas

Pandas is like the Excel of Python — but 100x more powerful and programmable.
It is a data manipulation and analysis library that makes it easy to work with structured data (tables, rows, columns).

import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Amit", "Priya", "Ravi", "Neha"],
    "Age": [25, 28, 22, 32],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore"]
}

df = pd.DataFrame(data)

# Filtering
print(df[df["Age"] > 25])

# Grouping
print(df.groupby("City")["Age"].mean())

OUTPUT

    Name  Age      City
1  Priya   28    Mumbai
3   Neha   32 Bangalore

City
Bangalore    32.0
Delhi        23.5
Mumbai       28.0
Name: Age, dtype: float64



Numpy
if Pandas is the Excel of Python, then NumPy is the Calculator + Engine of Python.
Almost every data library (Pandas, Scikit-learn, TensorFlow, PyTorch) is built on top of NumPy.

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # [5 7 9]

