from SolBlackjack import *
import unittest

class testSolBlackjack(unittest.TestCase):

    def setUp(self):
        self.blackjack=BlackJack(table={'row1':['6D',2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]},discardList=[17,18,19,20])
        self.blackjack2=BlackJack(table={'row1':[1,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]},discardList=[17,18,19,20])
        self.blackJack=BlackJack(table={'row1':['6D',2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]},discardList=['AH',18,19,20])
        self.BLACKJACK=BlackJack(table={'row1':['6D','3C','4C','5H','7H'],'row2':['8H','9H','10H','JH','QH'],'row3':['KH','9C','AH'],'row4':['JD','9D','AD']},discardList=[17,18,19,20])
        self.BLACKJACK2=BlackJack(table={'row1':['6d','3c','4c','5h','7h'],'row2':['8h','9h','10h','Jh','Qh'],'row3':['Kh','9c','Ah'],'row4':['Jd','9d','Ad']},discardList=[17,18,19,20])
        discardList=[17,18,19,20]

        
    def testCurrentTable(self):
        ''' test whehter the fucntion of Currenttable thorws the correct status of the current table'''
        # Case 1 display the status of the current table with only one card placed on the table
        self.assertEqual(self.blackjack.currentTable(),'Hands on the Table :\nrow1:6D,2,3,4,5\nrow2:6,7,8,9,10\nrow3:11,12,13\nrow4:14,15,16\nDiscards Table:\n17,18,19,20')
        # Case 2 display the status of the current Discards with only one discarded card
        self.assertEqual(self.blackJack.currentTable(),'Hands on the Table :\nrow1:6D,2,3,4,5\nrow2:6,7,8,9,10\nrow3:11,12,13\nrow4:14,15,16\nDiscards Table:\nAH,18,19,20')
        
    def testPlace_a_card_on_the_grid(self):
        ''' test whether the function of place a card on the grid works '''
        self.blackjack.place_a_card_on_the_grid('2C',2)
        self.blackjack2.place_a_card_on_the_grid('3h',1)
        # Case 1 place a card in one of the positions on the table
        self.assertEqual(self.blackjack.currentTable(),'Hands on the Table :\nrow1:6D,2C,3,4,5\nrow2:6,7,8,9,10\nrow3:11,12,13\nrow4:14,15,16\nDiscards Table:\n17,18,19,20')
        # Case 2 place a card in one of the positions in Discards
        self.assertEqual(self.blackJack.currentTable(),'Hands on the Table :\nrow1:6D,2,3,4,5\nrow2:6,7,8,9,10\nrow3:11,12,13\nrow4:14,15,16\nDiscards Table:\nAH,18,19,20')
        # Case 3 case senstivity
        self.assertEqual(self.blackjack2.currentTable(),'Hands on the Table :\nrow1:3H,2,3,4,5\nrow2:6,7,8,9,10\nrow3:11,12,13\nrow4:14,15,16\nDiscards Table:\n17,18,19,20')
        
    def testCalculateTotalScore(self):
        ''' test wheter the total calcualted score is correct'''
        #Case 1 uppercase
        self.assertEqual(self.BLACKJACK.calculate_total_score(),13)
        # Case 2 lowercase
        self.assertEqual(self.BLACKJACK2.calculate_total_score(),13)

    def testCheckGame(self):
        # Case 1 the game is over
        self.assertEqual(False,self.BLACKJACK.check_game())
        # Case 2 we are still in the game
        self.assertEqual(True,self.blackjack.check_game())
             

    def testScore_a_hand(self):
        ''' test wether the socre caculated per table is correct regardless of case sensetivity'''
        #Case 1 uppercase Blackjack with five cards 
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','6C','3D']), 7)
        #Case 2 uppercase twenty-one points with two cards
        self.assertEqual(self.blackjack.score_a_hand(['KD','AC']), 10)
        #Case 3 uppercase twenty points with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','6C','2D']), 5)
        #Case 4 uppercase nighteen points with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','6C','AD']), 4)
        #Case 5 uppercase eighteen points with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','3H','3D']), 3)
        #Case 6 uppercase seventeen points with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','2H','3D']), 2)
        #Case 7 uppercase sixteen points with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','AC','3D']), 1)
        #Case 8 uppercase fourteen points with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','AC','AD']), 0)
        #Case 9 uppercase BUST
        self.assertEqual(self.blackjack.score_a_hand(['3C','4C','5C','6C','KD']), 0)
        #Case 10 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','6c','3d']), 7)
        #Case 11 lowercase Blackjack with two cards
        self.assertEqual(self.blackjack.score_a_hand(['kd','ac']), 10)
        #Case 12 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','6c','2d']), 5)
        #Case 13 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','6c','ad']), 4)
        #Case 14 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','3h','3d']), 3)
        #Case 15 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','2h','3d']), 2)
        #Case 16 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','ac','3d']), 1)
        #Case 17 lowercase Blackjack with five cards
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','ac','ad']), 0)
        #Case 18 lowercase BUST
        self.assertEqual(self.blackjack.score_a_hand(['3c','4c','5c','6c','kd']), 0)
                         
        
unittest.main()
