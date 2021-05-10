import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('BRCA_pam50.tsv', sep = '\t', index_col = 0)
df = df.loc[:, ['ESR1', 'PGR', 'ERBB2', 'MKI67', 'Subtype']]
for i in df['Subtype'].unique():
    sns.boxplot(data=df.loc[df['Subtype'] == i])
    plt.savefig("BRCA_pam50"+i+".png")
    plt.close()
