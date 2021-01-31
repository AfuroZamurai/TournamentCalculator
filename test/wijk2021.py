"""
Test with the Tata Steel Masters 2021 in Wijk aan Zee
"""

from typing import Dict, List

from src.pairing import Pairing
from src.pairing import Result
from src.player import Player
from src.player import PlayerList
from src.tournament import Tournament


def get_players() -> PlayerList:
    participants = [Player(2862, 'Magnus Carlsen'), Player(2823, 'Fabiano Caruana'),
                    Player(2784, 'Maxime-Vachier Lagrave'), Player(2764, 'Anish Giri'),
                    Player(2749, 'Alireza Firouzja'), Player(2743, 'Jan-Krzysztof Duda'),
                    Player(2732, 'Pentala Harikrishna'), Player(2705, 'Radoslaw Wojtaszek'),
                    Player(2679, 'David Anton Guijarro'), Player(2677, 'Andrey Esipenko'),
                    Player(2671, 'Jorden van Foreest'), Player(2668, 'Alexander Donchenko'),
                    Player(2663, 'Nils Grandelius'), Player(2625, 'Aryan Tari')]

    return PlayerList(participants)


def get_pairings(players: PlayerList) -> Dict[int, List[Pairing]]:
    pairings = {}
    round1 = [Pairing(players['Magnus Carlsen'], players['Alireza Firouzja'], Result.WHITE_WIN),
              Pairing(players['Radoslaw Wojtaszek'], players['David Anton Guijarro'], Result.DRAW),
              Pairing(players['Pentala Harikrishna'], players['Maxime-Vachier Lagrave'], Result.DRAW),
              Pairing(players['Andrey Esipenko'], players['Jan-Krzysztof Duda'], Result.DRAW),
              Pairing(players['Nils Grandelius'], players['Alexander Donchenko'], Result.WHITE_WIN),
              Pairing(players['Fabiano Caruana'], players['Jorden van Foreest'], Result.DRAW),
              Pairing(players['Anish Giri'], players['Aryan Tari'], Result.WHITE_WIN)]
    pairings[1] = round1

    return pairings


if __name__ == '__main__':
    players = get_players()
    rounds = 13
    tiebreaks = ['Direct encounter', 'Sonneborn Berger', 'Games with Black']
    pairings = get_pairings(players)

    tournament = Tournament(players, rounds, tiebreaks, pairings)
    standings = tournament.calculate_standings()
    print(standings)
