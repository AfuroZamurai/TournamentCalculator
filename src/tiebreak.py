from collections import defaultdict
from typing import Dict, List

from src.pairing import Pairing
from src.player import PlayerList
from src.result import Result


def sonneborn_berger(table: List[Dict], players: PlayerList, pairings: Dict[int, List[Pairing]], relevance: int):
    for row in table:
        sb = 0.0
        player = players[row['name']]
        for name, results in player.opponents.items():
            for result in results:
                if result == Result.LOSS:
                    continue
                factor = 1
                if result == Result.DRAW:
                    factor = 0.5

                sb += factor * players[name].points
        if sb.is_integer():
            row['Sonneborn-Berger'] = int(sb)
        else:
            row['Sonneborn-Berger'] = sb

    return table


def direct_encounter(table: List[Dict], players: PlayerList, pairings: Dict[int, List[Pairing]], relevance: int):
    same_points = defaultdict(set)
    for i, player in enumerate(table):
        points = player['points']
        for j, opponent in enumerate(players.players):
            if i != j and points == str(opponent.pretty_points()):
                same_points[points].add(opponent)

    de_points = defaultdict(float)
    for point_group in same_points.values():
        for player in point_group:
            de_points[player.name] = 0
            for round in pairings.values():
                for game in round:
                    if game.player_white == player and game.player_black in point_group:
                        if game.result == Result.WHITE_WIN:
                            de_points[player.name] += 1
                        elif game.result == Result.DRAWN:
                            de_points[player.name] += 0.5
                    elif game.player_black == player and game.player_white in point_group:
                        if game.result == Result.BLACK_WIN:
                            de_points[player.name] += 1
                        elif game.result == Result.DRAWN:
                            de_points[player.name] += 0.5

    for row in table:
        if row['name'] in de_points.keys():
            row['Direct encounter'] = de_points[row['name']]
        else:
            row['Direct encounter'] = 0

    return table


def number_blacks(table: List[Dict], players: PlayerList, pairings: Dict[int, List[Pairing]], relevance: int):
    for row in table:
        p = players[row['name']]
        num_blacks = 0
        for r in pairings.values():
            for pairing in r:
                if pairing.player_black == p:
                    num_blacks += 1
        row['Games with Black'] = num_blacks
    return table


def number_wins(table: List[Dict], players: PlayerList, pairings: Dict[int, List[Pairing]], relevance: int):
    for row in table:
        p = players[row[0]]
        row['Number of wins'] = p.num_wins
    return table


def buchholz(table: List[Dict], players: PlayerList, pairings: Dict[int, List[Pairing]], relevance: int):
    return table
