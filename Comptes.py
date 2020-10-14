"""
Saisie de deux comptes bancaires : compte chèques et livret A
À compléter avec les exceptions ;-)

Éditeur : Laurent REYNAUD
Date : 14-10-2020
"""

import pickle


class CompteBancaire:

    def __init__(self, date, libelle, montant):
        self.date = date
        self.libelle = libelle
        self.montant = montant

    """ Getters """
    def get_date(self):
        return self.date

    def get_libelle(self):
        return self.libelle

    def get_montant(self):
        return self.montant


"""Intanciation de la classe CompteBancaire et déclaration des valeurs des deux comptes bancaires en les convertissant
sous la forme d'un dictionnaire afin de conserver les données saisies"""
CompteCheque = CompteBancaire('01-01-20', 'Ouverture du compte chèque', 0.00)
OperationsCC = {'Compte chèque :': '123',
                'Date :': [CompteCheque.get_date()],
                'Libellé :': [CompteCheque.get_libelle()],
                'Montant :': [CompteCheque.get_montant()]}
LivretA = CompteBancaire('01-01-20', 'Ouverture du livret A', 0.00)
OperationsLA = {'Livret A :': '456',
                'Date :': [LivretA.get_date()],
                'Libellé :': [LivretA.get_libelle()],
                'Montant :': [LivretA.get_montant()]}

"""Sérialisation"""
file = open('C:/Users/LRCOM/PycharmProjects/ComptesBancaires/MesComptes.txt', 'rb')
OperationsCC = pickle.load(file)
OperationsLA = pickle.load(file)
file.close()

"""Menu général"""
option = 0
while option != 8:
    print('-'*15, 'MENU GENERAL', '-'*15)
    print('1- Saisie des opérations sur le compte chèque')
    print("2- Suppression d'operations sur le compte chèque")
    print('3- Saisie des opérations sur le livret A')
    print("4- Suppression d'opérations sur le livret A")
    print('5- Virement de compte à compte')
    print('6- Édition des opérations saisies')
    print('7- Sauvegarde des données')
    print('8- Sortie du programme')
    try:
        option = int(input('Quelle option ? '))
        if option < 1 or option > 8:
            print('Le chiffre doit être compris entre 1 et 8... tu sais compter ?')
            print()
    except ValueError:
        print("Demande de saisie d'un chiffre...")
        print()

    """Saisie des opérations sur le compte chèque"""
    if option == 1:
        choix = 'o'
        while choix == 'o' or choix == 'O':
            date_operation = input('Date : ')
            OperationsCC['Date :'].append(date_operation)
            libelle_operation = input('Libellé : ')
            OperationsCC['Libellé :'].append(libelle_operation)
            try:
                montant_operation = float(input('Montant : '))
                OperationsCC['Montant :'].append(montant_operation)
            except ValueError:
                print('Demande de saisie de chiffres...')
                OperationsCC['Montant :'].append(0.00)
            choix = input('Nouvelle saisie (o/n) ? ')
        print()

    """Suppression d'opérations sur le compte chèque"""
    if option == 2:
        choix = 'o'
        while choix == 'o' or choix == 'O':
            try:
                date_suppression = input('Date à supprimer : ')
                OperationsCC['Date :'].remove(date_suppression)
                libelle_suppression = input('Libellé à supprimer : ')
                OperationsCC['Libellé :'].remove(libelle_suppression)
                montant_suppression = float(input('Montant à supprimer : '))
                OperationsCC['Montant :'].remove(montant_suppression)
            except ValueError:
                print('Erreur de saisie')
            choix = input('Nouvelle suppression (o/n) ? ')
        print()

    """Saisie des opérations sur le livret A"""
    if option == 3:
        choix = 'o'
        while choix == 'o' or choix == 'O':
            date_operation = input('Date : ')
            OperationsLA['Date :'].append(date_operation)
            libelle_operation = input('Libellé : ')
            OperationsLA['Libellé :'].append(libelle_operation)
            montant_operation = float(input('Montant : '))
            OperationsLA['Montant :'].append(montant_operation)
            try:
                montant_operation = float(input('Montant : '))
                OperationsLA['Montant :'].append(montant_operation)
            except ValueError:
                print('Demande de saisie de chiffres...')
                OperationsLA['Montant :'].append(0.00)
            choix = input('Nouvelle saisie (o/n) ? ')
        print()

    """Suppression d'opérations sur le livret A"""
    if option == 4:
        choix = 'o'
        while choix == 'o' or choix == 'O':
            try:
                date_suppression = input('Date à supprimer : ')
                OperationsLA['Date :'].remove(date_suppression)
                libelle_suppression = input('Libellé à supprimer : ')
                OperationsLA['Libellé :'].remove(libelle_suppression)
                montant_suppression = float(input('Montant à supprimer : '))
                OperationsLA['Montant : '].remove(montant_suppression)
            except ValueError:
                print('Erreur de saisie')
            choix = input('Nouvelle suppression (o/n) ? ')
        print()

    """Virement de compte à compte"""
    if option == 5:
        date_operation = input('Date : ')
        OperationsCC['Date :'].append(date_operation)
        OperationsLA['Date :'].append(date_operation)
        libelle_operation = input('Libellé : ')
        OperationsCC['Libellé :'].append(libelle_operation)
        OperationsLA['Libellé :'].append(libelle_operation)
        compteDebite = input('Compte à débiter (CC/LA) : ')
        if compteDebite == 'cc' or compteDebite == 'CC':
            try:
                montant_operation = float(input('Montant : '))
                OperationsCC['Montant :'].append(- montant_operation)
                OperationsLA['Montant :'].append(montant_operation)
            except ValueError:
                print('Erreur de saisie')
        elif compteDebite == 'la' or compteDebite == 'LA':
            try:
                montant_operation = float(input('Montant : '))
                OperationsCC['Montant :'].append(montant_operation)
                OperationsLA['Montant :'].append(-montant_operation)
            except ValueError:
                print('Erreur de saisie')
        print()

    """Édition des opérations saisies"""
    if option == 6:
        option = input('Quel compte à éditer (CC/LA) ? ')
        if option == 'cc' or option == 'CC':
            for k, v in OperationsCC.items():
                print(k, v)
            cumulCC = sum(OperationsCC['Montant :'])
            print('Le solde du compte chèque :', round(cumulCC, 2), '€')
            print()
        elif option == 'la' or option == 'LA':
            for k, v in OperationsLA.items():
                print(k, v)
            cumulLA = sum(OperationsLA['Montant :'])
            print('Le solde du livret A :', round(cumulLA, 2), '€')
            print()
        else:
            print('Erreur de saisie')
            print()

    """Sauvegarde des données"""
    if option == 7:
        file = open('C:/Users/LRCOM/PycharmProjects/ComptesBancaires/MesComptes.txt', 'wb')
        pickle.dump(OperationsCC, file)
        pickle.dump(OperationsLA, file)
        file.close()
        print('Sauvegarde effectuée !')
        print()

    """Sortie du programme"""
    if option == 8:
        print('Au revoir et à la prochaine !')
        exit()
