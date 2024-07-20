import pandas as pd

students = {
    "name": ["jerry", "rahul", "ravi"],
    "admitted-year": [2021, 2022, 2023],
    "rank": [12, 15, 56],
    "marks" : [99,98,92],
    "percentile" : [99.89, 99.45, 98.23]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(students)

# Display the DataFrame
print(df)

newData = pd.read_csv('demo.csv')
print(newData)

