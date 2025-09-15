from faker import Faker	#module de génération de mots
fake = Faker('fr_FR')		#argument pour choisir la langue des mots (ici c'est français)
with open('fichiermots.txt','w') as f :	#ouvre le fichier souhaité pour écrire dedans
	for i in range(10000):	
		mot = fake.word()	
		f.write(mot + '\n')	#à chaque itération écrit le mot dans le fichier suivi d'un retour à la ligne
