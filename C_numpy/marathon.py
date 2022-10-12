from email import header
import pandas as pd
import numpy as np

### Lecture du fichier .txt
data = pd.read_csv('db/marathon.txt', sep = "\t", names = ['ville','date', 'time', 'seconde'])
#data.columns = ["a", "b", "c", "etc."]
print(data)

tab_paris = []
tab_berlin = []

i = 0
for i in range (len(data)):
    if data['ville'][i] == "PARIS":
        tab_paris.append(1)
    else:
        tab_paris.append(0)
    
    if data['ville'][i] == "BERLIN":
        tab_berlin.append(1)
    else:
        tab_berlin.append(0)


data.insert(4, "isParis", tab_paris, True)
data.insert(5, "isBerlin", tab_berlin, True)

print(data)
print(data[['date', 'isParis', 'isBerlin']])
X = np.matrix(data[['date', 'isParis', 'isBerlin']])
Y = np.matrix(data[['seconde']])

A = (X.T * X).I * X.T * Y

print(A)
