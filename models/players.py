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
