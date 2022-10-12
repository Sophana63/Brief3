from dbfread import DBF
import csv
import pandas as pd

### Lecture du ficher .bdf
dbf= DBF('db/mar2012.dbf')
frame = pd.DataFrame(iter(dbf))    
print(frame)

### Lecture du fichier .csv 
df = pd.read_csv('db/mar2012.csv')
print(df.to_string()) 


### Lecture du fichier .txt
data = pd.read_csv('db/prima.txt')
print(data.to_string())