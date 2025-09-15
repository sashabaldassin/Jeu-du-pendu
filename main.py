import random
import turtle		#module pour dessiner le pendu dans une autre fenêtre
from interface import * #fichier où se situe les fonctions de tkinter
from partieauto import * #fichier où se situe les fonctions de la partie auto

#___________________________________________________________________________________Partie_humain___________________________________________________________________________________________________________________


def importer_mots(nom_fichier) :
#Cette fonction renvoie une liste de mots contenus dans un fichier(en argument) et convertie tous les mots en majuscule, en supprimant les espaces.

    f=open(nom_fichier)
    l1=[]
    for ligne in f :
        a=True
        ligne = ligne.strip() 			#supprime tous les espaces
        for j in range(len(ligne)) :
        	if not ((ligne[j]>='A' and ligne[j]<='Z') or (ligne[j]>='a' and ligne[j]<='z')) :	#vérifie que le caractère est une lettre comprise entre a et z, majuscule ou minuscule
        	     a=False
        if a :
               ligne = ligne.upper() 		#transforme le mot en majuscule
               if len(ligne)>=3 :            
                    l1.append(ligne) 		#ajoute le mot à la liste
    f.close()
    return l1		#retourne la liste des mots de plus de 3 lettres en majuscule


def choisir_mot_alea(liste):
#Cette fonction renvoie un mot choisi aléatoirement dans une liste passée en argument.

    nombre = random.randint(0, (len(liste)-1)) 		#on fait un randint pour obtenir un entier aléatoire entre 0 et le dernier élément de la liste
    mot = liste[nombre]  				#le mot sera celui qui correspond à l'indice dans la liste
    return mot


def initialiser_mot_part_decouv(mot_myst, car_subst="-"):
#Cette fonction renvoie une liste qui affiche la première et dernière lettre du mot à découvrir et des tirets pour chaque lettre à trouver en début de partie.

	l1=[]
	nbr=len(mot_myst)-1
	for i in range(len(mot_myst)): 
		if i==0 or i==nbr :										
			l1.append(mot_myst[i])		#on ajoute la première et la dernière lettre du mot à découvrir dans la liste.
		else :
			l1.append(car_subst)		#on ajoute le caractère dans la liste entre la première et la dernière lettre.
	return l1


def afficher_potence_texte(nb_err, nb_err_max):
#Cette fonction affiche le mot "Perdu !" en fonction du nombre d'erreurs commises par l'utilisateur et du nombre d'erreur max. Elle comptabilise le nombre d'erreurs.

    perdu = "PERDU" + (nb_err_max)*"!" 				#on écrit le mot dans une chaîne de caractères pour obtenir la longueur et chaque indice
    print(perdu[0:nb_err]+(nb_err_max-nb_err)*"-"+"!") 		#on affiche selon le nombre d'erreurs pour réutiliser la fonction
    

def demander_proposition(deja_dit):
#Cette fonction demande une lettre à l'utilisateur et vérifie si celle-ci est bien une lettre et n'a pas déjà été dite. Elle la transforme ensuite en majuscule.
	
	lettre = input("Saisir une lettre : ")
	while ( not((lettre>='a' and lettre<='z') or(lettre>='A' and lettre<='Z'))) or ((lettre.upper()) in deja_dit) or len(lettre)>1 :  #on vérifie chaque condition grâce à la boucle while 
		if (lettre.upper()) in deja_dit:	 
			print("La lettre a déjà été dite")	 						
		lettre = input("Saisir une lettre : ")
	return lettre.upper() 					#on retourne la lettre en majuscule



def decouvrir_lettre (lettre, mot_myst, lmot_decouv):
#Cette fonction modifie la liste du mot partiellement découvert pour rajouter une lettre que l'utilisateur vient de trouver. Elle renvoie True si elle est modifiée.

    x=False
    if lettre in mot_myst :
        for i in range (1, len(lmot_decouv)-1):				#boucle for de l'indice 1 à longueur du mot-1 pour ne pas comptabiliser la première et la dernière lettre
            if lettre == mot_myst[i] and lmot_decouv[i]!=lettre: 	#on parcours les lettres du mot mystère pour savoir si la lettre entrée est dedans.
                lmot_decouv[i]= lettre 					#si c'est le cas, on remplace le tiret correspondant par la lettre
                x=True 										
    return x
    
    
    
