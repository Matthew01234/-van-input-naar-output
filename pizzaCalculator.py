#Matthew Penhoat's Pizza calculator

pizzaklein= 5
pizzanormaal= 9
pizzagroot= 13

print('Welkom bij Matthew Pizzas, Hier kunt u bestellen!')

Hoeveelheidklein = int(input('Hoeveel kleine pizzas wilt u?: ' ))
Hoeveelheidnormaal = int(input('Hoeveel normale pizzas wilt u?: ' ))
Hoeveelheidgroot = int(input('Hoeveel grote pizzas wilt u?: ' ))

prijsklein = Hoeveelheidklein * pizzaklein
prijsnormaal = Hoeveelheidnormaal * pizzanormaal
prijsgroot = Hoeveelheidgroot * pizzagroot
prijstotaal = prijsklein + prijsnormaal + prijsgroot

print ('Bestel Bon')
print ('-----------------------------------------')
print ('Kleine pizza: €' + str(prijsklein))
print ('Normale pizza: €'  + str(prijsnormaal))
print ('Grote pizza: €' + str(prijsgroot))
print ('Totaalprijs: €' + str(prijstotaal))
print ('Bedankt voor uw bestelling!')
print ('-----------------------------------------')