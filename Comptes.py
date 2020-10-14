"""
Instanciation de la classe CompteBancaire en un objet 'compte' : une classe étant un type d'objet comme un chiffre, une
séquence, un dictionnaire... pour pouvoir conserver les données déclarées de l'objet 'compte' celui-ci est converti
sous la forme d'un dictionnaire ayant pour clé une str (n° de compte) et pour valeur une liste (date, libellé et
montant)

Éditeur : Laurent REYNAUD
Date : 14-09-2020
"""


class CompteBancaire:

    def __init__(self, num_compte, date, libelle, montant):
        self.num_compte = num_compte
        self.date = date
        self.libelle = libelle
        self.montant = montant
        return


if __name__ == '__main__':
    mon_dico = {}
    while True:
        print("MENU GENERAL")
        print("1- Créer un compte")
        print("2- Afficher tous les comptes")
        print("3- Sortir")
        print()
        print("Votre choix ? ")
        choix_saisi = int(input())
        if choix_saisi == 1:
            print("Numéro de compte créé:")
            num_saisi = input()
            if mon_dico.keys().__contains__(num_saisi):
                print('Attention de compte existe déjà...')
            print("Date de création du compte:")
            date_saisi = input()
            print("Libellé de création du compte (AN):")
            libelle_saisi = input()
            print("Montant à l'ouverture du compte:")
            montant_saisi = float(input())
            compte = CompteBancaire(num_saisi, date_saisi, libelle_saisi, montant_saisi)
            mon_dico.update({num_saisi: [date_saisi, libelle_saisi, montant_saisi]})
            print()
        if choix_saisi == 2:
            if mon_dico == {}:
                print("Aucun compte n'est créé")
            else:
                mes_comptes = list(mon_dico.items())
                for i in mes_comptes:
                    print('Compte créé n°', i[0], 'le', i[1][0], "avec l'intitulé :", i[1][1], 'pour un montant de',
                          i[1][2], '€')
            print()
        if choix_saisi == 3:
            print("Merci et à la prochaine !")
            quit()
