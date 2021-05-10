from scipy.stats import pearsonr, spearmanr

a = []
b = []
for i in range(1, 101):
    a.append(i)
    b.append(1/i)

print(pearsonr(a, b))
print(spearmanr(a, b))

c=[]
d=[]
for i in range(1, 20):
    c.append(i)
    d.append(i+20)

for i in range(20, 101):
    c.append(i+100)
    d.append(i-100000)

print(pearsonr(c, d))
print(spearmanr(c, d))