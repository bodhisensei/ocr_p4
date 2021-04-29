class Tournament:
    """Une classe pour générer un tournoi avec ces attributs.
    """

    def __init__(self, name=None, location=None, date=None, time_control=None, description=None):

        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.description = description
        self.list_players = []
        self.rounds = 4

    def __str__(self):
        return f"Le tournoi {self.name} de {self.location} de type {self.time_control} est pour le {self.date} " \
               f"est programmé."

    def __repr__(self):
        return f"Le tournoi {self.name} de {self.location} de type {self.time_control} est pour le " \
               f"{self.date} est rentré."

    def add_player(self, player):
        self.list_players.append(player)

    def serialize_tournament(self):
        """
        """
        return {'name': self.name, 'location': self.location, 'date': self.date,
                'nb_round': self.rounds, 'time_control': self.time_control,
                'description': self.description}
