import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

covid = pd.read_csv('human_coronavirus_aln_scores.tsv', sep = '\t', index_col = 0)
covid = 5000 - covid
model = TSNE(perplexity=50, metric= 'precomputed')
X = model.fit_transform(covid)
print(covid)
print(X)
covid[['TS1', 'TS2']] = X[:, :2]
covid['type'] = ['HCoV-HKU1']*20 + ['MERS-CoV']*20 + ['SARS-CoV-2']*20+['HCoV-229E']*20+['HCoV-NL63']*20+['HCoV-OC43']*20+['SARS-CoV']*20
sns.scatterplot(x='TS1', y='TS2', hue='type', data=covid)
plt.savefig("5_50.png")
plt.close()

