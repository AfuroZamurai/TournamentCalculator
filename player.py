class Player:
    def __init__(self, elo: int, name: str):
        """
        A PLayer is always part of a tournament and holds information about itself.
        The information can be personal (like name and possibly age, nationality and son on) or general, like points scored.
        :param elo: The Elo rating of this player at the time the tournament is played
        :param name: The full name of the player in the form first name last name
        """
        self.elo = elo
        self.name = name
        self.points: float = 0.0
