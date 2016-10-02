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
