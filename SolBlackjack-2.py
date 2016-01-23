from cards import *

class BlackJack(object):


    def __init__(self,table={'row1':[1,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]},discardList=[17,18,19,20]):
        self.deck=Deck()
        self.table=table
        self.discardList=discardList
        self.in_the_game =True
        self.choice = 0
        


    def currentTable(self):
        ''' display the current status of the table'''
        tableList = []
        tableList.append('Hands on the Table :')
        for row, cards in self.table.iteritems():
            row_string = (str(card) for card in cards)
            tableList.append(row + ':' + ','.join(row_string))
        discard_card=','.join([str(card) for card in self.discardList])
        tableList.append('Discards Table:')
        tableList.append(discard_card)
        ','.join(tableList)
        return '\n'.join(tableList)
    
        
    def place_a_card_on_the_grid(self,card,position):
        ''' place a card in the assigned position on the table'''
        card=card.upper()
        if position in self.table.values()[0]:
            cardPosition = self.table['row1'].index(position)
            self.table['row1'][cardPosition]=card 
        elif position in self.table.values()[1]:
            cardPosition = self.table['row2'].index(position)
            self.table['row2'][cardPosition]=card        
        elif position in self.table.values()[2]:
            cardPosition = self.table['row3'].index(position)
            self.table['row3'][cardPosition]=card
        elif position in self.table.values()[3]:
            cardPosition = self.table['row4'].index(position)
            self.table['row4'][cardPosition]=card
        elif position in self.discardList:
            cardPosition = self.discardList.index(position)
            self.discardList[cardPosition] = card
        else:
            print ' that position has a card you previously placed already'
        


    def check_game(self):
        ''' check to see if the game is over'''
        for item in self.table.values():
            for position in item:
                if type(position) == int:
                    return True
        self.in_the_game = False
        return False

    def calculate_total_score(self):
        ''' calculate the total socre based on accmulated scores in each row and column'''
        column1_1And2_2List=[]
        column2List=[]
        column3List=[]
        column4List=[]
        column5List=[]
        row1=self.score_a_hand(self.table['row1'])
        row2=self.score_a_hand(self.table['row2'])
        row3=self.score_a_hand(self.table['row3'])
        row4=self.score_a_hand(self.table['row4'])
        column1_1=self.table.values()[0][0]
        column1_2=self.table.values()[1][0]
        column1_1And2_2List.append(column1_1)
        column1_1And2_2List.append(column1_2)
        column1=self.score_a_hand(column1_1And2_2List)
        column2_1=self.table.values()[0][1]
        column2_2=self.table.values()[1][1]
        column2_3=self.table.values()[2][0]
        column2_4=self.table.values()[3][0]
        column2List.append(column2_1)
        column2List.append(column2_2)
        column2List.append(column2_3)
        column2List.append(column2_4)
        column2=self.score_a_hand(column2List)
        column3_1=self.table.values()[0][2]
        column3_2=self.table.values()[1][2]
        column3_3=self.table.values()[2][1]
        column3_4=self.table.values()[3][1]
        column3List.append(column3_1)
        column3List.append(column3_2)
        column3List.append(column3_3)
        column3List.append(column3_4)
        column3=self.score_a_hand(column3List)
        column4_1=self.table.values()[0][3]
        column4_2=self.table.values()[1][3]
        column4_3=self.table.values()[2][2]
        column4_4=self.table.values()[3][2]
        column4List.append(column4_1)
        column4List.append(column4_2)
        column4List.append(column4_3)
        column4List.append(column4_4)
        column4=self.score_a_hand(column4List)
        column5_1=self.table.values()[0][4]
        column5_2=self.table.values()[1][4]
        column5List.append(column5_1)
        column5List.append(column5_2)
        column5=self.score_a_hand(column5List)
        
        total_score =row1 + row2 + row3 + row4 + column1 + column2 + column3 + column4 + column5
        return total_score
        

    def score_a_hand(self,table):
        ''' scoring the hands for rows and columns'''
        card_sum = 0
        cardIncludesAce = False
        for card in table:
            card=card.upper()
            self.card_info = Card(card[:-1],card[1])
            self.card_info.get_rank()
            if self.card_info.get_rank() == 'A':
                cardIncludesAce = True
            elif self.card_info.get_rank() == 'J' or self.card_info.get_rank() == 'Q' or self.card_info.get_rank() == 'K':
                card_sum = card_sum +10
            elif self.card_info.get_rank() in ['B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                print 'invalid input'
            elif int(self.card_info.get_rank()) in range(2,11):
                card_sum = card_sum + int(self.card_info.get_rank())
                
        if card_sum < 11 and cardIncludesAce == True:
            card_sum = card_sum +11
        elif card_sum > 11 and cardIncludesAce == True:
            card_sum= card_sum +1
            
        if card_sum > 21:
            return 0
        if card_sum == 21:
            if len(table) == 2:
                return 10
            return 7
        if card_sum == 20:
            return 5
        if card_sum == 19:
            return 4
        if card_sum == 18:
            return 3
        if card_sum == 17:
            return 2
        if card_sum == 16:
            return 1
        if card_sum < 16:
            return 0
        
        
    def readFromHighScore(self):
        ''' read the highest score from file'''
        self.fo=open('highScore.txt','r')
        int_score=''.join(self.fo.readlines())
        return int(int_score)

    def writeFromHighScore(self,highScore):
        ''' write the highest score into the file'''
        self.fo=open('highScore.txt','w')
        self.fo.writelines(highScore)

        

    def error_checking(self,position):
        ''' error checking'''
        choice = 0
        while choice ==0:
            if position =='':
                return position
            
            elif position in str(range(1,21)):
                choice = 1 
                return position
        
            else:
                return position

    def print_welcome_message(self):
        print ''' Welcome to Stanley Game World! The game you are about to play is a slightly different
                  version of BlackJack you usually play but basically the ruels are the same. You are
                  trying to get points as close to 21 as possible but not beyond 21 which you will get
                  BUST and a score of zero for the entire row or column. When the game starts you should be able
                  to see a table with 5 columns and 4 rows. For each row and column, you are doing your
                  best efforts to get scores as high as possible but again not beyond 21 for each row and
                  column. In the end of the game, we will calculate the totalsocres you obtain depending
                  on the points you get for each row and column. The rules of scoring are shown in the table below!
                  
                  Hand Points Explanation
                  Blackjack 10 Blackjack is two cards that total 21
                  
                  points  scores   number of cards in each row or column
                  21      7        3, 4 or 5 cards total 21
                  20      5        Hand totals 20
                  19      4        Hand totals 19
                  18      3        Hand totals 18
                  17      2        Hand totals 17
                  16 and others 1 Hand totals 16 or less
                  BUST 0 Hand totals 22 or more


                  Alright! Let's start the game now!!!! YOHOHOHOOOO! \n '''
        

                       
    def play(self):
        self.print_welcome_message()
        print self.currentTable()
        self.deck.shuffle()
        dealt_card = self.deck.deal()
        while self.in_the_game == True:
            print ' the card you get is', dealt_card[0] + dealt_card[1]
            position = raw_input('enter the position you want to place your card in')
            position_correct=self.error_checking(position)
            if position_correct == '':
                print 'invalid input \n'
                print self.currentTable()
            elif position_correct in str(range(1,21)):
                position_correct=int(position_correct)
                try:
                    self.place_a_card_on_the_grid((dealt_card[0]+dealt_card[1]),position_correct)
                    dealt_card = self.deck.deal()
                    print self.currentTable()
                except ValueError:
                    pass
            else:
                print 'the number is either too large or you enter something that does not make sense you stupid guy \n'
                print self.currentTable()

            self.check_game()
        print ' we are gonna calcuate your total socre. Good Luck!!!'
        self.calculate_total_score()
        print 'the total score you got is', self.calculate_total_score()
        if self.calculate_total_score() > self.readFromHighScore():
            total_score = self.calculate_total_score()
            self.writeFromHighScore(str(total_score))
            print ' Congradulations!!! You broke the record of ', self.readFromHighScore(), 'Now, the new record is', self.calculate_total_score()

        while self.choice == 0:
            wanna_play_again = raw_input('wanna play again to break the record y/n')
            
            if wanna_play_again == 'y':
                play_again=BlackJack(table={'row1':[1,2,3,4,5],'row2':[6,7,8,9,10],'row3':[11,12,13],'row4':[14,15,16]},discardList=[17,18,19,20])
                print play_again.currentTable()
                play_again.deck.shuffle()
                dealt_card = play_again.deck.deal()
                while play_again.in_the_game == True:
                    print ' the card you get is', dealt_card[0] + dealt_card[1]
                    position = raw_input('enter the position you want to place your card in')
                    position_correct=play_again.error_checking(position)
                    if position_correct == '':
                        print 'invalid input \n'
                        print play_again.currentTable()
                    elif position_correct in str(range(1,21)):
                        position_correct=int(position_correct)
                        try:
                            play_again.place_a_card_on_the_grid((dealt_card[0]+dealt_card[1]),position_correct)
                            dealt_card = play_again.deck.deal()
                            print play_again.currentTable()
                        except ValueError:
                            pass
                    else:
                        print 'the number is either too large or you enter something that does not make sense you stupid guy \n'
                        print play_again.currentTable()

                    play_again.check_game()
                print ' we are gonna calcuate your total socre. Good Luck!!!'
                play_again.calculate_total_score()
                print 'the total score you got is', play_again.calculate_total_score()
                if play_again.calculate_total_score() > play_again.readFromHighScore():
                    total_score = play_again.calculate_total_score()
                    play_again.writeFromHighScore(str(total_score))
                    print ' Congradulations!!! You broke the record of ', play_again.readFromHighScore(), 'Now, the new record is', play_again.calculate_total_score()
                    
            elif wanna_play_again =='n':
                    print 'Enojy the rest of your day !! Bye Bye!!'
                    self.choice=1
                    break
            else:
                print 'invalid input'


        


                                         
                                        
                   
     
               
     
         

        
        

    


