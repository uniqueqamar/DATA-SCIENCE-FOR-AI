import pandas as pd   

s = pd.Series([10,20,30], index = ["a",'b','c'])
print(s)


data ={"name":["alia","husna"], "Age":[21,30]}
df = pd.DataFrame(data)
print(df)