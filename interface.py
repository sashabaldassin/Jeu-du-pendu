import random
from tkinter import *
from tkinter import ttk
import pygame
from main import *
from PIL import Image, ImageTk	#module pour lire les images

#_______________________________________________________________________________________Affichage_graphique_____________________________________________________________________________________
def afficher(msg) :
	global fenetre
	label = Label(fenetre, text=msg,bg='#000000', fg='white',font=("Courrier",8))
	label.pack()
	
def afficher_gros(msg) :
	global fenetre
	label = Label(fenetre, text=msg,bg='#000000' ,fg='white',font=("Courrier",15))		#Fonctions pour afficher du texte en différentes polices
	label.pack()

def afficher_perdu(msg) :
	global fenetre
	label = Label(fenetre, text=msg,bg='#000000' ,fg='white',font=("Courrier",35))		
	label.pack(side=BOTTOM)

def afficher_pendu(msg):
	global fenetre
	label = Label(fenetre, text=msg,bg='#000000', fg='white',font=("Courrier",30))
	label.pack(side=TOP)

#_____________________________________________________________________________La_partie__________________________________________________________________________________________________________________________________________________________________

def imagependu(mot_myst) :
#Cette fonction permet d'afficher les images du pendu
	global mot_couv
	global nbr_err
	global nbr_err_max
	if mot_myst==mot_couv :
		image = Image.open("cup.png") 
		nvlle_image = image.resize((int(image.width/4), int(image.height/4)))	# redimensionne l'image d'origine	
	elif nbr_err<=nbr_err_max :	
		image = Image.open("pendu"+str(nbr_err)+".png") 	# ouvre le fichier image du pendu correspondant au nombre d'erreurs
		nvlle_image = image.resize((int(image.width/8), int(image.height/8)))
	else :
		image = Image.open("fantome.png") 
		nvlle_image = image.resize((int(image.width/6), int(image.height/6)))
	
	photo = ImageTk.PhotoImage(nvlle_image)		
	image_pendu = Label(fenetre, image=photo)	
	image_pendu.image = photo
	image_pendu.pack()
	x = (fenetre.winfo_width() - photo.width()) // 2		# dimensions pour placer la photo dans la fenêtre
	y = (fenetre.winfo_height() - photo.height()) // 3		
	image_pendu.place(x=x, y=y)					# place l'image dans la fenêtre	

def boutons_lettre(deja_dit):
#Cette fonction crée les boutons pour jouer en fonction de ceux déjà cliqués précédemment
	global fenetre
	global nbr_err
	global mot_myst
	global nbr_err_max
	nbr_err_max=9
	Lettres_bouton = [0]*26 			#crée liste de 26 éléments
	bouton_cadre = Frame(fenetre, bg='black') 	#ajoute un cadre pour les boutons
	for i in range(26):
		if chr(i+65) not in deja_dit : 		#Vérification pour ne pas créer un bouton déjà appuyé
			Lettres_bouton[i] = Button(bouton_cadre,text=chr(i+65),command=lambda lettre=i+65: part_humain_tkinter(mot_myst,chr(lettre), "-"),height=3,width=2,bg='#F3F2F2',fg='black', font="bold") 	#crée les boutons portant le nom de chaque lettre
			Lettres_bouton[i].pack(side=LEFT, expand=YES)
		else :
			Lettres_bouton[i] = Button(bouton_cadre,text=chr(i+65),height=3,width=2, bg='#737373', fg='#ffffff') 
			Lettres_bouton[i].pack(side=LEFT, expand=YES)	#grise et rend inutilisable les boutons déjà utilisés
	bouton_cadre.pack(side='bottom', fill='x')
	if nbr_err>0 :
		imagependu(mot_myst)

