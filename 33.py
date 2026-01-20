import pandas as pd  
data = {
    "Class":["a","b","c"],
    "Score":[23,24,24],
    "Age":[19,19,18]
}
df =pd.DataFrame(data)
print("Original Dataset\n", df)

grouped= df.groupby("Class").mean
print(grouped)