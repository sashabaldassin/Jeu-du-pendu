import random
import main
#___________________________________________________________________________Partie_auto________________________________________________________________________________________________________________________________________________


def fabrique_liste_alphabet() :
#Cette fonction renvoie la liste des lettres majuscules dans l'odre alphabétique.

	liste_alphabet=[]
	for i in range(65,91,1) : 			#A=65 et Z=90 en code ASCII
		liste_alphabet.append(chr(i)) 		#boucle permettant d'ajouter les lettres de A à Z dans la liste.
	return liste_alphabet


def fabrique_liste_alea() :
#Cette fonction renvoie une liste contenant les lettres majucules mélangées.

	liste=fabrique_liste_alphabet()
	random.shuffle(liste) 		#fonction shuffle du module random qui mélange la liste par effet de bord
	return liste
	
	
def dico_frequence(nom_fichier) :
#Cette fonction renvoie un dictionnaire contenant les lettres présentes dans un fichier (clé) et leur fréquence d'apparition (valeur).
	
	dic_freq_lettre={}	
	f=open(nom_fichier)
	liste = main.importer_mots(nom_fichier)
	for mot in liste : 						#première boucle pour obtenir chaque mot
		indice=0
		for indice in range(len(mot)): 				#Deuxième boucle permettant d'obtenir les indices des mots
			if mot[indice] not in dic_freq_lettre : 	#condition pour voir si la lettre a déjà été trouvée.
				dic_freq_lettre[mot[indice]] = 1 	#Si c'est ce n'est pas le cas, on ajoute la clé.
			else :
				dic_freq_lettre[mot[indice]] = dic_freq_lettre[mot[indice]] +1 	#Sinon on rajoute 1 à la valeur de la clé
	f.close()
	return dic_freq_lettre


def lettre_la_plus_frequente(dico) :
#Cette fonction renvoie la lettre la plus fréquente d'un dictionnaire.

	max=None								
	for cle in dico :
		if max is None or dico[cle]>max :		#condition pour identifier une lettre ayant une valeur supérieure à max
			max = dico[cle]				#max prend la valeur de la clé la plus fréquente
			lettre = cle				#lettre est la clé associée à la valeur max
	return lettre
	
	
def fabrique_liste_freq(nom_fichier) :
#Cette fonction renvoie une liste ordonnée selon la fréquence d'apparition des lettres dans un fichier.

	liste_freq=[]
	dic = dico_frequence(nom_fichier)			#renvoie toutes les lettres dans un dictionnaire et leur fréquence.
	while len(dic)>0 :
		lettre = lettre_la_plus_frequente(dic)		#ajoute dans une liste la lettre la plus fréquente à chaque itération.
		liste_freq.append(lettre)
		del dic[lettre]					#supprime la lettre la plus fréquente afin de trouver la suivante.
	return liste_freq
		
		



