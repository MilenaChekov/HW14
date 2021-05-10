import pandas as pd
from scipy.stats import pearsonr, spearmanr
import numpy as np

breast = pd.read_csv('healthy_breast.tsv', sep = '\t', index_col = 0)
SPI1 = breast.loc['SPI1']
breast['cor'] = [spearmanr(SPI1, breast.loc[gene])[0] for gene in breast.index]
breast = breast.loc[np.abs(breast['cor']) > 0.8]
print(breast.index)
