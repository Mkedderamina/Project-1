#Pandas with M1 biochimie mkedder Amina ,Mkedderamina/Project-1
#for biochimie Master 1 Tlemcen ...09/12/2025
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

# Affichage 
print("Tableau des séquences ADN :")
print(df, "\n\n") 

# 1) Sélectionner la colonne "Longueur"
Longueur = df["Longueur"]
print(longueur,"\n\n")

# 2) Filtrer les séquences dont la longueur supérieure à 10
print("**************** Filtrage dont la longueur ****************")
# Filtrer les séquences dont la longueur supérieure à 10
filtred_df = df[df["Longueur"] > 10]
print(filtered_df,"\n\n")

# 3) calculer la moyenne du pourcentage de GC
print("**************** Calcul de la moyenne ****************")
# Calculer la moyenne du pourcentage de GC
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%","\n\n")

# 4) Ajouter une nouvelle colonne avec des calculs 
print("**************** Ajoute d'une nouvelle colonne ****************")
# Ajouter une nouvelle collone "Catégorie GC"
df["Catégorie_GC"] = df["Pourcentage_GC"].apply(lambda x: "Riche" if x > 55 else "Moyen" if 45 < x <55 else  "Faible")

# 5) Ajouter une colonne comptant les 'G'
df["Nombre de G"] = df["Séquence"].str.count("G")
print("===== Nombre de G ajoutés =====")
print(df,"\n\n")

# 6) Calculer l'écart type de pourcentage GC et de longueur
écarttype_gc = df["Pourcentage GC"].std()
écarttype_long = df["longueur"].std()
print("===== Écart type =====")
print("Écart type de pourcentage GC:", écarttype_gc)
print("Écart type de longueur:", écarttype_long)
print(df,"\n\n")

# 7) Sauvegarde et chargement des données avec pandas 
#Sauvegarder le DataFrame dans un facteur csv 
df.to csv("tableau séquence.csv , index=false)