def partie_humain(mot_myst, nb_err_max, car_subst="-",turtl=False):
#Cette fonction rassemble l'ensemble des fonctions précédentes pour permettre de jouer au pendu et de faire une partie entière;
	deja_dit=[] 		#on initialise une liste pour stocker toutes les lettres déjà entrées par le joueur
	pendu=[ " ", "\n\n\n\n\n\n\n_____","    \n  |  \n  |  \n  |  \n  |  \n  |  \n  |  \n__|___", " __________\n  |  \n  |  \n  |  \n  |  \n  |  \n  |  \n__|___"," __________\n  |      |\n  |      O\n  |  \n  |  \n  |  \n  |  \n__|___"," __________\n  |      |\n  |      O\n  |      |\n  |      |  \n  |  \n  |  \n__|___", " __________\n  |      |\n  |      O\n  |     /|\n  |      |  \n  |  \n  |  \n__|___"," __________\n  |      |\n  |      O\n  |     /|\ \n  |      |  \n  |  \n  |  \n__|___", " __________\n  |      |\n  |      O\n  |     /|\ \n  |      |\n  |     /  \n  |\n__|___"," __________\n  |      |\n  |      O\n  |     /|\ \n  |      |\n  |     / \ \n  |\n__|___"]
	nb_err=0 								#on initialise un compteur d'erreurs
	lmot_decouv=initialiser_mot_part_decouv(mot_myst, car_subst) 		#on montre la première et la dernière lettre du mot
	mot_couv=''
	for i in lmot_decouv :
		mot_couv=mot_couv + i
	print(mot_couv) 					#affiche la liste en format chaine de caractères
	while mot_couv!=mot_myst and nb_err<nb_err_max : 	#fait la boucle du jeu tant que le mot n'est pas découvert ou que le nombre d'erreurs max n'est pas atteint
		deja_dit_str=''
		if len(deja_dit)>0 :
			print("Les lettres déjà dites sont : ")
			taille=len(deja_dit)-1
			for i in range(len(deja_dit)):
				if i<taille :
					deja_dit_str = deja_dit_str + deja_dit[i] + '-'
				else :
					deja_dit_str = deja_dit_str + deja_dit[i]				
			print(deja_dit_str)
		print("\n")
		proposition = demander_proposition(deja_dit)			#demande une lettre au joueur
		deja_dit.append(proposition) 					#ajoute la lettre à la liste de celles déjà dites		
		if proposition in mot_myst : 					#vérifie si la lettre est dans le mot
			print("La lettre est présente.")
			decouvrir_lettre(proposition, mot_myst, lmot_decouv) 	#si oui, modifie le mot partiellement découvert pour rajouter la lettre
			mot_couv=''
			for i in lmot_decouv :
				mot_couv += i 					#transforme la liste du mot découvert en chaîne de caractère
			print("\nLe mot à découvrir est : ")
			print(mot_couv)						#affiche le mot partiellement découvert
			print("\n")
		else :
			nb_err+=1
			afficher_potence_texte(nb_err, nb_err_max) 		#sinon affiche le nombre d'erreurs
			if nb_err==1 :
				print("Vous avez fait une erreur\n")
			else :
				print("vous avez fait",nb_err,"erreurs\n")
			if turtl :
				turtle.title("Pendu")
				turtle.setup (startx=-2, starty=0) 		#place la fenêtre centrée à droite
				turtle.hideturtle()				#cache le marqueur
				if(nb_err==1):
					turtle.bk(100)
					turtle.fd(200)
				if(nb_err==2):
					turtle.bk(100)
					turtle.lt(90)
					turtle.fd(300)
				if(nb_err==3):
					turtle.rt(90)
					turtle.fd(150)
				if(nb_err==4):
					turtle.rt(90)
					turtle.fd(50)
					turtle.dot(50)
				if(nb_err==5):
					turtle.fd(100)
					turtle.bk(75)	   #Si l'option turtle est lancée, dessine le pendu dans une autre fenêtre en fonction du nombre d'erreurs
				if(nb_err==6):
					turtle.rt(45)
					turtle.fd(50)
					turtle.bk(50)
				if(nb_err==7):
					turtle.lt(90)
					turtle.fd(50)
					turtle.bk(50)
				if(nb_err==8):
					turtle.rt(45)
					turtle.fd(75)
					turtle.rt(45)
					turtle.fd(50)
					turtle.bk(50)
				if(nb_err==9):
					turtle.lt(90)
					turtle.fd(50)
			else :
				print(pendu[nb_err],"\n")


	if mot_couv==mot_myst :
		print("Bravo! Vous avez gagné! \n")
		if turtl and nb_err>0:
			turtle.bye()	#ferme la fenêtre turtle
		return True
	else :
		print("Perdu! Le mot était : "+ mot_myst +"\n")
		if turtl :
			turtle.bye()
		return False
    	
 		
    
