from models.players import Players
from models.tournaments import Tournament
from views.menus import Menus
from models.database import Datatiny
from models.rounds import Round, Match

from datetime import datetime
from operator import itemgetter


class Control_players():
    """
    Une classe pour créer et gérer les joueurs dans la base.
    """
    def __init__(self):
        self.menu = Menus()
        self.data = Datatiny

    def create_player(self):
        """Méthode de la classe Control_players pour demander les informations et créer des joueurs de la classe Players.
        :return: un objet player de la classe Players.
        """
        infos_player = self.menu.create_player()
        player = Players(*infos_player)
        return player

    def check_players(self):
        """Méthode de la classe Control_players pour lister les joueurs dans la base all_players et
        de proposer le choix du joueur a importé.
        :return: un chiffre int
        """
        print("------- Liste des joueurs dans la base -------")
        if len(self.data.all_players) == 0:
            print("Pas de joueurs dans la base")
            return None
        for player in self.data.all_players:
            print("Joueur numéro {id}: {first_name} {last_name} - classement {ranking}.".format(**player))
        doc_ids = len(self.data.all_players) + 1
        while True:
            try:
                number = int(input("------- Rentrer le numéro du joueur -------\n"))
                if number not in list(range(doc_ids)):
                    print("Mauvais numéro de joueur !")
                else:
                    return number
            except ValueError:
                print("Attention il faut un chiffre !")

    def list_players(self):
        """Méthode de la classe Control_players pour créer ou importer les joueurs dans un tournoi.
        :return: une liste d'objet joueurs.
        """
        # list_players = Players.auto_players()
        list_players = []
        for i in range(8):
            choice_create_player = self.menu.choice_create_player()
            if choice_create_player == 1:
                while True:
                    infos_player = self.create_player()
                    if self.data.check_player(infos_player) is False:
                        list_players.append(infos_player)
                        break
            elif choice_create_player == 2:
                choice_player = self.data.import_player(self.check_players())
                list_players.append(choice_player)
        return list_players


