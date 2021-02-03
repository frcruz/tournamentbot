from player import Player
from match import Matches
class Tournament: 

    def __init__(self, admin):
        self.name = 'Tournament Bot Tournament'
        self.admin = admin
        self.timer = 50
        self.players = {}
        self.matches = {}
    def __init__(self, admin, name):
        self.admin = admin
        self.name = name
        self.timer = 50
        self.players = {}
        self.matches = {}

    def add_player(self, name):
        self.players[name] = Player(name)
    
if __name__ == '__main__':
    tournament = Tournament('test', 'name')
    for x in range(0, 9):   
        tournament.add_player("test" + str(x))
    pairings = Matches(tournament.players)
    pairings.create_pairings()
    print(pairings.matches)
    for match in pairings.matches:
        pairings.matches[match].player1.win += 1
    pairings.create_pairings()
    for player in tournament.players:
        print(tournament.players[player].name + ": " + str(tournament.players[player].win))
    print("matchups: ")
    for match in pairings.matches:
        print(pairings.matches[match].player1.name + ": " + str(pairings.matches[match].player1.win))
        print(pairings.matches[match].player2.name + ": " + str(pairings.matches[match].player2.win))