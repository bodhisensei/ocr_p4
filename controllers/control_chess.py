from views.menus import Menus
from controllers.control_menus import Control_players
from controllers.control_menus import Control_tournament
from models.database import Datatiny


class Control_menu():
    """Une classe pour gérer le menu de base et le lancement d'un tournoi
    """

    def __init__(self):
        self.menu = Menus()
        self.cp = Control_players()
        self.ct = Control_tournament()
        self.data = Datatiny()

    def tournament_round(self, list_players):
        """Méthode de la classe Control_menu pour lancer le round 1 et le déroulement du tournoi.
        """
        print("------- ROUND 1 -------\n")
        round1 = self.ct.round1(list_players)
        self.ct.more_round(round1)

    def control_choice(self):
        """Méthode de la classe Control_menu pour gérer le choix de l'utilisateur dans le menu de base.
        """
        while True:
            self.menu.start()
            choice = self.menu.user_choice("------- Votre choix : ")
            if choice == 1:
                create_player = self.cp.create_player()
                self.menu.display(create_player)
                self.data.insert_player(create_player)
            if choice == 2:
                create_tournament = self.ct.create_tournament()
                list_players = self.cp.list_players()
                self.data.insert_data(list_players, create_tournament)
                self.tournament_round(list_players)
            if choice == 3:
                self.ct.resume_tournament()
            if choice == 4:
                player = self.menu.change_player()
                self.data.change_ranking(player)
            if choice == 5:
                self.ct.data_report()
            if choice == 6:
                exit()
