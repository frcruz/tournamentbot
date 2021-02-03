import unittest
from tournament import Tournament

class TestTournament(unittest.TestCase):

    def test_add_players(self):
        tournament = Tournament('test', 'name')
        for x in range(0, 9):   
            tournament.add_player("test" + str(x))
        self.assertEqual(9, len(tournament.players))

if __name__ == '__main__':
    unittest.main()