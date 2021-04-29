from pprint import pprint


class Menus():
    """Une classe pour créer les affichages et gérer les menus du programme.
    """

    def __init__(self):
        pass

    @staticmethod
    def start():
        """Méthode de la classe Menus pour affichier le menu général
        """
        print("Bienvenue dans le logiciel de gestion Centre échecs :\n")
        print("1: Ajouter un joueur à la base")
        print("2: Créer un tournoi")
        print("3: Reprendre le tournoi en cours")
        print("4: Changer le classement d'un joueur")
        print("5: Afficher un rapport")
        print("6: Sauvegarder et Quitter\n")

    @staticmethod
    def user_choice(message):
        """Méthode de la classe Menus pour demander un chiffre à l'utilisateur et vérifier le type int.
        :Args:
            le texte du message.
        :return: un chiffre int.
        """
        try:
            choice = int(input(message))
            if choice not in [1, 2, 3, 4, 5, 6]:
                print("Choisir un nb entre 1 et 6")
                return Menus.user_choice(message)
            return choice
        except ValueError:
            print("Attention ce n'est pas un chiffre ")
            return Menus.user_choice(message)

    @staticmethod
    def change_player():
        """Méthode de la classe Menus pour demander le prénom et nom du joueur que on va changer le classement.
        :return: une liste.
        """
        first_name = Menus.check("1: Entrer le prénom du joueur\n")
        last_name = Menus.check("1: Entrer le nom de famille du joueur\n")
        return [first_name, last_name]

    @staticmethod
    def check(message):
        """Méthode de la classe Menus pour demander une saisie à l'utilisateur et vérifier le type str.
        :Args:
            le texte du message.
        :return: une str.
        """
        try:
            return str(input(message))
        except Exception:
            print("Oups info incorrect!")
            return Menus.check(message)

    @staticmethod
    def check_float(message):
        """Méthode de la classe Menus pour demander un chiffre et vérifier le type float.
        :Args:
            le texte du message.
        :return: un chiffre float.
        """
        while True:
            try:
                number = float(input(message))
                if number == 0 or number == 0.5 or number == 1:
                    return number
                else:
                    print("Attention il faut un score de 0, 0.5 ou 1 !")
            except ValueError:
                print("Attention il faut un score de 0, 0.5 ou 1 !")

    @staticmethod
    def check_int(message):
        """Méthode de la classe Menus pour demander un chiffre à l'utilisateur et vérifier le type int.
        :Args:
            le texte du message.
        :return: un chiffre int.
        """
        while True:
            try:
                number = int(input(message))
                if number < 1 or number > 3:
                    print("Attention il faut un chiffre entre 1 et 3 !")
                else:
                    return number
            except ValueError:
                print("Attention il faut un chiffre !")

    @staticmethod
    def check_report(message):
        """Méthode de la classe Menus pour demander un chiffre à l'utilisateur et vérifier le type int.
        :Args:
            le texte du message.
        :return: un chiffre int.
        """
        while True:
            try:
                number = int(input(message))
                if number < 1 or number > 8:
                    print("Attention il faut un chiffre entre 1 et 8 !")
                else:
                    return number
            except ValueError:
                print("Attention il faut un chiffre !")

    @staticmethod
    def create_player():
        """Méthode de la classe Menus pour demander une saisie à l'utilisateur et vérifier les types str ou int.
        :return: une liste.
        """
        print("------- Création d'un joueur -------\n")
        first_name = Menus.check("1: Entrer le prenom du joueur\n")
        last_name = Menus.check("2: Entrer le nom du joueur\n")
        date_of_birth = Menus.check("3: Entrer la date d'anniversaire du joueur au format JJ/MM/AA\n")
        sex = Menus.check("4: Entrer le sexe du joueur M ou F\n")
        ranking = int(Menus.check("5: Entrer le classement du joueur (un chiffre)\n"))
        return first_name, last_name, date_of_birth, sex, ranking

    @staticmethod
    def choice_create_player():
        """Méthode de la classe Menus pour demander une saisie à l'utilisateur pour choisir de créer ou importer
        un joueur dans un tournoi.
        :return: un chiffre int.
        """
        print("------- Création de la liste des joueurs du tournoi -------")
        print("Voulez-vous créer un joueur -> 1\nImporter un joueur -> 2")
        while True:
            try:
                number = int(input("Votre choix: "))
                if number == 1 or number == 2:
                    return number
                else:
                    print("Attention il faut un chiffre 1 ou 2 !")
            except ValueError:
                print("Attention il faut un chiffre !")

    @staticmethod
    def choice_round():
        """Méthode de la classe Menus pour le menu entre chaque round du tournoi.
        """
        print("1: Continuer le tournoi")
        print("2: Stopper le tournoi et retour au menu général")
        print("3: Afficher le rapport du tournoi en cours\n")

    @staticmethod
    def create_tournament():
        """Méthode de la classe Menus pour demander une saisie à l'utilisateur pour créer un tournoi.
        :return: une liste.
        """
        print("------- Création d'un Tournoi -------\n")
        tournament_name = Menus.check("1: Entrer le nom du tournoi\n")
        tournament_location = Menus.check("2: Entrer la location du tournoi\n")
        tournament_date = Menus.check("3: Entrer la date du tournoi au format JJ/MM/AA\n")
        tournament_time_control = Menus.check("4: Entrer le time_control du tournoi, Blitz, Bullet ou Quick\n")
        tournament_description = Menus.check("5: Entrer la description du tournoi\n")
        return tournament_name, tournament_location, tournament_date, tournament_time_control, tournament_description

    @staticmethod
    def data_report():
        """Méthode pour afficher les choix des rapports.
        """
        print("------- Rapport sur les joueurs -------")
        print("1: Liste de tous les joueurs par ordre alphabétique")
        print("2: Liste de tous les joueurs par classement")
        print("3: Liste de tous les joueurs par tournoi et ordre alphabétique")
        print("4: Liste de tous les joueurs par tournoi et classement\n")
        print("------- Rapport sur les tournois -------")
        print("5: Liste de tous les tournois ")
        print("6: Liste de toutes les rounds par tournoi ")
        print("7: Liste de tous les matchs par tournoi\n")
        print("8: Retour au menu général")

    @staticmethod
    def display(message):
        """Méthode de la classe Menus pour afficher un message.
        :Args:
            le texte du message.
        """
        print()
        pprint(message)

    @staticmethod
    def display_report_player(message):
        """Méthode de la classe Menus pour afficher le rapport des joueurs.
        :Args:
            le texte du message.
        """
        print("{first_name} {last_name} - classement {ranking} - Id N°{id}".format(**message))
        print()

    @staticmethod
    def display_report_round(message):
        """Méthode de la classe Menus pour afficher le rapport des rounds des tournois.
        :Args:
            le texte du message.
        """
        print("{name} - {start_date} - {end_date}".format(**message))
        print()

    @staticmethod
    def display_report_tournament(message):
        """Méthode de la classe Menus pour afficher le rapport des tournois.
        :Args:
            le texte du message.
        """
        print("Le tournoi {name} a {location} de type {time_control} le {date}".format(**message))
        print()

    @staticmethod
    def display_round(list_match_paired):
        """Méthode de la classe Menus pour afficher la liste des matchs dans un tournoi.
        :Args:
            la liste des matchs.
        """
        print("Liste des prochains matchs : \n")
        print(list_match_paired[0][0], "  VS  ", list_match_paired[0][1])
        print(list_match_paired[1][0], "  VS  ", list_match_paired[1][1])
        print(list_match_paired[2][0], "  VS  ", list_match_paired[2][1])
        print(list_match_paired[3][0], "  VS  ", list_match_paired[3][1], "\n")

    # @staticmethod
    # def final_result(list_scores_sorted):
    #     print("******* Le vainqueur du tournoi *******")
    #     print(list_scores_sorted[0][0], "\n")

    @staticmethod
    def ranking_list(message):
        """Méthode de la classe Menus pour afficher le classement par points des joeuurs
        entre chaque round d'un tournois.
        :Args:
            le texte du message.
        """
        print("\n------- Liste des joueurs par points:")
        pprint(message)
        print()