class Control_tournament():
    """Une classe pour créer et gérer les tournois dans la base.
    """
    def __init__(self):
        self.menu = Menus()
        self.round = Round()
        self.match = Match()
        self.ct = Tournament()
        self.data = Datatiny()

    def create_tournament(self):
        """Méthode de la classe Control_tournament pour demander les informations et créer les tournois de la class Tournament.
        :return: un objet tournament de la classe Tournament.
        """
        list_create_tournement = self.menu.create_tournament()
        # tournament = Tournament("Master Chess 10000", "Rome", "24/04", "Quick", "Tournoi de Rome")
        tournament = Tournament(*list_create_tournement)
        print(tournament, "\n")
        return tournament

    def round1(self, list_players):
        """Méthode de la classe Control_tournament pour gérer le round 1.
        Args:
            list_players (Liste): liste des joueurs.
        Returns:
            [objet class Round]: start_round qui est le premier round du tournoi.
        """
        now = datetime.now()
        start_round = Round("Round 1", str(now.strftime("%Y-%m-%d %H:%M:%S")))
        round1 = start_round.round1(list_players)
        start_round.list_match_paired = round1
        self.match.list_match = start_round.list_match
        self.match.results(round1)
        now = datetime.now()
        start_round.end_date = str(now.strftime("%Y-%m-%d %H:%M:%S"))
        return start_round

    def more_round(self, round1):
        """Méthode de la classe Control_tournament pour le déroulement de chaque round jusqu à la fin du tournoi.
        Args:
            round1 (objet class Round): le premier tour du tournoi.
        """
        list_rounds = [round1]
        for i in range(self.ct.rounds - 1):
            print("\n------- ROUND ", (i + 2), "-------\n")
            now = datetime.now()
            round = Round("Round " + str(i + 2), str(now.strftime("%Y-%m-%d %H:%M:%S")))
            round.list_match = self.match.list_scores_sorted
            match_paired = round.next_round()
            self.menu.choice_round()
            self.data.insert_report(list_rounds)
            choice_round = self.menu.check_int("Choisissez une action : --> ")
            if choice_round == 1:
                self.menu.display_round(round.list_match_paired)
                self.menu.ranking_list((self.match.results(match_paired)))
                # self.menu.display(self.match.results(match_paired))
                now = datetime.now()
                round.end_date = str(now.strftime("%Y-%m-%d %H:%M:%S"))
                list_rounds.append(round)
                self.data.insert_report(list_rounds)
            if choice_round == 2:
                self.data.push_data(list_rounds, round)
                break
            if choice_round == 3:
                self.data.push_data(list_rounds, round)
                self.data_report()
                break

    def resume_tournament(self):
        """Méthode de la classe Control_tournament pour reprendre un tournoi en cours.
        Permet le déroulement de chaque round jusqu à la fin du tournoi. Il est possible
        d'arreter le tournoi entre chaque round et d'afficher les rapports.
        """
        print("------- Reprise du tournoi -------\n")
        list_datas = self.data.pull_data()
        try:
            list_rounds, list_player_score = list_datas
        except TypeError:
            return
        nb_remain_round = self.ct.rounds - (len(list_rounds))
        self.menu.display("******* Il reste " + str(nb_remain_round) + " rounds *******")
        self.menu.ranking_list(list_player_score)
        nb_next_round = self.ct.rounds - nb_remain_round
        for i in range(1, nb_remain_round + 1):
            print("\n------- ROUND ", (i + nb_next_round), "-------\n")
            now = datetime.now()
            round = Round("Round " + str(i + nb_next_round), now.strftime("%Y-%m-%d %H:%M:%S"))
            if i == 0:
                round.list_match = list_player_score
            else:
                round.list_match = self.match.list_scores_sorted
            macth_paired = round.next_round()
            self.menu.choice_round()
            choice_round = self.menu.check_int("Choisissez une action : --> ")
            if choice_round == 1:
                self.menu.display_round(round.list_match_paired)
                self.menu.ranking_list(self.match.results(macth_paired))
                round.end_date = now.strftime("%Y-%m-%d %H:%M:%S")
                list_rounds.append(round)
                self.data.insert_report(list_rounds)
            if choice_round == 2:
                self.data.push_data(list_rounds, round)
                break
            if choice_round == 3:
                self.data.push_data(list_rounds, round)
                self.menu.data_report()
                break

    def data_report(self):
        """Méthode de la classe Control_tournament pour gérer les rapports et proposer le choix
        à l'utilisateur.
        """
        while True:
            all_players = self.data.all_players
            infos_tournement = self.data.infos_tournement
            self.menu.data_report()
            choice_menu_report = self.menu.check_report("------- Votre choix : ")
            if choice_menu_report == 1:
                list_players = sorted(all_players.all(), key=itemgetter('last_name'))
                for player in list_players:
                    self.menu.display_report_player(player)
            if choice_menu_report == 2:
                players = all_players.all()
                list_players = sorted(players, key=itemgetter('ranking'), reverse=True)
                for player in list_players:
                    self.menu.display_report_player(player)
            if choice_menu_report == 3:
                tournament = infos_tournement.all()
                for i in range(len(tournament)):
                    self.menu.display("------- Tournoi " + tournament[i]['name'] + "-------")
                    list_players = sorted(tournament[i]['list_players'], key=itemgetter('last_name'))
                    for player in list_players:
                        self.menu.display_report_player(player)
            if choice_menu_report == 4:
                tournament = infos_tournement.all()
                for i in range(len(tournament)):
                    self.menu.display("------- Tournoi " + tournament[i]['name'] + "-------")
                    list_players = sorted(tournament[i]['list_players'], key=itemgetter('ranking'), reverse=True)
                    for player in list_players:
                        self.menu.display_report_player(player)
            if choice_menu_report == 5:
                tournament = infos_tournement.all()
                for i in range(len(tournament)):
                    self.menu.display_report_tournament(tournament[i])
            if choice_menu_report == 6:
                tournament = infos_tournement.all()
                for i in range(len(tournament)):
                    self.menu.display("------- Tournoi " + tournament[i]['name'] + "-------")
                    list_rounds = tournament[i]['list_rounds']
                    for round in list_rounds:
                        self.menu.display_report_round(round)
            if choice_menu_report == 7:
                tournament = infos_tournement.all()
                for i in range(len(tournament)):
                    self.menu.display("------- Tournoi " + tournament[i]['name'] + "-------")
                    list_match = tournament[i]['list_matchs']
                    for match in list_match:
                        self.menu.display(match)
            if choice_menu_report == 8:
                break
