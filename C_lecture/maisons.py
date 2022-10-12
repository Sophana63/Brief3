import random

def create_house ():
    num_house = []
    price_house = []
    for i in range (0, 58):
        num_house.append([i])
        price_house.append([random.randint(125000, 700000)])
    return num_house, price_house

print(create_house()[1])

#### Combien de maisons ont un prix supérieur ou égal à 300 0000 euros ? 
nb = 0
nb2 = 0
nb3 = 0
nb4 = 0
for i in range (0, len(create_house()[1])) :
    prix = create_house()[1]    
    if prix[i][0] >= 300000:
        nb = nb + 1
    if 250000 <= prix[i][0] <= 400000:
        nb2 = nb2 + 1
    if prix[i][0] <= 600000:
        nb3 = nb3 + 1
    if prix[i][0] < 150000 or prix[i][0] > 650000:
        nb4 = nb4 + 1

print("Nombre de maison supérieur ou égal à 300000 euros : " + str(nb) + "/58\n")
print("Nombre de maison compris entre 250000 et 400000 euros : " + str(nb2) + "/58\n")
print("Nombre de maison n'étant pas supérieur à 600000 euros : " + str(nb3) + "/58\n")
print("Nombre de maison inférieur à 150000€ et supérieur à 650000 euros : " + str(nb4) + "/58\n")


    
