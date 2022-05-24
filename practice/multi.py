import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("/Users/okawatomoaki/Documents/nltk/practice/multi.csv")

num_list = list(df.select_dtypes(exclude=object).columns)

fig = plt.figure(figsize=(10,10))

for i in range(len(num_list)):
    print(i)
    plt.subplot(4, 2, i+1)
    plt.title(num_list[i])
    plt.hist(df[num_list[i]])

plt.tight_layout()
plt.show()
