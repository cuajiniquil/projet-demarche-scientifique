adenine = 0
guanine = 0
thymine = 0
cytosine = 0
inconnu = 0
autre = 0
taille = 0
txgc = 0
skew = 0 
idx = 0

pas = int(input("Donner la taille du pas: ")) #20000
fenetre = int(input("Donner la taille de la fenetre: ")) #10000

seq = ""

fchr1 = open("Borrelia_burgdorferi_B31.txt", "r") #r = read
fchr2 = open("BBSortieSkew.txt", "a") #a = append


fchr2.write(f"Pb \t TxGC Skewed \n")

fchr1.readline() #Lit la ligne de description pour qu'elle ne compte pas sur les calculs
for ligne in fchr1:
    seq = seq + ligne[:-1]  # Ajoute la ligne à la séquence traité (en enlevant \n)

    #Répéte boucle au long de la séquence traité 
    while idx + fenetre <= len(seq):
        #Commence avec une fenêtre initiale dans la séquence
        seqfn = seq[idx:idx + fenetre]

        #Compte les bases dans cette fenêtre
        for base in seqfn:
            if base in "aA":
                adenine += 1
            elif base in "gG":
                guanine += 1
            elif base in "tT":
                thymine += 1
            elif base in "cC":
                cytosine += 1
            elif base in "nN":
                inconnu += 1

        #Taille de la fenêtre (!= taille sequence)
        taille = adenine + guanine + thymine + cytosine

        #Calcul du taux de GC
        if taille > 0:
            txgc = (guanine + cytosine) / taille
        else:
        #Evite des eventuelles divisions par 0
            txgc = 0
        #Calcul du skew GC:
        skew = (guanine - cytosine)/(guanine + cytosine) 
            
        #Affiche les résultats de la fenêtre
        print(f"Fenêtre {idx + 1}-{idx + fenetre}: A={adenine}, G={guanine}, T={thymine}, C={cytosine}, N={inconnu}, Skew={skew}")

        #Ecrit les résultats dans le fichier
        fchr2.write(f"{idx + 1} \t {skew} \n")

        #Réinitialisation des compteurs
        adenine = 0
        guanine = 0
        thymine = 0
        cytosine = 0
        inconnu = 0

        #Met à jour l'index pour la prochaine fenêtre
        idx += pas

#A l'origine du probeleme de l'effet de bord:
        
#Ecrit la taille et le taux de GC à la fin
#fchr2.write(f"{taille}\t{txgc}\n")

# Fermer les fichiers
fchr1.close()
fchr2.close()

