W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

ventes_commerciaux = {"Marie":15, "Samuel":17,  "Gaston":12, "Fred":10, "Mae":5, "Julie":15, "Zoe":7, "Claire":20, "Chloe":8, "Julien":14, "Gael":9, "Samia":15, "Omar":11, "Gabriel":16, "Manon": 2}

print("\n" + B + "### 1. Dictionnaire nommé ventes_commerciaux" + W)
print(ventes_commerciaux)
print("\n")

moyenne = sum(ventes_commerciaux.values()) / float(len(ventes_commerciaux))

print(B + "### 2. Moyenne des ventes" + W)
print("Moyenne : " + str(moyenne))
print("\n")

print(B + "### 3. Total des ventes" + W)
print("Total : " + str(sum(ventes_commerciaux.values())))
print("\n")

print(B + "### 4. Liste des commerciaux avec un nombre de ventes strictement supérieur à la moyenne" + W)
print([k for k, v in ventes_commerciaux.items() if v > moyenne])
print("\n")

print(B + "### 5. Meilleur vendeur" + W)
print(max(ventes_commerciaux, key=ventes_commerciaux.get))
print("\n")

print(B + "### 6.  Prénom  avec strictement moins de 4 lettres" + W)
for name, vente in ventes_commerciaux.items():    
    if len(name) < 4:
        print (name)
print("\n")

print(B + "### 7.  Prénom des vendeurs qui ont un nombre de ventes pairs" + W)
for name, vente in ventes_commerciaux.items():    
    if (vente % 2) == 0:
        print (name, vente)
print("\n")