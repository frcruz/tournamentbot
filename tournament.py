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
    for x in range(0, 8):
        tournament.add_player("test" + str(x))
    pairings = Matches(tournament.players)
    pairings.create_pairings()
    print(pairings.matches)