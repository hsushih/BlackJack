from cards import *
import unittest

class testCards(unittest.TestCase):
    
    def setUp(self):
        self.rank=Card(6,'D')
        self.rankLower=Card(7,'d')

    def equality(self, rank_one,rank_two):
        ''' return whether rank_one and rank_two are equal'''
        return (rank_one.rank.r == rank_two.rank.r and
                rank_one.rank.s == rank_two.rank.s)

    def testRank(self):
        ''' return whether self.rank works or not'''
        # Case1 the given rank is equal to rank manually input
        self.assertEqual(self.rank.r,6)
        # Case2 the given rank is not equal to rank manually input
        self.assertNotEqual(self.rank.r,7)

    def testSuit(self):
        ''' return whether self.suit works or not'''
        # Case 1 the input suit is uppercase 
        self.assertEqual(self.rank.s,'D')
        # Case 2 the input suit is lowercase
        self.assertEqual(self.rankLower.s,'D')

    def test__str__(self):
        #Case 1 the card is represented in uppercase
        self.assertEqual(str(self.rank), '6D')
        #Case 2 the card is represented in lowercase
        self.assertrankLower=(str(self.rankLower),'7D')

class testDeck(unittest.TestCase):

    def setUp(self):
        self.deck=Deck()


    def testGet_deck(self):
        '''testing whether the function of get_deck works'''
        self.assertEqual(self.deck.get_deck(),[['2', 'S'], ['2', 'C'], ['2', 'H'], ['2', 'D'], ['3', 'S'], ['3', 'C'], ['3', 'H'], ['3', 'D'], ['4', 'S'], ['4', 'C'], ['4', 'H'], ['4', 'D'], ['5', 'S'], ['5', 'C'], ['5', 'H'], ['5', 'D'], ['6', 'S'], ['6', 'C'], ['6', 'H'], ['6', 'D'], ['7', 'S'], ['7', 'C'], ['7', 'H'], ['7', 'D'], ['8', 'S'], ['8', 'C'], ['8', 'H'], ['8', 'D'], ['9', 'S'], ['9', 'C'], ['9', 'H'], ['9', 'D'], ['10', 'S'], ['10', 'C'], ['10', 'H'], ['10', 'D'], ['J', 'S'], ['J', 'C'], ['J', 'H'], ['J', 'D'], ['Q', 'S'], ['Q', 'C'], ['Q', 'H'], ['Q', 'D'], ['K', 'S'], ['K', 'C'], ['K', 'H'], ['K', 'D'], ['A', 'S'], ['A', 'C'], ['A', 'H'], ['A', 'D']])
       

    def testDeal(self):
        ''' testing whether the fuction of deal works'''
        self.assertEqual(self.deck.deal(),['A', 'D'])

    def test__str__(self):
        self.assertEqual(str(self.deck),"['2', 'S']\n['2', 'C']\n['2', 'H']\n['2', 'D']\n['3', 'S']\n['3', 'C']\n['3', 'H']\n['3', 'D']\n['4', 'S']\n['4', 'C']\n['4', 'H']\n['4', 'D']\n['5', 'S']\n['5', 'C']\n['5', 'H']\n['5', 'D']\n['6', 'S']\n['6', 'C']\n['6', 'H']\n['6', 'D']\n['7', 'S']\n['7', 'C']\n['7', 'H']\n['7', 'D']\n['8', 'S']\n['8', 'C']\n['8', 'H']\n['8', 'D']\n['9', 'S']\n['9', 'C']\n['9', 'H']\n['9', 'D']\n['10', 'S']\n['10', 'C']\n['10', 'H']\n['10', 'D']\n['J', 'S']\n['J', 'C']\n['J', 'H']\n['J', 'D']\n['Q', 'S']\n['Q', 'C']\n['Q', 'H']\n['Q', 'D']\n['K', 'S']\n['K', 'C']\n['K', 'H']\n['K', 'D']\n['A', 'S']\n['A', 'C']\n['A', 'H']\n['A', 'D']")
        
unittest.main()
