from statistics import variance


tab1 = [15, 6, 9, 5, 27]
tab2 = [1, 2, 3, 4, 5, 8]



def moyenne (tab1, tab2):
    total_moy = 0
    N = 0
    for i in range (0, len(tab1)):
        moy = tab1[i] * tab2[i]
        total_moy += moy  
        N += tab1[i]    
    x = total_moy / N
    print (x)
    return x

moy = float(moyenne(tab1, tab2))

def variance(moy):
    N = 0
    v = 0
    _x = moy
    for j in range(0, len(tab1)):
        v += tab2[j]*((tab1[j] - _x)*2)
        N += tab1[j] 
    variance = v / N
    return variance

var = variance(moy)

def ecart_type (value):
    ecart = value**(0.5)
    return ecart

def mediane (tab):
    tab.sort()
    x = 0
    if len(tab) % 2 == 0:
        n= len(tab) / 2
        n1 =  n + 1
        x = (tab[int(n)] + tab[int(n1)]) / 2
    else :
        n= (len(tab)+1) / 2
        x = tab[int(n)]
    return x
    

print("La moyenne est " + str(moy.__round__(2)))
print("La variance est " + str(var.__round__(2)))
print("L'écart type est " + str(ecart_type(var)))
print("La médiane est " + str(mediane(tab1)))