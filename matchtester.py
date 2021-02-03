import unittest

from tournament import Tournament
from match import Matches
class TestMatches(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_pairings_even(self):
        tournament = Tournament('test', 'name')
        for x in range(0, 8):   
            tournament.add_player("test" + str(x))
        self.assertEqual(8, len(tournament.players))
        pairings = Matches(tournament.players)
        pairings.create_pairings()
        self.assertEqual(4, len(pairings.matches))
        win_count = 0
        bye_player = None
        for player in tournament.players: 
            if tournament.players[player].win == 1:
                win_count += 1
    
        self.assertEqual(0, win_count)
        
    def test_create_pairings_odd(self):
        tournament = Tournament('test', 'name')
        for x in range(0, 9):   
            tournament.add_player("test" + str(x))
        self.assertEqual(9, len(tournament.players))
        pairings = Matches(tournament.players)
        pairings.create_pairings()
        self.assertEqual(4, len(pairings.matches))
        win_count = 0
        bye_player = None
        for player in tournament.players: 
            if tournament.players[player].win == 1:
                win_count += 1
        
        self.assertEqual(1, win_count)

    def test_create_pairings_multiple(self):
        tournament = Tournament('test', 'name')
        for x in range(0, 8):   
            tournament.add_player("test" + str(x))
        self.assertEqual(8, len(tournament.players))
        for x in range(1, 4):
            three_win = 0
            two_win = 0
            one_win = 0
            zero_win = 0
            if x == 1:
                three_win = 0
                two_win = 0
                one_win = 4
                zero_win = 4
            elif x == 2:
                three_win = 0
                two_win = 2
                one_win = 4
                zero_win = 2
            elif x == 3:
                three_win = 1
                two_win = 3
                one_win = 3
                zero_win = 1
            pairings = Matches(tournament.players)
            pairings.create_pairings()
            self.assertEqual(4, len(pairings.matches))
            three_win_count = 0
            two_win_count = 0
            one_win_count = 0
            zero_win_count = 0
            for match in pairings.matches:
                pairings.matches[match].player1.win += 1
            for player in tournament.players: 
                if tournament.players[player].win == 3:
                    three_win_count += 1
                elif tournament.players[player].win == 2:
                    two_win_count += 1
                elif tournament.players[player].win == 1:
                    one_win_count += 1
                elif tournament.players[player].win == 0:
                    zero_win_count += 1
            self.assertEqual(three_win, three_win_count)
            self.assertEqual(two_win, two_win_count)
            self.assertEqual(one_win, one_win_count)
            self.assertEqual(zero_win, zero_win_count)

if __name__ == '__main__':
    unittest.main()