def part_humain_tkinter(mot_myst, proposition, car_subst="-"):
#Cette fonction rassemble toutes les données et permet d'effectuer une partie de pendu en mode graphique
	global nbr_err
	global mot
	global deja_dit
	global lettres
	global lmot_decouv
	global deja_dit
	global mot_couv
	global nbr_err_max
	deja_dit.append(proposition)
	if proposition in mot_myst :
		decouvrir_lettre(proposition, mot_myst, lmot_decouv) 	
		mot_couv=''
		for i in lmot_decouv :
			mot_couv=mot_couv + i
		detruire()
		afficher_pendu(mot_couv) 	#réinitialise l'interface avec le nouveau mot partiellement découvert 
		boutons_lettre(deja_dit) 	#appel de la fonction qui créé les boutons lettres
	
		if mot_couv==mot_myst :
			detruire()
			afficher_pendu(mot_myst)
			afficher_pendu("Bravo! Vous avez gagné! \n")
			imagependu(mot_myst)
			retour_menu()

	elif (proposition not in mot_myst) and (nbr_err<nbr_err_max) : #si le joueur commet une erreur
		mot_couv=''
		for i in lmot_decouv :
			mot_couv=mot_couv + i
		nbr_err +=1
		detruire()
		afficher_pendu(mot_couv) 		#réaffiche le même mot partiellement découvert
		boutons_lettre(deja_dit)
		imagependu(mot_myst)
		
	elif nbr_err>=nbr_err_max :	#si le joueur a perdu
		detruire()
		nbr_err +=1      
		afficher_pendu("Perdu! Le mot était : "+ mot_myst)
		imagependu(mot_myst)
		retour_menu()


def corps_du_jeu():
#Cette fonction crée et initialise tous les paramètres graphiques et les options de partie humain
    detruire()
    global mot_myst
    global nbr_err
    global mot
    global lettres		#utilisation de variables globales car les valeurs sont modifiées mais on souhaite les
    global lmot_decouv		#conserver tout en changeant de fonction
    global deja_dit
    deja_dit=[]			#stocke les lettres déjà cliquées pour griser les boutons
    nbr_err=0
    liste_mots=importer_mots("fichiermots.txt") 
    mot_myst=choisir_mot_alea(liste_mots)
    lmot_decouv=initialiser_mot_part_decouv(mot_myst, '-') 
    mot_couv=''
    for i in lmot_decouv :
        mot_couv=mot_couv + i
    afficher_pendu(mot_couv)
    labe = Label(fenetre, text="Cliquez sur une lettre : ",bg='#000000', fg='white',font=("Courrier",18))
    labe.pack(side=TOP)
    boutons_lettre(deja_dit)	#Création 26 boutons

#__________________________________________________________________________________Menu____________________________________________________________________________________________________________________________________________________________________

def play():
#Cette fonction lance la musique
	pygame.mixer.music.load("pendu.wav")	#charge la musique
	pygame.mixer.music.play(loops=1000)	#fait tourner 1000 fois la musique chargée

def stop():
#Cette fonction arrête la musique
	pygame.mixer.music.stop()

def detruire():
#Cette fonction permet de détruire chaque élément présent dans l'interface
	global fenetre
	for widget in fenetre.winfo_children():  #boucle for qui parcourt tous les éléments présents de la fenêtre
		widget.destroy()
		
def retour_menu():
#Cette fonction crée un bouton pour retourner au menu
	global fenetre
	retourmenu= Button(fenetre, text="Retourner au menu",bg='white', fg='#000000', command=menu,height=2, width=18) 
	retourmenu.pack(pady=1, side=BOTTOM)			
			
