#table must be unique
import random

#constants
POINTS_WIN = 3
POINTS_DRAW = 1
class Matches: 
    def __init__(self, players):
        self.players = players
        self.matches = {}

    class Match: 
        def __init__(self, table, player1, player2):
            self.table = table
            self.player1 = player1
            self.player2 = player2

    def create_groups(self, players):
        groups = {}
        for player in players: 
            points = players[player].win * POINTS_WIN + players[player].draw * POINTS_DRAW
            if points not in groups:
                player_list = list()
                player_list.append(players[player])
                groups[points] = player_list
            else:
                groups[points].append(players[player])
        return groups

    def create_pairings(self):
        print("Swiss matchmaking")
        matches = {}
        groups = []
        groups = self.create_groups(self.players)
        for group in groups: 
            player1 = None
            player2 = None
            random_players = []
            for player in groups[group]:
                random_players.append(player)
            random.shuffle(random_players)
            id = 0
            for player in random_players:
                if player1 is None:
                    player1 = player
                    #print("p1: " + player1)
                elif player2 is None:
                    player2 = player
                    #print("p2: " + player2)
                if player1 and player2 is not None:
                    match = self.Match(id, player1, player2)
                    player1 = None
                    player2 = None
                    self.matches[id] = match
                    id += 1
            if player1 is not None and player2 is None:
                try: 
                    groups[group + 1].append(player1)
                except:
                    print("xception")
                    player1.win += 1
            

        return matches

    
        
        
