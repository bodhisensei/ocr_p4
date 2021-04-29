from tinydb import TinyDB, Query
from tinydb.operations import set
from models.players import Players
from models.rounds import Round


class Datatiny:
    """Une classe pour générer les différents tables dans tinyddb et le fichier de stockage
    db.json
    """
    db = TinyDB('db.json', indent=4)
    all_players = db.table('all_players')
    players_tournement = db.table('players_tournement')
    infos_tournement = db.table('infos_tournement')
    match_table = db.table('match_score')
    round_table = db.table('round')
    match_paired = db.table('match_paired')

    def __init__(self):
        pass

    def deserialize_player(self, dict_player):
        """Méthode pour déserialiser un dictionnaire Player en objet Player
        """
        player = Players(dict_player['first_name'], dict_player['last_name'], dict_player['date_of_birth'],
                         dict_player['sexe'], dict_player['ranking'], dict_player['id'])
        player.tag_players = dict_player['tag_players']
        return player

    def deserialize_round(self, dict_round):
        """Méthode pour déserialiser un dictionnaire Round en objet Round
        """
        round = Round(dict_round['name'], dict_round['start_date'], dict_round['end_date'])
        return round

    @staticmethod
    def deserial_player(dict_player):
        """Méthode pour exporter et déserialiser un dictionnaire Player en objet Player
        """
        player = Players(dict_player['first_name'], dict_player['last_name'], dict_player['date_of_birth'],
                         dict_player['sexe'], dict_player['ranking'], dict_player['id'])
        player.tag_players = dict_player['tag_players']
        return player

    @staticmethod
    def check_player(player):
        """Méthode qui permet de tester si le joueur est déjà dans la base de données.
        """
        User = Query()
        search_player = (Datatiny.all_players.search((User.first_name == player.first_name)
                         & (User.last_name == player.last_name)))
        if bool(search_player) is True:
            print("******* Joueur déjà existant ! *******\n")
            return True
        else:
            return False

    @staticmethod
    def import_player(number):
        """Méthode pour importer un joueur de la base avec son N°Id.
        """
        all_players = Datatiny.all_players
        serialized_player = all_players.get(doc_id=number)
        player = Datatiny.deserial_player(serialized_player)
        print("Joueur importé")
        return player

    def insert_player(self, player):
        """Méthode qui permet d'enregister et sérialisés les joueurs dans la base de données.
        """
        User = Query()
        doc_ids = len(Datatiny.all_players) + 1
        player.id = doc_ids
        serial_player = player.serialize_player()
        search_player = Datatiny.all_players.search((User.first_name == player.first_name) & (User.last_name == player.last_name))
        if bool(search_player) is False:
            Datatiny.all_players.insert(serial_player)
            print("******* Ajout du joueur dans la base *******\n")
        else:
            print("******* Joueur déjà existant ! *******\n")

    def change_ranking(self, player):
        """Méthode pour chercher et changer le classement un joueur dans la base de données.
        """
        try:
            search_player = Datatiny.all_players.search(Query().fragment({'first_name': player[0], 'last_name': player[1]}))
            if search_player == []:
                print("\nPas de joueur trouvé\n")
            else:
                print("Joueur trouvé: ", search_player, "\n")
                player_id = int(input("Entrer l'id du joueur trouvé: "))
                ranking = int(input("Entrer le nouveau classement du joueur: "))
                Datatiny.all_players.update(set("ranking", ranking), doc_ids=[player_id])
                new_player = Datatiny.all_players.search(Query().fragment({'first_name': player[0], 'last_name': player[1]}))
                print("\nNouveau classement : ", new_player, "\n")
        except NameError:
            print("Pas de joueur trouvé")

    def insert_data(self, list_players, tournament):
        """Méthode pour insérer les joueurs et les infos du tournoi dans la base de données.
        """
        # Netoyage de la base players_tournement
        Datatiny.players_tournement.truncate()
        User = Query()
        for player in list_players:
            search_player = Datatiny.all_players.search((User.first_name == player.first_name) & (User.last_name == player.last_name))
            if bool(search_player) is False:
                doc_ids = len(Datatiny.all_players.all()) + 1
                player.id = doc_ids
                new_serial_player = player.serialize_player()
                Datatiny.all_players.insert(new_serial_player)
                Datatiny.players_tournement.insert(new_serial_player)
            else:
                serial_player = player.serialize_player()
                Datatiny.players_tournement.insert(serial_player)
        serial_infos_tournement = tournament.serialize_tournament()
        Datatiny.infos_tournement.insert(serial_infos_tournement)

    def insert_report(self, list_rounds):
        """Méthode pour insérer les rounds et les matchs du tournoi dans la base de données.
        """
        list_dic_round = []
        list_dic_match = []
        list_dic_player = Datatiny.players_tournement.all()
        for round in list_rounds:
            dic_round = {"name": round.name, "start_date": round.start_date, "end_date": round.end_date}
            list_dic_round.append(dic_round)

            for match in round.list_match_paired:
                dic_player1_match = match[0][0].serialize_player()
                dic_player2_match = match[1][0].serialize_player()
                dic_match = {"player1": dic_player1_match, "player1_score": match[0][1],
                             "player2": dic_player2_match, "player2_score": match[1][1]}
                list_dic_match.append(dic_match)
        id_tournement = len(Datatiny.infos_tournement.all())
        Datatiny.infos_tournement.update({'list_players': list_dic_player, 'list_rounds': list_dic_round,
                                          'list_matchs': list_dic_match}, doc_ids=[id_tournement])

    def push_data(self, list_rounds, round):
        """Permet de rentrer les données des joueurs avec leurs scores, les rounds ainsi que les matchs
        d'un tournoi afin de le reprendre par la suite.
        """
        list_dic_player_score = []
        list_dic_round = []
        list_dic_match = []
        for player_score in round.list_player_scored:
            dic_player_match = player_score[0].serialize_player()
            dic_player_score = {"player": dic_player_match, "player_score": player_score[1]}
            list_dic_player_score.append(dic_player_score)
        Datatiny.match_table.insert({"player_scored": list_dic_player_score})
        for round in list_rounds:
            dic_round = {"name": round.name, "start_date": round.start_date,
                         "end_date": round.end_date}
            list_dic_round.append(dic_round)
            for match in round.list_match_paired:
                dic_player1_match = match[0][0].serialize_player()
                dic_player2_match = match[1][0].serialize_player()
                dic_match = {"player1": dic_player1_match, "player1_score": match[0][1],
                             "player2": dic_player2_match, "player2_score": match[1][1]}
                list_dic_match.append(dic_match)
        Datatiny.round_table.insert({'round': list_dic_round})
        Datatiny.match_paired.insert({'list_match_paired': list_dic_match})

    def pull_data(self):
        """ Permet de récuperer les données de la base pour continuer le tournoi en cours.
        :return: une liste avec une liste des rounds et une liste des joueurs avec leurs scores.
        """
        list_player_score = []
        list_rounds = []
        list_match_paired = []
        dic_player_score = Datatiny.match_table.all()
        try:
            dic_players_score = dic_player_score[0]['player_scored']
        except IndexError:
            print("Oups ! Pas de tournoi en cours...\n")
            return
        for dict_player in dic_players_score:
            list_player_score.append([self.deserialize_player(dict_player['player']), dict_player["player_score"]])
        dic_round = Datatiny.round_table.all()
        dic_round_description = dic_round[0]['round']
        for dict_round in dic_round_description:
            round = self.deserialize_round(dict_round)
            list_rounds.append(round)
        dic_match = Datatiny.match_paired.all()
        dic_match_paired = dic_match[0]['list_match_paired']
        for match in dic_match_paired:
            list_match_paired.append(([self.deserialize_player(match['player1']),
                                      match['player1_score']],
                                     [self.deserialize_player(match['player2']),
                                      match['player2_score']]))
        list_rounds[-1].list_match_paired = list_match_paired
        Datatiny.match_table.truncate()
        Datatiny.round_table.truncate()
        Datatiny.match_paired.truncate()
        list_datas = [list_rounds, list_player_score]
        return list_datas
