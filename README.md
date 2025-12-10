#Pandas with Mkedder Amina 
#For Biochimie Master 1 Tlemcen ...09/12/2025
#The project members : 
#Mdjahed Anfel
#Tadj mereim 
#Azzouz amina 


import pandas as pd 

# Données : Séquence ADN , longueur, Pourcentage de GC 
data = {
  "Séquence" : ["ATGCGTACGTA" , "GCTAGCTAGGCC" , "ATGCGCGTAAGT" , "TACGATCGTA" , "ATGAAAGGCCT" , "CGTACGTAGC" , "TTAACCGGAT"]
  "Longueur" : [12,12,12,10,11,10,10]
  "Pourcentage_GC" :[50,66.67,58.33,40,45.45,50,60]
}

#  Créations du DataFrame 
df = pd.DataFrame(data)
print("*********Création et affichage *********")

# 1) Affichage 
print("Tableau des séquences ADN :")
print(df, "\n\n") 

# 2) Sélectionné la colonne "Longueur"
print(*********Opération*********)
Longueur = df ["Longueur"]
print(Longueur ,"\n\n")

# 3) Filtrer les séquences de longueur > 10
print(*********Filtrage supérieur à 10*********)
Filtered_df = df[df["Longueur"] >à 10] 
print(Filtered_df, "\n\n")
