# hit the 'play' button on the top-left corner of this page

#Rules of Blackjack:

# 1. You are playing against the dealer who gives you
#    2 cards(both face up) and takes 2 cards(1 face 
#    up and 1 face down) from a deck of 52 shuffled cards.
# 2. each card has a value.all the numbered cards have the 
#    value equal to its number,all face cards(king,queen 
#    or jack) have value 10 and the ace can have either 
#    value 1 or 11,whatever is in the favour of the player
#    or the dealer himself
# 3. the object of the game is to have your hand's value 
#    greater than that of the dealer,without exceeding 
#    the value 21.this means that if your hand's value is 
#    greater than 21,you loose instantly !!!
# 4. for example,suppose,your hand's value is 14 and the 
#    dealler's hand's value is 18,you loose !!!
# 5. you have 2 options in the game:hit or stand
# 6. 'hit' means getting an extra card from the same deck of
#    52 cards,adding to your hand's value
#    and stand makes the dealer show his hand and 
#    accordingly the result of the game is decided.
# 7. if,after you decide to 'stand',the dealer's hand's value 
#    is less than or equal to 17,the dealer will keep 
#    adding a card to his hand from the same deck until his
#    hand's value exceeds 17
# 8. 'deal' means that the deck of 52 cards is reshuffled 
#    and the same game is restarted again
# 9. if the dealer exceeds 21,he gets bust and you win !!!
# 10.dealer wins tie,in this version of blackjack

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# finally finished :D
# Mini-project #6 - Blackjack

import simplegui
import random 

HEIGHT = 400
WIDTH = 650

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    


in_play = False
outcome = ""
score = 0

busted = ''

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        
class Hand:
    def __init__(self):
        self.cards = []
        
        
    def __str__(self):
        x = ''
        for card in self.cards:
             x += ' ' + str(card) 
        return 'hand contains' + x
    
   
    def add_card(self,card):
        return self.cards.append(card)
    
     
    def get_value(self):
        global val
        val = 0
        for card in self.cards:
            val += VALUES[card.rank]
        
        if ('A' in card.rank) and (val + 10 <= 21):
                val += 10
               
        return val
       
         
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas,pos)
            pos[0] += CARD_SIZE[0] + 10

            
            
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit , rank))
                
                
    def shuffle(self):
        random.shuffle(self.deck)
        
        
    def deal_card(self):
        c = random.choice(self.deck)
        self.deck.remove(c)
        return c
    
    def __str__(self):
        x = ''
        for card in self.deck:
            x += ' ' + str(card) 
        return 'deck contains' + x    
    
    
def deal():
    global outcome, in_play
    global my_deck , my_hand,dealer_hand,outcome
    global busted
    
    if not in_play: 
        outcome = 'Hit or Stand ?'

        my_deck = Deck()
        my_deck.shuffle()

        my_hand = Hand()
        dealer_hand = Hand()

        my_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        my_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())

        print
        print 'my ',my_hand
        print 'my hands value: ',my_hand.get_value()
        print 'dealer',dealer_hand
        print 'dealers hands value: ',dealer_hand.get_value()

    in_play = True
    busted = ''

def hit():
    global my_deck,my_hand
    global score ,in_play , outcome
    global busted
    
    if in_play :
        my_hand.add_card(my_deck.deal_card())
        if my_hand.get_value() > 21:
            outcome = 'New Deal ?'
            busted = 'BUSTED !!!'
            
            print 'my hands are: ',my_hand
            print 'my hand value is: '
            print my_hand.get_value()
            print 'busted'
            score -= 1   
            print 'score : ',score
            in_play = False
            print 'inplay: ',in_play
        else:
            outcome = 'Hit or Stand ?'
            print 'my hands are: ',my_hand
            print 'my hand value is: '
            print my_hand.get_value()
            print 'not YET busted :P '  
            print 'score : ',score
            print 'inplay: ',in_play
            print
            
            
            
def stand():
    global my_deck , my_hand,dealer_hand
    global score , in_play,outcome
    global busted
    
    
    
    if in_play:
        while dealer_hand.get_value() < 17 :
            dealer_hand.add_card(my_deck.deal_card())
    
        if dealer_hand.get_value() > 21:
            score += 1
            outcome = 'New Deal ?'
            busted = 'Dealer went BUST B]'
            print 'dealers hand: '
            print dealer_hand
            print 'dealers value'
            print dealer_hand.get_value()
            print 'dealer went bust !'
            print 'score: ', score
            in_play = False
            
        elif my_hand.get_value() > dealer_hand.get_value() :
            score += 1
            outcome = 'New Deal ?'
            busted = 'You Won !!! :D'
            print 'dealers hand: '
            print dealer_hand
            print 'dealers value'
            print dealer_hand.get_value()
            print 'jeet gaya tu !'
            print 'score: ' , score
            in_play = False
        else:
            outcome = 'New Deal ?'
            busted = "Dealer Won :O"
            print 'dealers hand:'
            print dealer_hand
            print 'dealers value'
            print dealer_hand.get_value()
            score -= 1
            print 'gaya tera paisa paani me... '
            print 'score : ', score
            in_play = False
            
            

def draw(canvas):
    global busted , score
    
    canvas.draw_text('*^*^* BLACKJACK *^*^*',(135,30) , 35,'black')
    
    canvas.draw_text('Your Hand:',(70,230) , 20,'black')
    my_hand.draw(canvas,[50 , HEIGHT - 50 - CARD_SIZE[1]])
    
    canvas.draw_text("Dealer's Hand:",(70,75),20,'black')
    dealer_hand.draw(canvas , [50,100] )
    
    if in_play:
        canvas.draw_text(outcome , (2500,235),30,'black')
    else:
        canvas.draw_text(outcome,(260,235),30,'black')
        
    # dealer ka front/back waala scene
    
    if in_play:
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] , CARD_CENTER[1])
        canvas.draw_image(card_back,card_loc , CARD_SIZE , [50 + CARD_CENTER[0] , 100 + CARD_CENTER[1]] , CARD_SIZE)
        
         
    canvas.draw_text(busted ,(265,385) ,25,'black')
    canvas.draw_text('Score: '+str(score),(480,78),25,'white')

    
frame = simplegui.create_frame("Blackjack", WIDTH , HEIGHT)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


deal()
frame.start()