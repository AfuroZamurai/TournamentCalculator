"""
Test with the Tata Steel Masters 2021 in Wijk aan Zee
"""

from typing import Dict, List

from src.pairing import Pairing
from src.result import Result
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

    # round 1
    round1 = [Pairing(players['Magnus Carlsen'], players['Alireza Firouzja'], Result.WHITE_WIN),
              Pairing(players['Radoslaw Wojtaszek'], players['David Anton Guijarro'], Result.DRAWN),
              Pairing(players['Pentala Harikrishna'], players['Maxime-Vachier Lagrave'], Result.DRAWN),
              Pairing(players['Andrey Esipenko'], players['Jan-Krzysztof Duda'], Result.DRAWN),
              Pairing(players['Nils Grandelius'], players['Alexander Donchenko'], Result.WHITE_WIN),
              Pairing(players['Fabiano Caruana'], players['Jorden van Foreest'], Result.DRAWN),
              Pairing(players['Anish Giri'], players['Aryan Tari'], Result.WHITE_WIN)]
    pairings[1] = round1

    # round 2
    round2 = [Pairing(players['David Anton Guijarro'], players['Magnus Carlsen'], Result.DRAWN),
              Pairing(players['Maxime-Vachier Lagrave'], players['Alireza Firouzja'], Result.DRAWN),
              Pairing(players['Alexander Donchenko'], players['Fabiano Caruana'], Result.BLACK_WIN),
              Pairing(players['Jan-Krzysztof Duda'], players['Nils Grandelius'], Result.BLACK_WIN),
              Pairing(players['Jorden van Foreest'], players['Anish Giri'], Result.DRAWN),
              Pairing(players['Pentala Harikrishna'], players['Andrey Esipenko'], Result.DRAWN),
              Pairing(players['Aryan Tari'], players['Radoslaw Wojtaszek'], Result.DRAWN)]
    pairings[2] = round2

    # round 3
    round3 = [Pairing(players['Magnus Carlsen'], players['Aryan Tari'], Result.DRAWN),
              Pairing(players['Anish Giri'], players['Alexander Donchenko'], Result.DRAWN),
              Pairing(players['Radoslaw Wojtaszek'], players['Jorden van Foreest'], Result.DRAWN),
              Pairing(players['Fabiano Caruana'], players['Jan-Krzysztof Duda'], Result.DRAWN),
              Pairing(players['Nils Grandelius'], players['Pentala Harikrishna'], Result.BLACK_WIN),
              Pairing(players['Andrey Esipenko'], players['Maxime-Vachier Lagrave'], Result.DRAWN),
              Pairing(players['Alireza Firouzja'], players['David Anton Guijarro'], Result.WHITE_WIN)]
    pairings[3] = round3

    # round 4
    round4 = [Pairing(players['Jorden van Foreest'], players['Magnus Carlsen'], Result.DRAWN),
              Pairing(players['Maxime-Vachier Lagrave'], players['David Anton Guijarro'], Result.DRAWN),
              Pairing(players['Jan-Krzysztof Duda'], players['Anish Giri'], Result.DRAWN),
              Pairing(players['Andrey Esipenko'], players['Nils Grandelius'], Result.DRAWN),
              Pairing(players['Pentala Harikrishna'], players['Fabiano Caruana'], Result.DRAWN),
              Pairing(players['Alexander Donchenko'], players['Radoslaw Wojtaszek'], Result.DRAWN),
              Pairing(players['Aryan Tari'], players['Alireza Firouzja'], Result.DRAWN)]
    pairings[4] = round4

    # round 5
    round5 = [Pairing(players['Magnus Carlsen'], players['Alexander Donchenko'], Result.DRAWN),
              Pairing(players['Alireza Firouzja'], players['Jorden van Foreest'], Result.DRAWN),
              Pairing(players['David Anton Guijarro'], players['Aryan Tari'], Result.DRAWN),
              Pairing(players['Anish Giri'], players['Pentala Harikrishna'], Result.DRAWN),
              Pairing(players['Fabiano Caruana'], players['Andrey Esipenko'], Result.DRAWN),
              Pairing(players['Nils Grandelius'], players['Maxime-Vachier Lagrave'], Result.WHITE_WIN),
              Pairing(players['Radoslaw Wojtaszek'], players['Jan-Krzysztof Duda'], Result.DRAWN)]
    pairings[5] = round5

    # round 6
    round6 = [Pairing(players['Jan-Krzysztof Duda'], players['Magnus Carlsen'], Result.DRAWN),
              Pairing(players['Maxime-Vachier Lagrave'], players['Aryan Tari'], Result.DRAWN),
              Pairing(players['Jorden van Foreest'], players['David Anton Guijarro'], Result.WHITE_WIN),
              Pairing(players['Nils Grandelius'], players['Fabiano Caruana'], Result.DRAWN),
              Pairing(players['Pentala Harikrishna'], players['Radoslaw Wojtaszek'], Result.DRAWN),
              Pairing(players['Andrey Esipenko'], players['Anish Giri'], Result.DRAWN),
              Pairing(players['Alexander Donchenko'], players['Alireza Firouzja'], Result.BLACK_WIN)]
    pairings[6] = round6

    # round 7
    round7 = [Pairing(players['Magnus Carlsen'], players['Pentala Harikrishna'], Result.DRAWN),
              Pairing(players['David Anton Guijarro'], players['Alexander Donchenko'], Result.DRAWN),
              Pairing(players['Aryan Tari'], players['Jorden van Foreest'], Result.BLACK_WIN),
              Pairing(players['Fabiano Caruana'], players['Maxime-Vachier Lagrave'], Result.WHITE_WIN),
              Pairing(players['Anish Giri'], players['Nils Grandelius'], Result.WHITE_WIN),
              Pairing(players['Alireza Firouzja'], players['Jan-Krzysztof Duda'], Result.WHITE_WIN),
              Pairing(players['Radoslaw Wojtaszek'], players['Andrey Esipenko'], Result.BLACK_WIN)]
    pairings[7] = round7

    # round 8
    round8 = [Pairing(players['Andrey Esipenko'], players['Magnus Carlsen'], Result.WHITE_WIN),
              Pairing(players['Jan-Krzysztof Duda'], players['David Anton Guijarro'], Result.DRAWN),
              Pairing(players['Pentala Harikrishna'], players['Alireza Firouzja'], Result.BLACK_WIN),
              Pairing(players['Maxime-Vachier Lagrave'], players['Jorden van Foreest'], Result.DRAWN),
              Pairing(players['Fabiano Caruana'], players['Anish Giri'], Result.DRAWN),
              Pairing(players['Nils Grandelius'], players['Radoslaw Wojtaszek'], Result.DRAWN),
              Pairing(players['Alexander Donchenko'], players['Aryan Tari'], Result.DRAWN)]
    pairings[8] = round8

    # round 9
    round9 = [Pairing(players['Magnus Carlsen'], players['Nils Grandelius'], Result.WHITE_WIN),
              Pairing(players['Aryan Tari'], players['Jan-Krzysztof Duda'], Result.DRAWN),
              Pairing(players['Jorden van Foreest'], players['Alexander Donchenko'], Result.DRAWN),
              Pairing(players['Radoslaw Wojtaszek'], players['Fabiano Caruana'], Result.BLACK_WIN),
              Pairing(players['Alireza Firouzja'], players['Andrey Esipenko'], Result.DRAWN),
              Pairing(players['Anish Giri'], players['Maxime-Vachier Lagrave'], Result.WHITE_WIN),
              Pairing(players['David Anton Guijarro'], players['Pentala Harikrishna'], Result.DRAWN)]
    pairings[9] = round9

    # round 10
    round10 = [Pairing(players['Fabiano Caruana'], players['Magnus Carlsen'], Result.DRAWN),
               Pairing(players['Maxime-Vachier Lagrave'], players['Alexander Donchenko'], Result.WHITE_WIN),
               Pairing(players['Andrey Esipenko'], players['David Anton Guijarro'], Result.WHITE_WIN),
               Pairing(players['Nils Grandelius'], players['Alireza Firouzja'], Result.DRAWN),
               Pairing(players['Anish Giri'], players['Radoslaw Wojtaszek'], Result.WHITE_WIN),
               Pairing(players['Jan-Krzysztof Duda'], players['Jorden van Foreest'], Result.DRAWN),
               Pairing(players['Pentala Harikrishna'], players['Aryan Tari'], Result.DRAWN)]
    pairings[10] = round10

    # round 11
    round11 = [Pairing(players['Magnus Carlsen'], players['Anish Giri'], Result.DRAWN),
               Pairing(players['Alexander Donchenko'], players['Jan-Krzysztof Duda'], Result.DRAWN),
               Pairing(players['Aryan Tari'], players['Andrey Esipenko'], Result.WHITE_WIN),
               Pairing(players['Jorden van Foreest'], players['Pentala Harikrishna'], Result.WHITE_WIN),
               Pairing(players['Alireza Firouzja'], players['Fabiano Caruana'], Result.DRAWN),
               Pairing(players['David Anton Guijarro'], players['Nils Grandelius'], Result.DRAWN),
               Pairing(players['Radoslaw Wojtaszek'], players['Maxime-Vachier Lagrave'], Result.DRAWN)]
    pairings[11] = round11

    # round 12
    round12 = [Pairing(players['Radoslaw Wojtaszek'], players['Magnus Carlsen'], Result.DRAWN),
               Pairing(players['Nils Grandelius'], players['Aryan Tari'], Result.DRAWN),
               Pairing(players['Fabiano Caruana'], players['David Anton Guijarro'], Result.DRAWN),
               Pairing(players['Anish Giri'], players['Alireza Firouzja'], Result.DRAWN),
               Pairing(players['Andrey Esipenko'], players['Jorden van Foreest'], Result.DRAWN),
               Pairing(players['Maxime-Vachier Lagrave'], players['Jan-Krzysztof Duda'], Result.DRAWN),
               Pairing(players['Pentala Harikrishna'], players['Alexander Donchenko'], Result.WHITE_WIN)]
    pairings[12] = round12

    # round 13
    round13 = [Pairing(players['David Anton Guijarro'], players['Anish Giri'], Result.DRAWN),
               Pairing(players['Alexander Donchenko'], players['Andrey Esipenko'], Result.BLACK_WIN),
               Pairing(players['Magnus Carlsen'], players['Maxime-Vachier Lagrave'], Result.WHITE_WIN),
               Pairing(players['Jorden van Foreest'], players['Nils Grandelius'], Result.WHITE_WIN),
               Pairing(players['Aryan Tari'], players['Fabiano Caruana'], Result.DRAWN),
               Pairing(players['Alireza Firouzja'], players['Radoslaw Wojtaszek'], Result.DRAWN),
               Pairing(players['Jan-Krzysztof Duda'], players['Pentala Harikrishna'], Result.DRAWN)]
    pairings[13] = round13

    return pairings


if __name__ == '__main__':
    name = 'Tata Steel Masters 2021'
    players = get_players()
    rounds = 13
    tiebreaks = ['Direct encounter', 'Sonneborn-Berger', 'Games with Black']
    pairings = get_pairings(players)

    tournament = Tournament(name, players, rounds, tiebreaks, pairings)
    standings = tournament.calculate_standings()
    print('{0}, Standings after round {1}:\n'.format(name, len(pairings)))
    print(standings)
