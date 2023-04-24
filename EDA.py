import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

columns = ['col1', 'col2']

fig, axs = plt.subplots(len(columns), 1, figsize=(15, 6*len(columns)))

for i, col in enumerate(columns):
    ax = sns.countplot(x=data[col], order=data[col].value_counts().sort_values(ascending=False).index, ax=axs[i])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha = 'right')
    ax.set_title(col)

plt.tight_layout()
plt.show()