def partie_humain_alea(nom_fichier, nb_err_max, car_subst="-",turtl=False):
#Cette fonction permet de jouer une partie entière de pendu à partir d'un fichier contenant des mots sur chaque lignes.

	liste_mots = importer_mots(nom_fichier) 				#trie la liste, en passant en majuscule
	mot_myst = choisir_mot_alea(liste_mots) 				#choisit un mot au hasard
	return(partie_humain(mot_myst, nb_err_max, car_subst="-",turtl=turtl)) 	#on lance la partie !

#______________________________________________________________________________________Partie_auto____________________________________________________________________________________________________

def partie_auto (mot_myst, liste_lettres, affichage = True, pause = False) :
#Cette fonction est le programme pour faire une partie automatique. Elle renvoie le nombre d'erreurs commises par l'ordinateur.

	nb_err = 0
	car_subst="-"
	lmot_decouv=initialiser_mot_part_decouv(mot_myst, car_subst) 
	mot_couv=''
	for i in lmot_decouv :				#initialise le mot partiellement découvert
		mot_couv=mot_couv + i 
	if affichage :
		print(mot_couv,"\n")                    #l'affiche si l'utilisateur souhaite avoir un affichage
		if pause == True :
			attente = input("Appuyez sur n'importe quelle touche pour continuer : \n")
		else :
			print("\n")
	proposition = 0
	while mot_couv!=mot_myst : 
		lettre = liste_lettres[proposition]
		if affichage :
			print(("La lettre choisie est "+ lettre+"!"))
		if lettre in mot_myst : 
			if affichage :
				print("La lettre est présente.")
			decouvrir_lettre(lettre, mot_myst, lmot_decouv)         #remplace la lettre trouvée dans le mot partiellement découvert
			mot_couv=''
			for i in lmot_decouv :
				mot_couv=mot_couv + i 
			if affichage :
				print(mot_couv) 
				if pause == True :
					attente = input("Appuyez sur n'importe quelle touche pour continuer : ")
		else :
			if affichage :
				print("Lettre incorrecte")
			nb_err+=1
		if affichage :
			print("\n") 	
		proposition+=1
		if affichage and mot_couv==mot_myst:	
			print("Bravo, le mot a été trouvé !")
			if nb_err==1 :
				print("1 seule erreur a été commise !\n")
			else :
				print((str(nb_err)+ " erreurs ont été commises !\n"))
	return nb_err
				
#__________________________________________________________________________________________Partie_terminal________________________________________________________________________________________________		

if __name__=="__main__":

						
	print("\nBienvenue dans le jeu du pendu !\n")
	graphisme = input("Souhaitez vous une interface graphique ? (oui/non) \n")
	while graphisme!='oui' and graphisme!='non' :
		graphisme=input("Choisissez une réponse correcte : ")
	if graphisme=='oui' :
		graphisme = True			#détermine si le joueur souhaite une interface graphique avec tkinter
	else :
		graphisme = False	
	
	if not graphisme :	
		num=0			#première affectation pour rentrer dans la boucle
		while num!=3 :
	
