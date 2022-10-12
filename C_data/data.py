import pandas as pd

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

# chargement du fichier ERP
file_name = "db/erp.xlsx"
df_erp = pd.read_excel(file_name)

# chargement du fichier WEB
df_web = pd.read_excel("db/web.xlsx")

# Je renomme le fichier WEB, la colonne "sku" en "id_web"
# Ca me permettra de joindre le fichier WEB et LIAISON
# afin d'avoir le même nom de colonne
df_web.rename(columns = {"sku":"id_web"}, inplace=True)

# Je supprime tous les champs vides de la colonne "id_web"
df_web = df_web.dropna(subset=['id_web'])

# chargement du fichier LIAISON
df_liaison = pd.read_excel("db/liaison.xlsx")

# Liaison entre les fichiers ERP et LIAISON
liaison = pd.merge(df_erp, df_liaison, on="product_id", how="inner")

# Liaison entre les fichiers LIAISON et WEB
erp_web = pd.merge(liaison, df_web, on="id_web", how="inner")

# Affiche les données liées
print("\n" + B + "### Centralisation des données" + W)
print(erp_web)

# Tri les données: je récupère que les données avec "product" en post_type
list_price = erp_web[erp_web["post_type"] == "product"][["product_id", "price", "total_sales"]]

# Je réinitialise l'index de mon dataframe trié et lié
list_price = list_price.reset_index(drop=True)

# Je récupère les colonnes des prix et le nombre de vente
# Je boucle pour récupérer le chiffre d'affaire
tab_ca = []
ca_total = 0
for l in range (len(list_price.index)):
    montant_total = list_price["price"].iloc[l] * list_price["total_sales"].iloc[l]
    tab_ca.append([list_price["product_id"].iloc[l], montant_total, list_price["price"].iloc[l]])
    ca_total += montant_total

print("\n" + B + "### Chiffre d'affaire " + W)
print(str(ca_total) + "euros")

# Fonction permettant de ressortir la moyenne et l'écart type
def z_score (tab):
    total_moy = 0
    moyenne = 0 
    moy = 0   
    for j in range (0, len(tab)):
        price = tab[j][2] 
        total_moy += price
    moyenne = total_moy / len(tab) 

    variance = 0
    for i in range (0, len(tab)):
        variance += (tab[i][2] - moyenne)**2

    variance = variance / len(tab)
    ecart_type = variance**(0.5)
    return moyenne, ecart_type


print("\n" + B + "### Moyenne et Ecart Type " + W)
print(z_score(tab_ca)[0], z_score(tab_ca)[1])

# Déclaration des variables pour le graphique
nb = 0
nb2 = 0
tab_x = []
tab_y = []
tab_Zx = []
tab_Zy = []
# Je boucle pour trouver le Z Score pour chaque prix
for i in range (0, len(tab_ca)):    
    
    Z = (tab_ca[i][2] - z_score(tab_ca)[0]) / z_score(tab_ca)[1]   
    
### Si le ZScore est au dessus de 2, je l'ajoute dans un tableau Z-Score 
### Il permettra d'afficher le graphique avec 2 couleurs différentes
    if Z > 2 :
        nb += 1
        tab_Zy.append(i)
        tab_Zx.append(tab_ca[i][2])        
    else:
        tab_y.append(i)
        tab_x.append(tab_ca[i][2])
print(nb, nb2)

### Partie graphique: nuage de points
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
 
_x= tab_x
_y= tab_y

_Zx = tab_Zx
_Zy = tab_Zy
 
# Creation du graphique avec un 2ème y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Création des points 
fig.add_trace(
    go.Scatter(x=_x, y=_y, name="Prix", mode="markers"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=_Zx, y=_Zy, name="Z Score > 2", mode="markers"),
    secondary_y=True,
)

# Titre
fig.update_layout(
    title_text="Analyse et l’identification des outliers"
)

# x-axis titre
fig.update_xaxes(title_text="Nuage de points")

# y-axes titre
fig.update_yaxes(title_text="<b>Prix</b> des produits", secondary_y=False)
fig.update_yaxes(title_text="<b>Index</b> des produits", secondary_y=True)

fig.show() 