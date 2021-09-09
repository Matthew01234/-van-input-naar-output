#Feest luch kosten

hoeveelheidcrossant = int(input('Hoeveel crossants wilt u: '))
hoeveelheidstokbrood = int(input('Hoeveel stokbrooden wilt u: '))
hoeveelheidkortingsbonnen = int(input('Hoeveel kortingsbonnen heeft u: '))

print ('Bestel lijst')
crossant = hoeveelheidcrossant * 0.39
stokbrood = hoeveelheidstokbrood * 2.78
Kortingsbon = hoeveelheidkortingsbonnen * 0.50
prijs= (crossant + stokbrood) - Kortingsbon 



if prijs> 0:
    print ('De feestlunch kost je bij de bakker ' + str(prijs) +' euro voor de '+ str(hoeveelheidcrossant) + ' croissantjes en de ' + str(hoeveelheidstokbrood) + ' stokbroden als de ' + str(hoeveelheidkortingsbonnen) + ' kortingsbonnen nog geldig zijn!')

    