#__________________________________________________________________________________menu_principal_______________________________________________________________________________________________________

			num=0 		#deuxième affectation pour remettre à 0 lors d'un nouveau tour de boucle
			print("\n1. Lancer une partie")
			print("2. Lire les règles")
			print("3. Quitter")
			while num!=1 and num!=2 and num!=3:
				try :					#instruction qui vérifie que l'utilisateur a rentré un entier
					num = int(input("Choisissez un numéro : "))
				except :
					continue
			
#__________________________________________________________________________________lancer_la_partie______________________________________________________________________________________________________			
			if num==1:
				partie=0
				print("\n1. Vous contre l'ordinateur")
				print("2. Ordinateur contre lui-même")
				while partie!=1 and partie!=2 :
					try :
						partie = int(input("Choisissez un numéro : "))
					except :
						continue
			
#__________________________________________________________________________________partie_humain_____________________________________________________________________________________________________			
			
				if partie==1 :
					print("\nVotre partie va bientôt commencer... \n")
					turt=input("Souhaitez vous afficher un pendu dans une autre fenêtre ? (oui/non) \n")
					while turt!='oui' and turt!='non' :
						turt=input("Choisissez une réponse correcte : ")
					if turt=='oui' :
						turt = True	                #détermine si le joueur souhaite un affichage graphique du pendu avec turtle
					else :
						turt = False
					partie_humain_alea("fichiermots.txt", 9, car_subst="-", turtl=turt)
				
	#__________________________________________________________________________________Partie_auto_____________________________________________________________________________________________________			
				#_________________________________________________affichage_et_pause_________________________________________________________________
				elif partie==2 :					
					mot_myst=choisir_mot_alea(importer_mots("fichiermots.txt"))
					affichage= None
					while affichage!='oui' and affichage!='non' :
						affichage=input("\nSouhaitez-vous un affichage ? (oui/non) \n")
					if affichage=='oui':
						affichage=True
						pause=None
						while pause!='oui' and pause!='non' :
							pause=input("Souhaitez-vous faire des pauses ? (oui/non) \n")
						if pause=='oui':
							pause=True
						
					else :
						affichage=False
						pause=False
					
				#___________________________________________________stratégie_de_l'ordinateur_______________________________________________________________
					
				
					print("\nChoisissez la méthode utilisée par l'ordinateur :\n")
			
					print("1. Les lettres sont dites par ordre alphabétique ")
					print("2. Les lettres sont dites de façon aléatoire ")
					print("3. Les lettres sont dites par ordre décroissant de fréquence d'apparition ")	
					
					strat= 0
					while strat!=1 and strat!=2 and strat!=3 :
						try :
							strat= int(input("Choisissez un numéro : "))
						except :
							continue
					
					if strat==1 :
						liste=fabrique_liste_alphabet()
					elif strat==2 :
						liste=fabrique_liste_alea()			#Choisi la liste en fonction du choix de l'utilisateur
					else :
						liste=fabrique_liste_freq("fichiermots.txt")
					
					
				#____________________________________________________________la_partie_______________________________________________________________________	
				
					partie_auto (mot_myst, liste, affichage, pause) 	#Lance la partie selon tous les choix précédents
				
#_____________________________________________________________________________________________règles_______________________________________________________________________________________________________________				
				
			elif num==2 :
			#affiche les règles du jeu
				print("Vous devez trouver un mot, chaque tiret correspond à une lettre, la première et la dernière sont affichées. \n")
				print("Vous proposez une lettre : \n\n")
				print("- Si la lettre fait partie du mot, elle est affichée à la place du ou des tiret(s) correspondant(s). \n")
				print("- Sinon la première lettre de \"PERDU!!\" est affichée. \n")
				print("Le jeu continue ainsi; vous proposez des lettres jusqu’à arriver à l'une des deux situations suivantes : \n\n")
				print("- Vous avez trouvé toutes les lettres du mot, vous avez gagné.\n")
				print("- Le mot \"PERDU!!!!!\" est entièrement affiché, vous avez perdu. \n")
				print("Vous avez droit à 9 erreurs. \n")
			
		
		print("\nMerci, au revoir !\n")
			
	else :
		creer_fenetre()	#appelle une fonction du fichier interface qui lance tkinter

