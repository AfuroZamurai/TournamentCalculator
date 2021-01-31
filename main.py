from tournament import Tournament
from player import Player

if __name__ == '__main__':
    wc = Player(2862, 'Magnus Carlsen')
    challenger = Player(2823, 'Fabiano Caruana')

    players = [wc, challenger]
    wijk = Tournament(players, 14)

    print('Standings:')
    print('-----------------------')

    for player in wijk.players:
        points = player.points
        if points.is_integer():
            print('| {0} {1:.0f}'.format(player.name, player.points))
        else:
            print('| {0} {1:.1f}'.format(player.name, player.points))

