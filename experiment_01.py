# Experiment 1

import pandas as pd

url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'
df = pd.read_csv(url)
print(df.head())


df.to_csv("output.csv", index=False)

# Convert DataFrame to JSON and back
json_data = df.to_json()
df_json = pd.read_json(json_data)
print(df_json.head())

# Save and load Excel files
df.to_excel("output.xlsx", index=False)
df_excel = pd.read_excel("output.xlsx")
print(df_excel.head())
