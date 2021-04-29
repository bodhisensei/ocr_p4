class Players:
    """Une classe pour générer un joueur avec ces attributs.
    """
    def __init__(self, first_name="", last_name="", date_of_birth="", sex="", ranking=None, id=None):

        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ranking = ranking
        self.id = id
        self.tag_players = []

    def __str__(self):
        return f"""{self.first_name} {self.last_name} - classement {self.ranking}"""

    def __repr__(self):
        return f"""{self.first_name} {self.last_name} - classement {self.ranking}"""

    def add_tag(self, id):
        """Methode pour tag l'id d'un joueur déjà affronté
        """
        self.tag_players.append(id)

    def serialize_player(self):
        """Méthode de la classe Players qui permet de sérialiser l'objet Players
        :return: un dictionnaire de l'objet Players
        """
        return {"first_name": self.first_name, "last_name": self.last_name, "date_of_birth": self.date_of_birth,
                "sexe": self.sex, "ranking": self.ranking, "tag_players": self.tag_players, "id": self.id}

    # @staticmethod
    # def auto_players():
    #     """
    #     """
    #     player1 = Players("Pat", "Vio", "2702", "male", 80, 1)
    #     player2 = Players("Lony", "Vio", "1212", "male", 40, 2)
    #     player3 = Players("Flo", "Jean", "0306", "male", 50, 3)
    #     player4 = Players("Hugo", "Jean", "2312", "male", 50, 4)
    #     player5 = Players("Dan", "Vio", "0102", "male", 60, 5)
    #     player6 = Players("Thor", "God", "2404", "male", 30, 6)
    #     player7 = Players("Yann", "Del", "1703", "male", 20, 7)
    #     player8 = Players("Greg", "ST", "1810   ", "male", 10, 8)
    #     return [player1, player2, player3, player4, player5, player6, player7, player8]
