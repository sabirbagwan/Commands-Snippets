import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

columns = ['col1', 'cole2']

fig, axs = plt.subplots(len(columns), 1, figsize=(15, 6*len(columns)))

for i, col in enumerate(columns):
    ax = sns.countplot(x=data[col], order=data[col].value_counts().sort_values(ascending=False).index, ax=axs[i])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha = 'right')
    ax.set_title(col)
    ax.set_title(col, fontsize=18, fontweight='bold', fontfamily='Arial')
    ax.set_xlabel(col, fontsize=16, fontfamily='Arial')
    ax.set_ylabel('Count', fontsize=16, fontfamily='Arial')
    
    labels = data[col].value_counts().sort_values(ascending = False).values
    ax.bar_label(ax.containers[0], labels=labels, label_type='edge')
    
    
plt.tight_layout()
plt.show()
