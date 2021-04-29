from views.menus import Menus


class Round:
    """Une classe pour générer un round avec ces attributs.
    """

    def __init__(self, name="", start_date=None, end_date=None):

        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.list_match = []
        self.list_match_paired = []
        self.list_player_scored = []

    def __str__(self):
        return f"\n{self.name} - {self.start_date} - {self.end_date} - {self.list_match} - {self.list_match_paired} " \
               f"- {self.list_player_scored}."

    def __repr__(self):
        return f"\n{self.name} - {self.start_date} - {self.end_date} - {self.list_match} - {self.list_match_paired} " \
               f"- {self.list_player_scored}."

    def round1(self, list_players):
        """Méthode pour trier une liset de joueur en fonction du classement pour les matchs
        du round 1.
        Args:
            list_players (List): Liste des joueurs
        Returns:
            list_match: Liste des matchs
        """
        players_sorted = (sorted(list_players, key=lambda player: player.ranking, reverse=True))
        players_strong = players_sorted[:4]
        players_weak = players_sorted[-4:]
        self.list_match.append(([players_strong[0]], [players_weak[0]]))
        self.list_match.append(([players_strong[1]], [players_weak[1]]))
        self.list_match.append(([players_strong[2]], [players_weak[2]]))
        self.list_match.append(([players_strong[3]], [players_weak[3]]))
        print(players_strong[0], "  VS  ", players_weak[0])
        print(players_strong[1], "  VS  ", players_weak[1])
        print(players_strong[2], "  VS  ", players_weak[2])
        print(players_strong[3], "  VS  ", players_weak[3])
        return self.list_match

    def next_round(self):
        """Méthode pour matcher les joueurs en fonction du système suisse.
        Un joueur ne peux pas rejouer contre un autre joueur.
        Cette méthode s'applique pour tous les rounds du tournois sauf le round 1.
        """
        for player in self.list_match:
            self.list_player_scored.append(player)
        nb_players = len(self.list_match)
        for i in range(0, nb_players, 2):
            j = i + 1
            while j < nb_players and self.list_match[i][0].id in self.list_match[j][0].tag_players:
                j += 1

            if j == nb_players:
                j -= 1
                p = self.switch(j)
                player_notag = self.list_match[p]
                self.list_match[p] = self.list_match[i]
                self.list_match[i] = player_notag

            else:
                # Changement de place entre un player notag pour mettre 2eme position de la liste.
                player_notag = self.list_match[j]
                self.list_match[j] = self.list_match[i + 1]
                self.list_match[i + 1] = player_notag

        for i in range(0, nb_players, 2):
            self.list_match_paired.append((self.list_match[i], self.list_match[i + 1]))
        return self.list_match_paired

    def switch(self, p):
        m = p - 1
        while m > 0 and (self.list_match[p][0].id in self.list_match[m][0].tag_players) and (self.list_match[m][0].id not in self.list_match[m - 1][0].tag_players):
            m -= 1
        p = m
        return p


class Match:
    """Une classe utilisée pour réprésenter un match.
    """

    def __init__(self):
        self.list_match = []
        self.menu = Menus()
        self.list_scores_sorted = []

    def results(self, list_matchs):
        """Méthode pour appliquer un score à chaque joueur et de tag l'id_player du joueur
        pour savoir si un joueur a deja joué contre un autre joueur.
        :Returns: une liste de joueurs classés par points et par ranking.
        """
        list_scores = []
        i = 0
        for player1, player2 in list_matchs:
            i = i + 1
            score1 = self.menu.check_float(f"""\nRentrer le score de {player1} du match {i}: """)
            score2 = self.menu.check_float(f"""\nRentrer le score de {player2} du match {i}: """)
            # Check list player déjà un score
            if len(player1) == 1:
                player1.append(score1)
                player2.append(score2)
            else:
                player1[1] += score1
                player2[1] += score2

            player1[0].add_tag(player2[0].id)
            player2[0].add_tag(player1[0].id)
            list_scores.append(player1)
            list_scores.append(player2)
        # Trie du ranking des joueurs du plus fort au moins fort
        list_ranking_sorted = (sorted(list_scores, key=lambda player: player[0].ranking, reverse=True))
        # Trie du score des joueurs de plus au moins
        self.list_scores_sorted = (sorted(list_ranking_sorted, key=lambda player: player[1], reverse=True))
        return self.list_scores_sorted
