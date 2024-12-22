def supprimer_doublons(fichier):
    with open(fichier, 'r', encoding='latin-1') as f:
        lignes = f.readlines()

    lignes_sans_doublons = list(dict.fromkeys(lignes))

    with open(fichier, 'w', encoding='latin-1') as f:
        f.writelines(lignes_sans_doublons)

fichier = 'list.txt'
supprimer_doublons(fichier)
