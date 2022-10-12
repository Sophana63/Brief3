import pandas as pd

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

### Lecture du fichier .csv 
col_names=['App','Category','Rating','Reviews','Size','Installs','Type','Price','Content Rating','Genres','Last Updated','Current Ver','Android Ver'] 
df_google_ap_1 = pd.read_csv('db/googleplaystore_1.csv', on_bad_lines='skip', delimiter = ";")


 
### je groupe les catégories et les place dans un tableau
df2 = df_google_ap_1.groupby(['Category'], as_index=True)
group_cat = []
for cat in df2.groups.keys():
    group_cat.append([cat, 0])

### Idem pour les genres
df3 = df_google_ap_1.groupby(['Genres'], as_index=True)
group_genres = []
for gen in df3.groups.keys():
    group_genres.append([gen, 0])

### tableau des applications de plus d'un milliard
tab_milliard = []

print(group_genres)
for i in range (len(df_google_ap_1.index)):
    new_install = df_google_ap_1['Installs'].iloc[i].replace('+', '').replace(',', '').replace('3.6M', '3600000').replace('Varies with device', '0')

    category = df_google_ap_1['Category'].iloc[i]
    for j in range (0, len(group_cat)):
        if group_cat[j][0] == category:
            nb_install = group_cat[j][1]
            nb_install = nb_install + int(new_install)
            group_cat[j][1] = nb_install
            
    genre = df_google_ap_1['Genres'].iloc[i]
    for k in range (0, len(group_genres)):
        if group_genres[k][0] == genre:
            nb_genre = group_genres[k][1]
            nb_genre = nb_genre + int(new_install)
            group_genres[k][1] = nb_genre
    
    if int(new_install) >= 1000000000:
        tab_milliard.append([df_google_ap_1['App'].iloc[i], df_google_ap_1['Category'].iloc[i], int(new_install)])


print("\n" + B + "### 1. Liste des données CSV" + W)
print(df_google_ap_1)
print("\n")

print("\n" + B + "### 2. Liste total des catégories supérieur ou égal à 1 millard" + W)
for k in range(0, len(group_cat)):
    if group_cat[k][1] >= 1000000000:
        print(O + str(group_cat[k][0]) + " : " + W + str(group_cat[k][1]) + " installations")
print("\n")

print( B + "### 2. Liste total des genres supérieur ou égal à 1 millard" + W)
for k in range(0, len(group_genres)):
    if group_genres[k][1] >= 1000000000:
        print(O + str(group_genres[k][0]) + " : " + W + str(group_genres[k][1]) + " installations")
print("\n")

print(B + "### 2. Liste des apllications avec plus d'un milliard d'installation" + W)
print(pd.DataFrame(tab_milliard))
print("\n")

print(B + "### 3. Le plus grand nombre de Reviews" + W)
print(df_google_ap_1.loc[df_google_ap_1['Reviews'].idxmax()][["App", "Rating", "Reviews"]])
print("\n")

print(B + "### 4. Afficher les colonnes 2,5,6 et les lignes 3 à 16 du Dataframe" + W)
print(df_google_ap_1.iloc[2:15, [1, 4, 5]])
print("\n")

print(B + "### 5. Applications ouvertes aux personnes de tous âges" + W)
print(df_google_ap_1.loc[df_google_ap_1["Content Rating"].isin(["Everyone", " Everyone", "Everyone "])])
print("\n")

print(B + "### 6. Catégorie avec le plus d’applications" + W)
print(df_google_ap_1.groupby(['Category']).count().sort_values(by='App', ascending=False).iloc[0:1, [0]])
print("\n")

new_price = ['', 0]
for i in range (len(df_google_ap_1.index)):
    price_replace = df_google_ap_1["Price"].iloc[i].replace('Free', '0').replace('$', '')
    if float(price_replace) > new_price[1]:
        new_price[0] = df_google_ap_1["App"].iloc[i]
        new_price[1] = float(price_replace)


print(B + "### 7. Application vendue la plus chère" + W)
print(new_price)
print("\n")


