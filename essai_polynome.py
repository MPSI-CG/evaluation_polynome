################################################
####				            ####
####   Fonctions d'evaluation de polynome   ####
####					    ####
################################################

#Methode 1 : calcul de gauche a droite systematique

def resoudre_polynome1(list_coef, x):
	somme = 0

	for i in range(len(list_coef)):
		puissance_x = 1

		for j in range(i):
			puissance_x *= x

		somme += (list_coef[i] * puissance_x)
	
	return somme

#Methode 2 : stocker les valeur des puissances de k dans un tableau de longueur n

def resoudre_polynome2(list_coef, x):
	list_puissance_x = [1]
	somme = 0

	for i in range(1, len(list_coef)):
		list_puissance_x.append(list_puissance_x[i-1] * x)

	for i in range(len(list_coef)):
		somme += (list_coef[i] * list_puissance_x[i])

	return somme

#Methode 3 : utilisation d'un compteur pour les puissance de x

def resoudre_polynome3(list_coef, x):
	somme = 0
	puissance_x = 1

	for i in range(len(list_coef)):
		somme += (list_coef[i] * puissance_x)
		puissance_x *= x

	return somme

# Methode 4 : Algorithme de Horner
# Si vous trouvez une methode plus elegante n'hesitez pas a modifier !

def resoudre_polynome4(list_coef, x):
	somme = list_coef[len(list_coef)-1]
	
	for i in range(len(list_coef)-2, -1, -1):
		somme = somme * x + list_coef[i]

	return somme

 # Bonus

def factorielle(n):
        if n == 0:
                return 1
        return n * factorielle(n-1)

def generer_coef_polynome(n):
        list_coef = []

        for i in range(n+1):
                list_coef.append((factorielle(n)/(factorielle(i)*factorielle(n-i))))

        return list_coef
 
def resoudre_polynome(methode, list_coef, x):
        if methode == 1:
                return resoudre_polynome1(list_coef, x)
        if methode == 2:
                return resoudre_polynome1(list_coef, x)
        if methode == 3:
                return resoudre_polynome1(list_coef, x)
        if methode == 4:
                return resoudre_polynome1(list_coef, x)
 
        return -1
 
def calculer_polynome():
        print 'Entrer le degre du polynome a resoudre : '
        degre_polynome = input()
 
        print 'Entrer la valeur de l\'inconnue x minimale : '
        x_min = input()
 
        print 'Entrer la valeur de l\'inconnue x maximale : '
        x_max = input()
         
        print 'Entrer le numero de l\'algorithme de resolution : '
        methode = input()
 
        if degre_polynome < 100 and x_min < x_max and x_max < 100 and methode > 0 and methode < 5:
                for x in range(x_min, x_max+1):
                        print 'Pour x = ' + str(x) + " : " + str(resoudre_polynome(methode, generer_coef_polynome(degre_polynome), x))