def regles():
#Cette fonction affiche les règles du jeu et permet de revenir au menu
	detruire()
	global fenetre
	label = Label(fenetre, text="\n\nVous devez trouver un mot, chaque tiret correspond à une lettre, la première et la dernière sont affichées.\n",bg='#000000' ,fg="White",font=("Courrier",20))
	label.pack()
	label = Label(fenetre, text="Vous cliquez sur une lettre \n\n",bg='#000000' ,fg='#ECF000',font=("Courrier",20))	#utilisation d'un label pour changer de couleur
	label.pack()
	afficher_gros("- Si la lettre fait partie du mot, elle est affichée à la place du ou des tiret(s) correspondant(s). ")
	afficher_gros("- Sinon le pendu commence à s'afficher\n\n")
	label = Label(fenetre, text="Le jeu continue ainsi; vous proposez des lettres jusqu’à arriver à l'une des deux situations suivantes : \n ",bg='#000000' ,fg='#ECF000',font=("Courrier",20))
	label.pack()		
	afficher_gros("- Vous avez trouvé toutes les lettres du mot, vous avez gagné.")
	afficher_gros("- Le pendu est entièrement affiché, vous avez perdu! \n\n")
	label = Label(fenetre, text="Vous avez droit à 10 erreurs. \n",bg='#000000' ,fg='#ECF000',font=("Courrier",20))
	label.pack()	
	retour_menu()
	

def music():
#Cette fonction lance ou stop la musique selon le choix de l'utilisateur
	global fenetre
	detruire()
	label = Label(fenetre, text="Musique : ",bg='#000000' ,fg='#ECF000',font=("Courrier",20,"bold")) #argument "bold" sert à écrire en gras
	label.pack()
	on= Button(fenetre, text="ON",bg='white', fg='#000000',font=("bold"),command=play,height=2,width=30, relief = RAISED) #raised fait ressortir les boutons
	on.pack(pady=1) 	#Lance la musique
	off = Button(fenetre, text="OFF",bg='white', fg='#000000', font=("bold"),command=stop,height=2,width=20, relief= RAISED)  
	off.pack(pady=1) 	#éteint la musique
	retour_menu()
	
	
def menu():
#Fonction qui définit le menu principal. Elle est appelée à chaque fin de jeu

	detruire()
	global fenetre
	afficher("\n\n\n\n\n\n\n\n\n\n\n")
	lab = Label(fenetre, text="Bienvenue dans le jeu du pendu",bg='#000000', fg='white',font=("Courrier",40,"bold"))
	lab.pack()
	afficher("\n\n\n\n\n\n\n\n\n")
	labe = Label(fenetre, text="Cliquez sur un bouton",bg='#000000', fg='white',font=("Courrier",15))
	labe.pack(side=TOP)
	jeu1 = Button(fenetre, text="Lancer une partie",bg='white', fg='#000000',font=("bold"),command=corps_du_jeu,height=2,width=30, relief = RAISED)  #Lance le jeu
	jeu1.pack(pady=1)
	jeu2 = Button(fenetre, text="Lire les règles",bg='white', fg='#000000', font=("bold"),command=regles,height=2,width=20, relief= RAISED)   #appel de la fonction règles
	jeu2.pack(pady=1)
	jeu4 = Button(fenetre, text="Musique",bg='white', fg='#000000', font=("bold"),command=music,height=2,width=20, relief= RAISED)   #appel de la fonction musique
	jeu4.pack(pady=1)
	jeu3 = Button(fenetre, text="Quitter",bg='white', fg='#000000', font=("bold"),command=fenetre.destroy, height=2, width=15, relief= RAISED) #détruit la fenêtre de tkinter
	jeu3.pack(pady=1)
	

def creer_fenetre():
#Cette fonction crée tous les paramètres pour la fenêtre de l'interface et lance le menu

	global fenetre
	fenetre = Tk()				#lance fenêtre tkinter
	fenetre.title("Le pendu")		#nom de la fenêtre
	fenetre.attributes('-fullscreen', True)	#dimension de la fenêtre en plein écran
	fenetre.config(background='#000000')	#configuration de la fenêtre
	menu() 					#Lance l'interface du menu
	pygame.mixer.init()		 	#initalise la musique
	play() 					#lance automatiquement la musique
	fenetre.mainloop() 			#garde la fenêtre ouverte
		
	
