#speelhaldag2 + input
hoeveelheidpersonen = int(input('Met hoeveel personen komt u?: '))
sessies = int(input('Hoeveel sessies van 5 minuten wilt u?: '))

toegangticket= 7.45
vipvr= sessies * 0.37
personen= hoeveelheidpersonen

prijs= (vipvr + toegangticket) * personen



if prijs> 0:
    print ('Dit geweldige dagje-uit met ' + str(personen) + ' personen in de Speelhal met 45 minuten VR kost je maar ' + str(prijs) + ' euro')


