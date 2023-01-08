#card class
#suit,rank,integer value
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self,rank,suit):
        self.suit=suit.capitalize()
        self.rank=rank.capitalize()
        self.value=values[rank.capitalize()]
    def __str__(self):
        return self.rank + ' of '+self.suit
#deck class
class Deck:
    def __init__(self):
        self.all_cards=[]
        #create each card
        for suit in suits:
            for rank in ranks:
                #create all cards
                created_card=Card(rank,suit)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
#Player class
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        #list of multiple card objects
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        #single card object
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'PLayer {self.name} has {len(self.all_cards)} cards'
# GAME SETUP
player_one=Player('One')
player_two=Player('Two')

new_deck=Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on=True
round_num=0

while game_on:
    
    round_num+=1
    print (f'Round #{round_num}')
    
    if len(player_one.all_cards)==0:
           print ('Player 1 has no cards. Player 2 wins!')
           game_on=False
           break
    if len(player_two.all_cards)==0:
           print ('Player 2 has no cards. Player 1 wins!')
           game_on=False
           break
    #Start new round
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
           
    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())
    
    #while at_war
    
    at_war=True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
            
        elif player_two_cards[-1].value>player_one_cards[-1].value:
            
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war=False
            
        else:
            print('WAR!')
            if len(player_one.all_cards)<5:
                print('Player 1 is out of cards!')
                print('Player 2 wins!')
                game_on=False
                break
                
            elif len(player_two.all_cards)<5:
                print('Player 2 is out of cards!')
                print('Player 1 wins!')
                game_on=False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())