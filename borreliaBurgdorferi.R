#setwd("C:/Users/Emma/OneDrive/Desktop/LDD1/S2/demarche_scientifique")
#PARTIE 1: Gallus (Taux GC)
#PLTdata=read.table("nouv_tgc.txt", sep = "\t", header = TRUE)
#plot(PLTdata$TailleChromosome, PLTdata$TauxGC, xlab = "Taille du chromosome", ylab = "Taux GC", main = "Taux de GC en fonction de la taille du chromosome")
#lines(PLTdata$TailleChromosome, PLTdata$TauxGC)

#PARTIE 2: Borrelia burgdorferi (Biais GC)
#premier essai de creation de graphe: 

dataBB=read.table("BBSortieSkew.txt",sep="\t",header=TRUE)

#plot(dataBB$Pb, dataBB$TxGC.Skewed, type = "l", xlab = "Paires de base", ylab = "Biais GC", main = "Biais de GC en fonction de la position dans le génome")
#lines

#image avec erreur:
#plot(dataBB$Pb, dataBB$TxGC.Skewed, xlab = "Paires de base", ylab = "Biais GC", main = "Biais de GC en fonction de la position GC")
#lines(dataBB$Pb, dataBB$TxGC.Skewed)

#apres modifiation d'erreur effet de bord: l'oriC
BBdata2=read.table("BBSortieSkew.txt", sep = "\t", header = TRUE)
plot(BBdata2$Pb, BBdata2$TxGC.Skewed, type = "l", xlab = "Paires de base", ylab = "Biais GC", main = "Biais de GC en fonction de la position")

#ajout de ligne pour mieux voir 
abline(h=0, col="red", lty=2)
#note: lty= type de ligne. 2 pour tirets, 3 pour points etc.

#resreg<-lm(PLTdata$TailleChromosome, PLTdata$TauxGC, data=PLTdata)

#calculs supplementaires
avOric = mean(BBdata2[1:20,2])
apOric = mean(BBdata2[23:41,2])

#Zone approximative de l'OriC: entre 23e et 24e colonne (440-460 kPb)
BBsauts <- diff(BBdata2[,2])
which.max(abs(BBsauts))
